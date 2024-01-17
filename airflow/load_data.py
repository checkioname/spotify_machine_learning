import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os


load_dotenv()

#Credenciais
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("API_KEY")


# Configurar autenticação
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



import pandas as pd

# Obter informações sobre um artista
artist_id = '7n2Ycct7Beij7Dj7meI4X0'
artist_info = sp.artist(artist_id)
print(artist_info)

print(artist_info.keys())
df = pd.DataFrame({
    'Seguidores': [artist_info['followers']['total']],
    'ID do Artista': [artist_info['id']],
    'Popularidade' : [artist_info['popularity']],
    'Nome' : [artist_info['name']],
    'Genero' : [artist_info['genres']]
})

df