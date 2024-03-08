import streamlit as st
import mysql.connector
import os
import urllib.parse

st.title("Hello World")

# Récupérer la chaîne de connexion à partir de la variable d'environnement
conn_str = os.environ.get("DATABASE_URLS")

# Analyser l'URL de la base de données
conn_params = urllib.parse.urlparse(conn_str)
# Extrait les paramètres de connexion
username = conn_params.username
password = conn_params.password
host = conn_params.hostname
database = conn_params.path[1:]  # Supprime le premier caractère '/'
port = conn_params.port

# Se connecter à la base de données
cnx = mysql.connector.connect(
    host=host,
    user=username,
    password=password,
    database=database,
    port=port
)

# Créer un curseur pour exécuter des requêtes
cursor = cnx.cursor()

# Exécuter une requête pour sélectionner tous les éléments de la table
cursor.execute("SELECT * FROM users")

# Récupérer les résultats de la requête
results = cursor.fetchall()

# Fermer le curseur et la connexion à la base de données
cursor.close()
cnx.close()

# Afficher les résultats dans Streamlit
st.write("Éléments de la table :")
for row in results:
  st.write(row)
