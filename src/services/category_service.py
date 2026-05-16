from datetime import datetime

from src.utils.elasticsearch_handler import get_es_client

es = get_es_client()


# ---------------------------------------------------------
# Create Category
# ---------------------------------------------------------
def create_category(payload):

    category_count = es.count(
        index="categories"
    )["count"]

    document = {
        "category_id": category_count + 1,
        "main_category": payload["main_category"],
        "sub_category": payload["sub_category"],
        "created_at": str(datetime.now())
    }

    es.index(
        index="categories",
        document=document
    )

    return {
        "status": True,
        "message": "Category created successfully"
    }


# ---------------------------------------------------------
# Get Categories
# ---------------------------------------------------------
def get_categories():

    response = es.search(
        index="categories",
        body={
            "size": 1000,
            "query": {
                "match_all": {}
            }
        }
    )

    categories = []

    for hit in response["hits"]["hits"]:

        categories.append(
            hit["_source"]
        )

    return {
        "status": True,
        "data": categories
    }
