SELECT
    (SELECT COUNT(*) FROM orders_source) AS source_count,
    (SELECT COUNT(*) FROM orders_target) AS target_count;
