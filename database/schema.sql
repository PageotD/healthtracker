-- Create USER table
CREATE TABLE IF NOT EXISTS "user" (
    uuid TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    user_id VARCHAR(50) UNIQUE NOT NULL,
    user_name VARCHAR(100) NOT NULL
);

-- Create WEIGHT table
CREATE TABLE IF NOT EXISTS weight (
    uuid TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    user_id TEXT NOT NULL,
    measurement_datetime TIMESTAMP NOT NULL,
    weight_value DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "user"(uuid)
);

-- Create CALORIES table
CREATE TABLE IF NOT EXISTS calories (
    uuid TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    user_id TEXT NOT NULL,
    measurement_datetime TIMESTAMP NOT NULL,
    calories_value DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "user"(uuid)
);

-- Create SLEEP table
CREATE TABLE IF NOT EXISTS  sleep (
    uuid TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    user_id TEXT NOT NULL,
    start_datetime TIMESTAMP NOT NULL,
    end_datetime TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "user"(uuid),
    CHECK (end_datetime > start_datetime)
);

-- Create ACTIVITY table
CREATE TABLE IF NOT EXISTS  activity (
    uuid TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    user_id TEXT NOT NULL,
    start_datetime TIMESTAMP NOT NULL,
    end_datetime TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "user"(uuid),
    CHECK (end_datetime > start_datetime)
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS  idx_weight_user_datetime ON weight(user_id, measurement_datetime);
CREATE INDEX IF NOT EXISTS  idx_calories_user_datetime ON calories(user_id, measurement_datetime);
CREATE INDEX IF NOT EXISTS  idx_sleep_user_datetime ON sleep(user_id, start_datetime);
CREATE INDEX IF NOT EXISTS  idx_activity_user_datetime ON activity(user_id, start_datetime);
