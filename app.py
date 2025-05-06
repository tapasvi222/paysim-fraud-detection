import flask
from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except Exception as e:
    print("Error loading model:", str(e))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get data from the form submission
        form_data = request.form.to_dict()  # Convert ImmutableMultiDict to regular dict
        print("Form Data Received:", form_data)
        step = request.form.get('step')
        amount = request.form.get('amount')
        oldbalanceOrg = request.form.get('oldbalanceOrg')
        newbalanceOrig = request.form.get('newbalanceOrig')
        oldbalanceDest = request.form.get('oldbalanceDest')
        newbalanceDest = request.form.get('newbalanceDest')
        isFlaggedFraud = request.form.get('isFlaggedFraud')
        transactionType = request.form.get('transactionType')
        # Retrieve form data from the request object
        step = float(request.form.get('step'))
        amount = float(request.form.get('amount'))
        oldbalanceOrg = float(request.form.get('oldbalanceOrg'))
        newbalanceOrig = float(request.form.get('newbalanceOrig'))
        oldbalanceDest = float(request.form.get('oldbalanceDest'))
        newbalanceDest = float(request.form.get('newbalanceDest'))
        isFlaggedFraud = int(request.form.get('isFlaggedFraud'))
        transactionType = request.form.get('transactionType')

        # One-hot encode the transaction type
        type_CASH_IN = 1 if transactionType == 'CASH_IN' else 0
        type_CASH_OUT = 1 if transactionType == 'CASH_OUT' else 0
        type_DEBIT = 1 if transactionType == 'DEBIT' else 0
        type_PAYMENT = 1 if transactionType == 'PAYMENT' else 0
        type_TRANSFER = 1 if transactionType == 'TRANSFER' else 0
        xtrain_columns = ['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 
                  'newbalanceDest', 'isFlaggedFraud', 'type_CASH_IN', 'type_CASH_OUT', 
                  'type_DEBIT', 'type_PAYMENT', 'type_TRANSFER']

            # Prepare the input feature vector (model expects it to be a list)
        features = [
                step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, 
                newbalanceDest, isFlaggedFraud, type_CASH_IN, type_CASH_OUT, 
                type_DEBIT, type_PAYMENT, type_TRANSFER
            ]
        features_df = pd.DataFrame([features], columns=xtrain_columns)
        print(features_df)
        prediction = model.predict(features_df)
        prediction_result = prediction[0]      

    return f'''

                    <h2><strong>Fraud Detection:</strong> { prediction_result}</h2>
        '''
    

if __name__ == "__main__":
    app.run(debug=True)


