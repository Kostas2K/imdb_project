{{ 
(
    config(
        materialized='table',
        tags=['dim', 'title_ratings']
    )
)
}}

SELECT *
FROM {{ ref('src_title_ratings') }} AS ratings