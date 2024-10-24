import unittest
from flask import Flask
from flask_login import LoginManager
from your_flask_app import app, User  # Remplace par le nom de ton fichier Flask

class FlaskTestCase(unittest.TestCase):
    
    def setUp(self):
        # Créer un client de test
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.login_manager = LoginManager()
        self.login_manager.init_app(app)
        
    def test_login_page(self):
        # Test que la page de connexion se charge correctement
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Nom d\'utilisateur', response.data)  # Vérifie si 'Nom d\'utilisateur' est présent

    def test_dashboard_access(self):
        # Test d'accès au tableau de bord après connexion
        with self.app:
            self.app.post('/login', data=dict(username='admin', password='adminpass'))  # Remplace par les identifiants valides
            response = self.app.get('/dashboard')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Bienvenue dans le tableau de bord', response.data)  # Vérifie le message d'accueil

    def test_admin_access(self):
        # Test d'accès à la page admin
        with self.app:
            self.app.post('/login', data=dict(username='admin', password='adminpass'))  # Remplace par les identifiants valides
            response = self.app.get('/admin')
            self.assertEqual(response.status_code, 200)  # Vérifie que l'accès est autorisé

    def test_marketing_access(self):
        # Test d'accès à la page marketing
        with self.app:
            self.app.post('/login', data=dict(username='marketing', password='marketingpass'))  # Remplace par les identifiants valides
            response = self.app.get('/marketing')
            self.assertEqual(response.status_code, 200)  # Vérifie que l'accès est autorisé

if __name__ == '__main__':
    unittest.main()

