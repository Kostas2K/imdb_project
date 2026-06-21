from google.cloud import bigquery

def load_gcs_to_bq(table_schema):
    client = bigquery.Client(project='myprojectbq-328820')

    project_id='myprojectbq-328820'
    dataset_id='imdb'
    GCS_URI='gs://kk_imdb_data/imdb/data/title.basics.tsv'
    
    table_id = "{}.{}".format(project_id, dataset_id)
    

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )

    load_job=client.load_table_from_uri(
       GCS_URI,
       table_id,
       job_config=job_config
    )

    load_job.result()

    table = client.get_table(table_id)
    print("Loaded {} rows into {}".format(table.num_rows, table_id))

bigquery_table_schema = [
    bigquery.SchemaField("tconst", "STRING", mode="REQUIRED",description="Unique id for each title"),
    bigquery.SchemaField("titleType", "INTEGER",mode="REQUIRED",description="Type of show with main distinction between episodes and movies"),
    bigquery.SchemaField("primaryTitle", "STRING", mode="NULLABLE", description="Title of the show. For series, it mainly is the episode number"),
    bigquery.SchemaField("originalTitle", "STRING", mode="NULLABLE", description="Same as primary title"),
    bigquery.SchemaField("isAdult", "BOOLEAN",mode="NULLABLE",description="Whether the title is an adult"),
    bigquery.SchemaField("startYear", " INTEGER",mode="NULLABLE",description="Year the title was released"),
    bigquery.SchemaField("endYear", "STRING", mode="NULLABLE",description="Mainly missing field"),
    bigquery.SchemaField("runtimeMinutes", "INTEGER", mode="NULLABLE",description="Duration of the title in minutes"),
    bigquery.SchemaField("genres", "STRING", mode="NULLABLE",description="Genres of the title"),
]

if __name__ == "__main__":
    load_gcs_to_bq(bigquery_table_schema)

