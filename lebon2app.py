# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Route pour la racine (/)
@app.route('/')
def index():
    return redirect(url_for('reception'))

# Route pour la première page
@app.route('/reception')
def reception():
    return render_template('reception.html')

# Route pour la deuxième page
@app.route('/connexion')
def connexion():
    return render_template('connexion.html')

# Route pour la troisième page
@app.route('/card')
def card():
    return render_template('card.html')

# Route pour la cinquième page
@app.route('/compte')
def compte():
    return render_template('compte.html')

# Route pour la sixième page
@app.route('/virement')
def virement():
    return render_template('virement.html')

# Redirections
@app.route('/next/<current_page>')
def next_page(current_page):
    if current_page == 'reception':
        return redirect(url_for('connexion'))
    elif current_page == 'connexion':
        return redirect(url_for('card'))
    elif current_page == 'card':
        return redirect(url_for('compte'))
    elif current_page == 'compte':
        return redirect(url_for('virement'))
    elif current_page == 'virement':
        return redirect(url_for('reception'))  # Retour à l'accueil

if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0', port=5002)
