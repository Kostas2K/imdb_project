SELECT nconst, 
    primaryName ,
    birthYear ,
    deathYear ,
    knownForTitles

FROM {{ source('imdb', 'name_basics') }}
