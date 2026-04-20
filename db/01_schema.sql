-- Reference schema for the Lucy tech-test.
-- Populated with venue metadata and daily revenue targets by 02_seed.sql.

CREATE TABLE venues (
    venue_id   TEXT PRIMARY KEY,
    venue_name TEXT NOT NULL,
    city       TEXT NOT NULL,
    country    TEXT NOT NULL,
    timezone   TEXT NOT NULL  -- IANA tz name, e.g. 'Europe/Stockholm'
);

CREATE TABLE daily_targets (
    venue_id      TEXT NOT NULL REFERENCES venues(venue_id),
    business_date DATE NOT NULL,
    target_eur    INTEGER NOT NULL,
    PRIMARY KEY (venue_id, business_date)
);
