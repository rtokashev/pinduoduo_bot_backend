create extension pg_cron;
select cron.schedule('update-expired-joint-purchase-request', '0 0 * * *', $$UPDATE joint_purchase_request set is_active = false where created_at < now()::timestamp - interval '7 days' $$);
select cron.schedule('update-expired-users-subscriptions', '5 0 * * *', $$ UPDATE users SET is_subscriber = false, subscription_end_date = null WHERE subscription_end_date::timestamp < now()::timestamp $$);
