{{
    config(
        materialized='table',
        tags=['dim', 'title_akas']
    )
}}

SELECT *
FROM {{ ref('src_title_akas') }} 