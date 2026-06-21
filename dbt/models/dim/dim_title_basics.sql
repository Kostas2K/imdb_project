{{
    config(
        materialized='table',
        tags=['dim', 'title_basics']

    )
}}

SELECT *
FROM {{ ref('src_title_basics') }} 
