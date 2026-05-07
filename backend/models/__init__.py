# Importer dans l'ordre
from models.pages import Page
from models.users import User
from models.posts import Post
from models.recrutements import Recrutement
from models.tache import Tache

# Export tous les modèles
__all__ = ['Page', 'User', 'Post', 'Recrutement', 'Tache']