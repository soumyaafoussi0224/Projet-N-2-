from flask import Flask, request, render_template_string

app = Flask(__name__)

# Fonction pour calculer le factoriel
def calculer_factoriel(x):
    F = 1
    for i in range(1, x + 1):
        F *= i
    return F

# Page d'accueil avec formulaire
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST':
        nombre_str = request.form.get('nombre')

        if not nombre_str:
            result = "Erreur : Veuillez entrer un nombre."
        else:
            try:
                nombre = int(nombre_str)
                if nombre < 0:
                    result = "Erreur : Veuillez entrer un nombre positif."
                else:
                    result = f"Le factoriel de {nombre} est : {calculer_factoriel(nombre)}"
            except ValueError:
                result = "Erreur : Veuillez entrer un nombre entier valide."

    return render_template_string('''
        <h1>Bienvenue sur l'application de calcul du factoriel</h1>
        <form method="post">
            <label for="nombre">Entrez un nombre :</label>
            <input type="text" id="nombre" name="nombre">
            <button type="submit">Calculer</button>
        </form>
        {% if result %}
            <h2>{{ result }}</h2>
        {% endif %}
    ''', result=result)

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(debug=True)