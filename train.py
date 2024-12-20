from flask import Flask, request, render_template
import joblib
import numpy as np

# Load the trained model
model = joblib.load('iris_model.pkl')

# Create Flask app
app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    try:
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
    except ValueError:
        return "Invalid input. Please enter numerical values only."

    # Prepare input for the model
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)
    species = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
    
    # Return the prediction
    return f"The predicted species is: {species[prediction[0]]}"

if __name__ == "__main__":
    app.run(debug=True)