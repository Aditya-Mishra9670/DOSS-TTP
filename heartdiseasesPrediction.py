import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample data creation (Replace this with your actual dataset)
data = {
    'Age': [29, 45, 53, 35, 61, 40, 52, 37, 45, 50],
    'Cholesterol': [200, 240, 220, 180, 250, 210, 230, 190, 240, 260],
    'BloodPressure': [120, 140, 130, 110, 150, 125, 135, 115, 140, 145],
    'ExerciseInducedAngina': [0, 1, 0, 1, 1, 0, 1, 0, 1, 1],  # 0 = No, 1 = Yes
    'HeartDiseaseRisk': [0, 1, 1, 0, 1, 0, 1, 0, 1, 1]  # 0 = Low Risk, 1 = High Risk
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and target variable
X = df[['Age', 'Cholesterol', 'BloodPressure', 'ExerciseInducedAngina']]
y = df['HeartDiseaseRisk']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Convert predictions to binary outcome (0 or 1)
y_pred_binary = [1 if p >= 0.5 else 0 for p in y_pred]

# Evaluate the model
mse = mean_squared_error(y_test, y_pred_binary)
print(f"Mean Squared Error: {mse}")

# Example prediction
example_data = pd.DataFrame({'Age': [50], 'Cholesterol': [230], 'BloodPressure': [140], 'ExerciseInducedAngina': [1]})
predicted_risk = model.predict(example_data)
predicted_risk_binary = [1 if p >= 0.5 else 0 for p in predicted_risk]
print(f"Predicted Heart Disease Risk for the example data: {'High Risk' if predicted_risk_binary[0] == 1 else 'Low Risk'}")
