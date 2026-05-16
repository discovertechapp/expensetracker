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
