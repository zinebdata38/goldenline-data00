from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Configurer Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Vue à afficher pour la connexion

# Modèle d'utilisateur de base avec Flask-Login
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Exemple d'une base de données d'utilisateurs
users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}

# Gestion du chargement de l'utilisateur
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Définir une route pour le login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('dashboard'))
        return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

# Définir une route pour le tableau de bord
@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hello, {current_user.id}! Welcome to your dashboard.'

# Définir une route pour la déconnexion
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Définir une route pour la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')  # Renvoyer un fichier HTML pour la page d'accueil

# Définir le port dynamique pour Heroku ou un port local
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)

