from . import db
from pymongo import ReturnDocument


def updateUser(date_time, discord_id):
    # Select database and collection
    database = db.get_connection()
    collection = database["users"]

    # search document
    doc = {"discord_id": discord_id}

    # Create an update operator
    newvalues = {"$set": {"last_spin": date_time}}

    # Actualizar el primer documento que tenga edad 30
    try:
        result = collection.update_one(doc, newvalues)
        return {"status": "succes", "result": result}
    except Exception as e:
        return {"status": "error", "error": e}
