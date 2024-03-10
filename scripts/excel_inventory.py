import pandas as pd
from pymongo import MongoClient

# Conexión a MongoDB
# TODO: Se debe hacer un env para reemplazar esta cadena de conexiòn
# client = MongoClient("mongodb://mongo_db:27017/inventory")
client = MongoClient("mongodb://127.0.0.1:27017/inventory")
# TODO: La DB se debería de llamar inventory 
db = client["inventory"]
collection = db["products"]

# Leer el archivo Excel
df = pd.read_excel("lista_radiadores_general_c_medida.xlsx")

# Convertir el DataFrame de pandas a una lista de diccionarios
data = df.to_dict(orient="records")

# Insertar los datos en la colección de MongoDB
collection.insert_many(data)

print("Datos insertados correctamente en MongoDB.")
