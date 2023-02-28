from flask import Flask, render_template, jsonify

app = Flask(__name__)

TECHNIQUES = [
  {
    'id':
    1,
    'title':
    'KNN Imputation',
    'description':
    'KNN Imputer based on k-Nearest neighbours algorithm.',
    'url':
    'https://imputation-techniques.shashwat12304.repl.co/KNN',
    'code':
    'https://github.com/shashwat12304/Imputation-techniques',
    'mail':
    'mailto:shashwatsharma12304@gmail.com?subject=Doubt%20regarding%20KNN%20imputer&body=Name%20%3A%20%3Cyour%20name%3E%0D%0AGithub%20Link%3A%20%3Cyour%20repository%20link%3E%0D%0ADescription%3A%20%3CIssues%20to%20be%20removed%3E'
  },
  {
    'id':
    2,
    'title':
    'MissForest',
    'description':
    'A Random Forest algorithm based model imputation approach.',
    'url':
    'https://imputation-techniques.shashwat12304.repl.co/Missforest',
    'code':
    'https://github.com/shashwat12304/Imputation-techniques',
    'mail':
    'mailto:shashwatsharma12304@gmail.com?subject=Doubt%20regarding%20KNN%20imputer&body=Name%20%3A%20%3Cyour%20name%3E%0D%0AGithub%20Link%3A%20%3Cyour%20repository%20link%3E%0D%0ADescription%3A%20%3CIssues%20to%20be%20removed%3E'
  },
]


@app.route("/")
def hello_jovian():
  return render_template('home.html', techniques=TECHNIQUES)


@app.route("/KNN")
def hello_KNN():
  return render_template('KNN.html')


@app.route("/Missforest")
def hello_forest():
  return render_template('Missforest.html')


@app.route("/api/techniques")
def list_techniques():
  return jsonify(TECHNIQUES)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
