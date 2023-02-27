from flask import Flask, render_template, jsonify

app = Flask(__name__)

TECHNIQUES = [
  {
    'id': 1,
    'title': 'KNN Imputation',
    'description': 'KNN Imputer based on k-Nearest neighbours algorithm.'
  },
  {
    'id': 2,
    'title': 'MissForest',
    'description': 'A Random Forest algorithm based model imputation approach.'
  },
]


@app.route("/")
def hello_jovian():
  return render_template('home.html', techniques=TECHNIQUES)


@app.route("/KNN")
def hello_KNN():
  return render_template('KNN.html')


@app.route("/api/techniques")
def list_techniques():
  return jsonify(TECHNIQUES)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
