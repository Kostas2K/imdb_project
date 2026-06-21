SELECT titleId, title
FROM {{ source('imdb', 'title_akas') }}
