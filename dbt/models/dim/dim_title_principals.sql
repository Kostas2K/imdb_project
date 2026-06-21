{{
    config(
        materialized='table',
        tags=['dim', 'title_principals'],

    )
}}

SELECT *
FROM {{ ref('src_title_principals') }} 