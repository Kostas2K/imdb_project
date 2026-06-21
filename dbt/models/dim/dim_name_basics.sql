{{
    config(
        materialized='table',
        tags=['dim', 'name_basics']
    )
}}

SELECT *
FROM {{ ref('src_name_basics') }}