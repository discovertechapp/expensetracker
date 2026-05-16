from datetime import datetime

from src.utils.elasticsearch_handler import get_es_client

es = get_es_client()


# ---------------------------------------------------------
# Create Expense
# ---------------------------------------------------------
def create_expense(payload):

    expense_count = es.count(
        index="expenses"
    )["count"]

    document = {
        "expense_id": expense_count + 1,
        "user_id": payload["user_id"],
        "main_category": payload["main_category"],
        "sub_category": payload["sub_category"],
        "amount": payload["amount"],
        "description": payload.get("description", ""),
        "expense_date": payload["expense_date"],
        "created_at": str(datetime.now())
    }

    es.index(
        index="expenses",
        document=document
    )

    return {
        "status": True,
        "message": "Expense added successfully"
    }


# ---------------------------------------------------------
# Get Expenses
# ---------------------------------------------------------
def get_expenses(user_id=None):

    query = {
        "match_all": {}
    }

    if user_id:

        query = {
            "term": {
                "user_id": user_id
            }
        }

    response = es.search(
        index="expenses",
        body={
            "size": 1000,
            "sort": [
                {
                    "expense_date": {
                        "order": "desc"
                    }
                }
            ],
            "query": query
        }
    )

    expenses = []

    for hit in response["hits"]["hits"]:

        expense = hit["_source"]

        expense["document_id"] = hit["_id"]

        expenses.append(expense)

    return {
        "status": True,
        "data": expenses
    }


# ---------------------------------------------------------
# Update Expense
# ---------------------------------------------------------
def update_expense(document_id, payload):

    existing_doc = es.get(
        index="expenses",
        id=document_id
    )

    expense = existing_doc["_source"]

    expense["main_category"] = payload["main_category"]
    expense["sub_category"] = payload["sub_category"]
    expense["amount"] = payload["amount"]
    expense["description"] = payload.get(
        "description",
        ""
    )
    expense["expense_date"] = payload["expense_date"]

    es.index(
        index="expenses",
        id=document_id,
        document=expense
    )

    return {
        "status": True,
        "message": "Expense updated successfully"
    }


# ---------------------------------------------------------
# Delete Expense
# ---------------------------------------------------------
def delete_expense(document_id):

    es.delete(
        index="expenses",
        id=document_id
    )

    return {
        "status": True,
        "message": "Expense deleted successfully"
    }
