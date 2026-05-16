from datetime import datetime

from src.utils.elasticsearch_handler import get_es_client

es = get_es_client()


# ---------------------------------------------------------
# Create Diary Entry
# ---------------------------------------------------------
def create_diary_entry(payload):

    diary_count = es.count(
        index="diary_entries"
    )["count"]

    document = {
        "diary_id": diary_count + 1,
        "user_id": payload["user_id"],
        "title": payload["title"],
        "notes": payload["notes"],
        "entry_date": payload["entry_date"],
        "created_at": str(datetime.now())
    }

    es.index(
        index="diary_entries",
        document=document
    )

    return {
        "status": True,
        "message": "Diary entry created successfully"
    }


# ---------------------------------------------------------
# Get Diary Entries
# ---------------------------------------------------------
def get_diary_entries(user_id):

    response = es.search(
        index="diary_entries",
        body={
            "size": 1000,
            "sort": [
                {
                    "entry_date": {
                        "order": "desc"
                    }
                }
            ],
            "query": {
                "term": {
                    "user_id": user_id
                }
            }
        }
    )

    entries = []

    for hit in response["hits"]["hits"]:

        entry = hit["_source"]

        entry["document_id"] = hit["_id"]

        entries.append(entry)

    return {
        "status": True,
        "data": entries
    }
