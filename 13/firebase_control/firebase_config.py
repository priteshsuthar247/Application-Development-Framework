import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase
cred = credentials.Certificate("13/firebase_control/firebase_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://led-controller-697a9-default-rtdb.firebaseio.com/'
})

# Get a reference to the database service
ref = db.reference('/')