create table if not exists driftinfo (
    id integer primary key autoincrement,
    brief_text text (280),
    disturbance integer (1) DEFAULT 0,
    headline text (1000),
    long_text text (3000),
    processed_mail integer (1) DEFAULT 0,
    processed_sms integer (1) DEFAULT 0,
    processed_twitter integer (1) DEFAULT 0,
    processed_wordpress integer (1) DEFAULT 0,
    timestamp TIMESTAMP  DEFAULT CURRENT_TIMESTAMP
);
