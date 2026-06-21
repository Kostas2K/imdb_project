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
    bigquery.SchemaField("nconst", "STRING", mode="NULLABLE", description="Unique id for the name/person"),
    bigquery.SchemaField("primaryName", "STRING", mode="NULLABLE", description="Name by which the person is most often credited in the dataset"),
    bigquery.SchemaField("birthYear", "INTEGER", mode="NULLABLE", description="The year in which the person was born. If the birth year is not known, value will be missing."),
    bigquery.SchemaField("deathYear", "INTEGER", mode="NULLABLE", description="The year in which the person died. If the death year is not known, value will be missing"),
    bigquery.SchemaField("primaryProfession", "STRING", mode="NULLABLE", description="The top-3 professions of the person, separated by commas. If known, it will be sorted"),
    bigquery.SchemaField("knownForTitles", "STRING", mode="NULLABLE", description="Titles the person is known for, separated by commas. The ordering of the titles in this field is not significant, since it is just a subset of the titles in the title.principals.tsv"),
]

if __name__ == "__main__":
    load_gcs_to_bq(bigquery_table_schema)

