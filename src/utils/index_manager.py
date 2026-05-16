from src.utils.elasticsearch_handler import get_es_client

es = get_es_client()


def create_indices():

    indices = [
        "users",
        "expenses",
        "categories",
        "diary_entries"
    ]

    for index_name in indices:

        if not es.indices.exists(index=index_name):

            es.indices.create(index=index_name)

            print(f"{index_name} index created")

        else:
            print(f"{index_name} index already exists")
