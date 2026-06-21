 SELECT *
  FROM {{ source('imdb', 'title_ratings') }}