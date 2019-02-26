create table if not exists driftinfo (
    id integer primary key autoincrement,
    brief_text text (280),
    disturbance integer (1) DEFAULT 0,
    headline text (1000),
    long_text text (3000),
    processed_mail TIMESTAMP DEFAULT 0,
    processed_sms TIMESTAMP DEFAULT 0,
    processed_twitter TIMESTAMP DEFAULT 0,
    processed_wordpress TIMESTAMP DEFAULT 0,
    timestamp TIMESTAMP  DEFAULT CURRENT_TIMESTAMP,
    username text (100)
);
