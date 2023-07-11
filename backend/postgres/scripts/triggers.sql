create or replace procedure insert_default_user_limits(telegram_id bigint)
language sql as
$$
insert into public.limits (telegram_id, free_requests_count)
VALUES(telegram_id, 3)
on conflict do nothing;
$$;

create or replace function insert_default_user_limits() returns trigger as
$body$
begin
insert into public.limits (telegram_id, free_requests_count)
VALUES(new.telegram_id, 3)
on conflict do nothing;
return new;
end;
$body$
language plpgsql;

create or replace trigger default_user_limits after insert on "public".users
for each row
execute procedure insert_default_user_limits();

create or replace function sync_limits_with_ban_status() returns trigger as
$body$
declare
	user_limits_is_defined	bool;
begin
select exists(select 1 from public.limits where telegram_id = new.telegram_id) into user_limits_is_defined;
if not user_limits_is_defined then
	call insert_default_user_limits(new.telegram_id);
end if;

if new.is_banned then
	update public.limits set daily_requests_count = 0, free_requests_count = 0 where telegram_id = new.telegram_id;
else
	update public.limits set daily_requests_count = 3 where telegram_id = new.telegram_id;
end if;

return null;
end;
$body$
language plpgsql;



create or replace function sync_limits_with_subscription_status() returns trigger as
$body$
declare
	user_limits_is_defined	bool;
begin
select exists(select 1 from public.limits where telegram_id = new.telegram_id) into user_limits_is_defined;
if not user_limits_is_defined then
	call insert_default_user_limits(new.telegram_id);
end if;

if new.is_banned then
	return null;
end if;

if new.is_subscriber then
	update public.limits set daily_requests_count = 10 where telegram_id = new.telegram_id;
else
	update public.limits set daily_requests_count = 3 where telegram_id = new.telegram_id;
end if;
return null;
end;
$body$
language plpgsql;

create or replace trigger sync_limits_with_subscription_status after update of is_subscriber on "public".users
for each row execute procedure sync_limits_with_subscription_status();

create or replace trigger sync_limits_with_ban_status after update of is_banned on "public".users
for each row execute procedure sync_limits_with_ban_status();