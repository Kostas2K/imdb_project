from google.cloud import bigquery
from google.api_core.exceptions import NotFound

import google.cloud.bigquery

datasets_name = ['names_basics','title_akas','title_basics','title_crew','title_principals','title_ratings']

def create_datasets(project_id, dataset_id,datasets_name):

    client = bigquery.Client(project=project_id)

    dataset_id="{}.{}".format(project_id,dataset_id)

    dataset=bigquery.Dataset(dataset_id)

    try:
        client.get_dataset(dataset_id)
        print("Dataset {} already exists.".format(dataset_id))
    except NotFound:
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = "US"
        dataset = client.create_dataset(dataset, timeout=30)
        print("Dataset {} created.".format(dataset_id))

for name in datasets_name:
    create_datasets('myprojectbq','imdb',name)


