import streamlit as st
import pandas as pd
from faker import Faker

# Initialiser Faker
fake = Faker()

# Générer des données aléatoires
def generate_data(num_entries):
    data = {
        'Nom': [fake.last_name() for _ in range(num_entries)],
        'Prénom': [fake.first_name() for _ in range(num_entries)]
    }
    return pd.DataFrame(data)

# Application Streamlit
st.title("Générateur de Noms et Prénoms")

num_entries = st.number_input("Combien de noms voulez-vous générer ?", min_value=1, max_value=1000, value=10)

if st.button("Générer"):
    df = generate_data(num_entries)
    st.write(df)
    st.download_button("Télécharger le fichier CSV", df.to_csv(index=False).encode('utf-8'), "noms_prenoms.csv", "text/csv")



