create extension pg_cron;
select cron.schedule('update-expired-joint-purchase-request', '0 0 * * *', $$UPDATE joint_purchase_request set is_active = false where created_at < now()::timestamp - interval '7 days' $$);
select cron.schedule('update-expired-users-subscriptions', '5 0 * * *', $$ UPDATE users SET is_subscriber = false, subscription_end_date = null WHERE subscription_end_date::timestamp < now()::timestamp $$);

create or replace procedure update_available_user_limits()
language plpgsql as
$$
declare
daily_used_limits smallint ;
remaining_total_limits smallint;
limits_row record;
begin
	for limits_row in select * from "public".limits
	loop
		daily_used_limits := case
			when limits_row.total_requests_count >= 3 then 3
			when limits_row.total_requests_count < 3 and limits_row.total_requests_count > 0 then limits_row.total_requests_count
			else 0
			end;
		remaining_total_limits := case
			when limits_row.total_requests_count > 3 then limits_row.total_requests_count - 3
			else 0
			end;

		update limits
			set daily_requests_count = daily_used_limits, total_requests_count = remaining_total_limits
		where id = limits_row.id;

	end loop;
end
$$;
-- антипаттерн делать обновление в цикле for, переписать как будет время

select cron.schedule('update-available-user-limits', '0 10 * * *', $$ call update_available_user_limits() $$);