{{
    config(
        materialized='table',
        tags=['dim', 'names_with_principals']
    )
}}




WITH NB AS (
    SELECT NB.*
    FROM {{ ref('dim_name_basics') }} AS NB
),

TB AS (
SELECT TB.tconst, TB.nconst
FROM {{ ref('dim_title_principals')}} AS TB
),

TA AS (
    SELECT DISTINCT titleId, title
    FROM {{ ref('dim_title_akas') }} AS TA
)

SELECT NB.*, TB.tconst, TA.title
FROM NB
INNER JOIN TB
ON NB.nconst  = TB.nconst
INNER JOIN TA
ON TB.tconst = TA.titleId
