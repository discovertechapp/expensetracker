from src.utils.elasticsearch_handler import get_es_client

es = get_es_client()


# ---------------------------------------------------------
# Dashboard Summary
# ---------------------------------------------------------
def get_dashboard_summary(user_id):

    response = es.search(
        index="expenses",
        body={
            "size": 0,
            "query": {
                "term": {
                    "user_id": user_id
                }
            },
            "aggs": {
                "total_expense": {
                    "sum": {
                        "field": "amount"
                    }
                },
                "category_summary": {
                    "terms": {
                        "field": "main_category.keyword"
                    },
                    "aggs": {
                        "total_amount": {
                            "sum": {
                                "field": "amount"
                            }
                        }
                    }
                }
            }
        }
    )

    total_expense = response["aggregations"][
        "total_expense"
    ]["value"]

    categories = []

    for bucket in response["aggregations"][
        "category_summary"
    ]["buckets"]:

        categories.append({
            "category": bucket["key"],
            "amount": bucket["total_amount"]["value"]
        })

    return {
        "status": True,
        "data": {
            "total_expense": total_expense,
            "category_summary": categories
        }
    }
