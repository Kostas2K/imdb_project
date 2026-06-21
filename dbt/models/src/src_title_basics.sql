SELECT tconst, titleType, primaryTitle, runtimeMinutes, genres, startYear, endYear
FROM {{ source('imdb', 'title_basics') }}
