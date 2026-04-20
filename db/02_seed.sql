-- Seed data for the Lucy tech-test.
--
-- Five venues across Europe plus daily revenue targets for the test window
-- 2026-04-07 … 2026-04-16 (10 business days).

INSERT INTO venues (venue_id, venue_name, city, country, timezone) VALUES
    ('v_sto', 'Storgatan Bistro',  'Stockholm', 'SE', 'Europe/Stockholm'),
    ('v_lon', 'Shoreditch Kitchen', 'London',   'GB', 'Europe/London'),
    ('v_ber', 'Kreuzberg Küche',   'Berlin',   'DE', 'Europe/Berlin'),
    ('v_mad', 'Malasaña Taberna',  'Madrid',   'ES', 'Europe/Madrid'),
    ('v_hel', 'Kallio Keittiö',    'Helsinki', 'FI', 'Europe/Helsinki');

-- Daily targets. Weekdays at venue base level; Fri/Sat ~1.5×; Sun ~0.85×.
-- Amounts rounded to the nearest 50 EUR. Integer EUR per schema.

INSERT INTO daily_targets (venue_id, business_date, target_eur) VALUES
    -- v_sto: base 5200 EUR
    ('v_sto', '2026-04-07', 5200),   -- Tue
    ('v_sto', '2026-04-08', 5200),   -- Wed
    ('v_sto', '2026-04-09', 5200),   -- Thu
    ('v_sto', '2026-04-10', 7800),   -- Fri
    ('v_sto', '2026-04-11', 7800),   -- Sat
    ('v_sto', '2026-04-12', 4400),   -- Sun
    ('v_sto', '2026-04-13', 5200),   -- Mon
    ('v_sto', '2026-04-14', 5200),   -- Tue
    ('v_sto', '2026-04-15', 5200),   -- Wed
    ('v_sto', '2026-04-16', 5200),   -- Thu

    -- v_lon: base 6000 EUR
    ('v_lon', '2026-04-07', 6000),
    ('v_lon', '2026-04-08', 6000),
    ('v_lon', '2026-04-09', 6000),
    ('v_lon', '2026-04-10', 9000),
    ('v_lon', '2026-04-11', 9000),
    ('v_lon', '2026-04-13', 6000),
    ('v_lon', '2026-04-14', 6000),
    ('v_lon', '2026-04-15', 6000),
    ('v_lon', '2026-04-16', 6000),

    -- v_ber: base 4500 EUR
    ('v_ber', '2026-04-07', 4500),
    ('v_ber', '2026-04-08', 4500),
    ('v_ber', '2026-04-10', 6750),
    ('v_ber', '2026-04-11', 6750),
    ('v_ber', '2026-04-12', 3800),
    ('v_ber', '2026-04-13', 4500),
    ('v_ber', '2026-04-14', 4500),
    ('v_ber', '2026-04-15', 4500),
    ('v_ber', '2026-04-16', 4500),

    -- v_mad: base 4000 EUR
    ('v_mad', '2026-04-07', 4000),
    ('v_mad', '2026-04-08', 4000),
    ('v_mad', '2026-04-09', 4000),
    ('v_mad', '2026-04-10', 6000),
    ('v_mad', '2026-04-11', 6000),
    ('v_mad', '2026-04-12', 3400),
    ('v_mad', '2026-04-13', 4000),
    ('v_mad', '2026-04-14', 4000),
    ('v_mad', '2026-04-15', 4000),

    -- v_hel: base 3200 EUR
    ('v_hel', '2026-04-07', 3200),
    ('v_hel', '2026-04-08', 3200),
    ('v_hel', '2026-04-09', 3200),
    ('v_hel', '2026-04-10', 4800),
    ('v_hel', '2026-04-11', 4800),
    ('v_hel', '2026-04-12', 2700),
    ('v_hel', '2026-04-13', 3200),
    ('v_hel', '2026-04-14', 3200),
    ('v_hel', '2026-04-15', 3200),
    ('v_hel', '2026-04-16', 3200),

    ('v_sto', '2026-04-05', 55000),
    ('v_hel', '2026-04-20', 48000);
