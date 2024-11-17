from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///local.db'  # Utilise PostgreSQL en production et SQLite en local
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configuration de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Modèle d'utilisateur
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route pour se connecter
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
        return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

# Route pour le tableau de bord
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)

# Route pour se déconnecter
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Route pour afficher la liste des utilisateurs
@app.route('/list_users')
@login_required
def list_users():
    users = User.query.all()
    return render_template('list_users.html', users=users)

# Route pour créer un nouvel utilisateur
@app.route('/create_user', methods=['GET', 'POST'])
@login_required
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Vérifier si l'utilisateur existe déjà
        if User.query.filter_by(username=username).first():
            return render_template('create_user.html', error="User already exists")
        
        # Créer et ajouter l'utilisateur
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('list_users'))
    return render_template('create_user.html')

# Route pour supprimer un utilisateur
@app.route('/delete_user/<int:user_id>')
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('list_users'))

# Route pour la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

# Commande CLI pour initialiser la base de données
@app.cli.command("init-db")
def init_db():
    """Créer la base de données et ajouter un utilisateur par défaut."""
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        admin = User(username="admin", password="admin")
        db.session.add(admin)
        db.session.commit()
    print("Base de données initialisée avec succès.")

# Démarrage de l'application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)

