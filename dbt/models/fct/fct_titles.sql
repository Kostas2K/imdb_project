{{ config(
    materialized='table',
    tags=['fact']
) }}


WITH names_principals AS (
SELECT NP.tconst, NP.primaryName, NP.birthYear, NP.deathYear, NP.title --  birth year and death year not added in the fact table
FROM {{ ref('dim_names_w_principals') }} AS NP
),

title_ratings AS (
SELECT tconst, AVG(averageRating) AS avgRating, SUM(numVotes) AS nrVotes
FROM {{ ref('dim_title_ratings') }} AS TR
GROUP BY tconst
),

title_principals AS (
select tconst, count(nconst) as nr_subjects_per_title
from {{ ref('dim_title_principals') }}
GROUP BY tconst
--HAVING COUNT(nconst)>1
ORDER BY 2 DESC
),

title_basics AS (
  SELECT tconst, genres, AVG(runtimeMinutes) AS avg_runtime, startYear, endYear, titleType
  FROM {{ ref('dim_title_basics') }}
  GROUP BY tconst, genres, startYear, endYear, titleType
  ORDER BY avg_runtime DESC)

SELECT DISTINCT NP.tconst, NP.primaryName, NP.title,
TR.avgRating, TR.nrVotes, 
TP.nr_subjects_per_title, 
TB.genres, TB.avg_runtime,
TB.startYear, TB.endYear, TB.titleType
FROM names_principals AS NP

INNER JOIN title_ratings AS TR
ON NP.tconst = TR.tconst

INNER JOIN title_basics AS TB  
ON NP.tconst = TB.tconst

INNER JOIN title_principals AS TP
ON NP.tconst = TP.tconst