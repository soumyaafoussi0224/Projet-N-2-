from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(debug=True)