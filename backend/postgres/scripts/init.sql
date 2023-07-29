BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 60f1d9725e31

CREATE TABLE joint_purchase_request (
    id SERIAL NOT NULL, 
    chat_id BIGINT NOT NULL, 
    link VARCHAR NOT NULL, 
    goods_id INTEGER NOT NULL, 
    photo TEXT NOT NULL, 
    post_id INTEGER NOT NULL, 
    post_url VARCHAR NOT NULL, 
    is_active BOOLEAN, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    UNIQUE (chat_id), 
    UNIQUE (link)
);

CREATE INDEX ix_joint_purchase_request_created_at ON joint_purchase_request (created_at);

CREATE INDEX ix_joint_purchase_request_goods_id ON joint_purchase_request (goods_id);

CREATE INDEX ix_joint_purchase_request_id ON joint_purchase_request (id);

CREATE TABLE users (
    id SERIAL NOT NULL, 
    telegram_id BIGINT NOT NULL, 
    phone VARCHAR, 
    username VARCHAR NOT NULL, 
    language_code VARCHAR, 
    is_banned BOOLEAN, 
    is_subscriber BOOLEAN, 
    subscription_end_date BOOLEAN, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    UNIQUE (phone), 
    UNIQUE (telegram_id), 
    UNIQUE (telegram_id, phone)
);

CREATE INDEX ix_users_id ON users (id);

CREATE INDEX ix_users_subscription_end_date ON users (subscription_end_date);

INSERT INTO alembic_version (version_num) VALUES ('60f1d9725e31') RETURNING alembic_version.version_num;

-- Running upgrade 60f1d9725e31 -> ede678fe4a48

CREATE TABLE referrals (
    id SERIAL NOT NULL, 
    user_id BIGINT NOT NULL, 
    referred_id BIGINT, 
    PRIMARY KEY (id), 
    UNIQUE (user_id)
);

CREATE INDEX ix_referrals_id ON referrals (id);

UPDATE alembic_version SET version_num='ede678fe4a48' WHERE alembic_version.version_num = '60f1d9725e31';

-- Running upgrade ede678fe4a48 -> 08be2b3c47b9

ALTER TABLE referrals ADD COLUMN created_at TIMESTAMP WITHOUT TIME ZONE;

CREATE INDEX ix_referrals_created_at ON referrals (created_at);

ALTER TABLE users ADD COLUMN create_time_holder TIMESTAMP without time zone NULL;

ALTER TABLE users ALTER COLUMN subscription_end_date TYPE timestamp without time zone USING create_time_holder;

ALTER TABLE users DROP COLUMN create_time_holder;

UPDATE alembic_version SET version_num='08be2b3c47b9' WHERE alembic_version.version_num = 'ede678fe4a48';

-- Running upgrade 08be2b3c47b9 -> d741067358c5

ALTER TABLE joint_purchase_request ADD FOREIGN KEY(chat_id) REFERENCES users (telegram_id);

UPDATE alembic_version SET version_num='d741067358c5' WHERE alembic_version.version_num = '08be2b3c47b9';

-- Running upgrade d741067358c5 -> 8b0411711a52

ALTER TABLE joint_purchase_request DROP CONSTRAINT joint_purchase_request_chat_id_key;

UPDATE alembic_version SET version_num='8b0411711a52' WHERE alembic_version.version_num = 'd741067358c5';

-- Running upgrade 8b0411711a52 -> 10d0409b776c

CREATE TABLE limits (
    id SERIAL NOT NULL, 
    telegram_id BIGINT NOT NULL, 
    free_requests_count SMALLINT NOT NULL, 
    total_requests_count SMALLINT, 
    daily_requests_count SMALLINT, 
    PRIMARY KEY (id), 
    FOREIGN KEY(telegram_id) REFERENCES users (telegram_id), 
    UNIQUE (telegram_id)
);

CREATE INDEX ix_limits_id ON limits (id);

UPDATE alembic_version SET version_num='10d0409b776c' WHERE alembic_version.version_num = '8b0411711a52';

-- Running upgrade 10d0409b776c -> cb95394e547a

ALTER TABLE limits ADD COLUMN available_requests_count SMALLINT;

UPDATE alembic_version SET version_num='cb95394e547a' WHERE alembic_version.version_num = '10d0409b776c';

-- Running upgrade cb95394e547a -> 2aba664e93d3

ALTER TABLE limits DROP COLUMN total_requests_count;

ALTER TABLE limits DROP COLUMN available_requests_count;

UPDATE alembic_version SET version_num='2aba664e93d3' WHERE alembic_version.version_num = 'cb95394e547a';

-- Running upgrade 2aba664e93d3 -> 5f7424f44f88

CREATE TABLE reviews (
    id SERIAL NOT NULL, 
    post_id INTEGER NOT NULL, 
    post_url VARCHAR NOT NULL, 
    goods_id INTEGER NOT NULL, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id)
);

CREATE INDEX ix_reviews_created_at ON reviews (created_at);

CREATE INDEX ix_reviews_goods_id ON reviews (goods_id);

CREATE INDEX ix_reviews_id ON reviews (id);

UPDATE alembic_version SET version_num='5f7424f44f88' WHERE alembic_version.version_num = '2aba664e93d3';

-- Running upgrade 5f7424f44f88 -> 2c83c258aca5

UPDATE alembic_version SET version_num='2c83c258aca5' WHERE alembic_version.version_num = '5f7424f44f88';

-- Running upgrade 2c83c258aca5 -> 5a0740b3c451

ALTER TABLE reviews ADD COLUMN goods_url VARCHAR(2048);

UPDATE alembic_version SET version_num='5a0740b3c451' WHERE alembic_version.version_num = '2c83c258aca5';

-- Running upgrade 5a0740b3c451 -> 992fc7037940

CREATE TABLE cargo (
    id SERIAL NOT NULL, 
    chat_id BIGINT NOT NULL, 
    weight FLOAT NOT NULL, 
    price INTEGER NOT NULL, 
    paid BOOLEAN, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    FOREIGN KEY(chat_id) REFERENCES users (telegram_id)
);

CREATE INDEX ix_cargo_created_at ON cargo (created_at);

CREATE INDEX ix_cargo_id ON cargo (id);

UPDATE alembic_version SET version_num='992fc7037940' WHERE alembic_version.version_num = '5a0740b3c451';

-- Running upgrade 992fc7037940 -> e9966e15bddf

ALTER TABLE joint_purchase_request ALTER COLUMN goods_id TYPE BIGINT;

ALTER TABLE reviews ALTER COLUMN goods_id TYPE BIGINT;

UPDATE alembic_version SET version_num='e9966e15bddf' WHERE alembic_version.version_num = '992fc7037940';

COMMIT;
