import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('data.csv')

# Selecting only the relevant columns
X = df[['Years_of_Experience']]  # Features - double brackets for DataFrame format
y = df['Salary']  # Target

# Creating the linear regression model
model = LinearRegression()
model.fit(X, y)  # Training the model

# Making predictions for the existing data (for plotting)
y_pred = model.predict(X)

# Function to predict salary based on years of experience
def predict_salary(years_of_experience):
    # Create a DataFrame for the new data with the same feature name as used during training
    new_data = pd.DataFrame({'Years_of_Experience': [years_of_experience]})
    prediction = model.predict(new_data)
    return prediction[0]

# Plotting the results
plt.scatter(X, y, color='blue', label='Actual Salary')
plt.plot(X, y_pred, color='red', label='Predicted Salary Line')
plt.title('Years of Experience vs Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()

# Displaying the coefficient and intercept
print(f"Coefficient (Slope): {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")

# Example usage of the prediction function
years_exp_input = 15  # Example: 7 years of experience
predicted_salary = predict_salary(years_exp_input)
print(f"Predicted salary for {years_exp_input} years of experience: ${predicted_salary:.2f}")
