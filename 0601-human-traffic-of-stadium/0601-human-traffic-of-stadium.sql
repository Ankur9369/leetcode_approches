WITH filtered AS (
    SELECT *,
           id - ROW_NUMBER() OVER (ORDER BY id) as grp
    FROM Stadium
    WHERE people >= 100
),
grouped AS (
    SELECT *,
           COUNT(*) OVER (PARTITION BY grp) as consecutive_count
    FROM filtered
)
SELECT id, visit_date, people
FROM grouped
WHERE consecutive_count >= 3
ORDER BY visit_date;