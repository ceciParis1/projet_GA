import streamlit as st
from annoy import AnnoyIndex

# On suppose que 'commune_documents' est déjà préparé et que 'commune_embeddings' est disponible
# 'annoy_index' est l'index Annoy déjà créé à partir des embeddings des documents

# Fonction pour rechercher les documents similaires avec Annoy
def search_similar_documents(query_embedding, top_n=5):
    # Trouver les indices des n documents les plus proches dans l'index Annoy
    indices = annoy_index.get_nns_by_vector(query_embedding, top_n)
    # Récupérer les documents correspondants
    return [commune_documents[i]["page_content"] for i in indices]

# Interface Streamlit
st.title("Assistant IA - Taux de couverture FTTH")

# Entrée de la requête utilisateur
user_query = st.text_input("Posez votre question sur la couverture FTTH :")

# Lorsque l'utilisateur soumet une question
if st.button("Générer une réponse"):
    if user_query:
        # Embedder la requête
        query_embedding = embedding_model.embed_documents([user_query])[0]
        
        # Recherche des documents pertinents
        similar_documents = search_similar_documents(query_embedding)
        
        # Afficher les documents similaires
        st.write("Documents pertinents :")
        for doc in similar_documents:
            st.write(f"- {doc}")
    else:
        st.write("Veuillez entrer une question.")