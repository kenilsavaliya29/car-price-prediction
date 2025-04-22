# Car Price Prediction

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![Flask](https://img.shields.io/badge/Flask-3.x-green.svg) ![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.x-orange.svg)

A machine learning web application that predicts car prices based on various features using Random Forest Regression.

## Features

- Real-time car price prediction
- Modern, responsive UI with Bootstrap 5
- Machine Learning model trained on car sales data
- Easy-to-use web interface

## Tech Stack

- **Backend**: Flask
- **Frontend**: Bootstrap 5, HTML/CSS
- **ML**: scikit-learn (RandomForestRegressor)
- **Data Processing**: pandas, numpy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kenilsavaliya29/car-price-prediction.git
cd car-price-prediction
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open http://localhost:5000 in your browser

## Model Features

The prediction model takes into account:
- Year of manufacture
- Present price (in lakhs)
- Kilometers driven
- Number of previous owners
- Fuel type (Petrol/Diesel/CNG)
- Seller type (Dealer/Individual)
- Transmission (Manual/Automatic)

## Deployment

The application is configured for deployment on Vercel.

## Author

- Kenil Savaliya
- GitHub: [@kenilsavaliya29](https://github.com/kenilsavaliya29)

## License

This project is licensed under the MIT License.
