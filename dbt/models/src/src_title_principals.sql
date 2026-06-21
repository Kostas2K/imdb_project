 SELECT tconst, nconst
  FROM {{ source('imdb', 'title_principals') }}