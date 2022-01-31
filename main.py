from flask import Flask

import pickle

columns = ['Temperature', 'Revenue']
models = pickle.load(open('sale_.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return 'Previsão de lucro'

@app.route('/maquina_predict/<winnings>')
def acquisition(winnings):
    df_input = [float(winnings)]
    predictModel = models.predict([df_input])

    return f"previsao de lucro : {predictModel[0]}"

@app.errorhandler(Exception)
def all_exception_handler(error):
   return f'Error',  404


app.run(debug=True)
