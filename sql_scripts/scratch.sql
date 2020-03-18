
WITH corona_cte AS (
    SELECT *,
           row_number() OVER (ORDER BY last_update)                    AS row_num
    FROM  corona_info
    WHERE province_name = 'Hubei'
)
SELECT current_row.*,
       current_row.confirmed - COALESCE(previous_row.confirmed, 0)      AS  confirmed_delta
FROM        corona_cte     current_row
LEFT JOIN   corona_cte     previous_row ON current_row.row_num = previous_row.row_num + 1
ORDER BY row_num DESC

