import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db


cred = credentials.Certificate("./config/python-example-qs-firebase-adminsdk-9qe7k-2d1e6b36d1.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://python-example-qs-default-rtdb.firebaseio.com/'})

# Crea un colecion(tabla) con el nombre Productos
STR_COLECTION = 'Products'

# Agregar PUSH
# ref = db.reference(STR_COLECTION)
# ref.push({
#   "id": "2340a855-fcb1-4b2f-8cf1-14b27a241f54",
#   "name": "Syrup - Monin - Blue Curacao",
#   "count": 93,
#   "price": "$2221.59",
#   "descripcion": "Stereotactic Gamma Beam Radiosurgery of Thorax Lymphatics",
#   "url": "http://dummyimage.com/160x100.png/cc0000/ffffff"
# })

db = firestore.client()
ref = db.collection(STR_COLECTION)
ref.document('2340a855-fcb1-4b2f-8cf1-14b27a241f54').set({
  "name": "Syrup - Monin - Blue Curacao",
  "count": 93,
  "price": "$2221.59",
  "descripcion": "Stereotactic Gamma Beam Radiosurgery of Thorax Lymphatics",
  "url": "http://dummyimage.com/160x100.png/cc0000/ffffff"
})

#Obtener todos los elementos GET
ref = db.reference(STR_COLECTION)
get_all = ref.get()
print(get_all)