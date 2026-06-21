from google.cloud import bigquery

def load_gcs_to_bq(table_schema):
    client = bigquery.Client(project='myprojectbq-328820')

    project_id='myprojectbq-328820'
    dataset_id='imdb'
    GCS_URI='gs://kk_imdb_data/imdb/data/title.principals.tsv'
    
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
    bigquery.SchemaField("ordering", "INTEGER",mode="REQUIRED",description="A number to uniquely identify rows for a given titleId"),
    bigquery.SchemaField("nconst", "STRING", mode="NULLABLE", description="Unique id for the name/person"),
    bigquery.SchemaField("category", "STRING", mode="NULLABLE", description="The category of job that person was in"),
    bigquery.SchemaField("job", "STRING", mode="NULLABLE", description="The specific job title that person had"),
    bigquery.SchemaField("characters", "STRING", mode="NULLABLE", description="The name of the character played if the category is actor or actress"),
]

if __name__ == "__main__":
    load_gcs_to_bq(bigquery_table_schema)

