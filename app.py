from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import os

app = Flask(__name__)

# Load model - update path to be relative to current file
model_path = os.path.join(os.path.dirname(__file__), 'car_model.pkl')
model = pickle.load(open(model_path, "rb"))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    Fuel_Type_Diesel=0
    
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Owner=int(request.form['Owner'])
        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        Year=2025-Year  # Updated to current year
        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0
        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
        prediction=model.predict(np.array([[Year, 
                                          Present_Price, 
                                          Kms_Driven,
                                          Owner, 
                                          Fuel_Type_Diesel, 
                                          Fuel_Type_Petrol, 
                                          Seller_Type_Individual, 
                                          Transmission_Mannual]]))
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You can sell the Car at {} lakhs".format(output))
    else:
        return render_template('index.html')

# Add this for Vercel
app.debug = True

if __name__=="__main__":
    app.run()