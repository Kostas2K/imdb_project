from google.cloud import bigquery

def load_gcs_to_bq(table_schema):
    client = bigquery.Client(project='myprojectbq-328820')

    project_id='myprojectbq-328820'
    dataset_id='imdb'
    GCS_URI='gs://kk_imdb_data/imdb/data/title.akas.tsv'
    
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
    bigquery.SchemaField("titleId", "STRING", mode="NULLABLE", description="Unique id for each title"),
    bigquery.SchemaField("ordering", "INTEGER", mode="NULLABLE", description="A number to uniquely identify rows for a given titleId"),
    bigquery.SchemaField("title", "STRING", mode="NULLABLE", description="The localized title"),
    bigquery.SchemaField("region", "STRING", mode="NULLABLE", description="The region for this version of the title"),
    bigquery.SchemaField("language", "STRING", mode="NULLABLE", description="The language of the title"),
    bigquery.SchemaField("types", "STRING", mode="NULLABLE", description="Types the title is known for, separated by commas"),
    bigquery.SchemaField("attributes", "STRING", mode="NULLABLE", description="Attributes of the title, separated by commas"),
    bigquery.SchemaField("isOriginalTitle", "BOOLEAN", mode="NULLABLE", description="0: not original title, 1: original title"),
    ]

if __name__ == "__main__":
    load_gcs_to_bq(bigquery_table_schema)

