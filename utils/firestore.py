from firebase_admin import credentials, firestore, initialize_app
from datetime import datetime, timedelta

cred = credentials.Certificate("firebase/serviceAccountKey.json")
initialize_app(cred)
db = firestore.client()

def create_pass(user_id, pass_type):
    trips_map = {"daily": 2, "weekly": 10, "monthly": 30}
    expiry_map = {"daily": 3, "weekly": 15, "monthly": 60}

    expiry_date = (datetime.now() + timedelta(days=expiry_map[pass_type])).isoformat()
    db.collection("passes").add({
        "userId": user_id,
        "passType": pass_type,
        "tripsRemaining": trips_map[pass_type],
        "expiryDate": expiry_date
    })
