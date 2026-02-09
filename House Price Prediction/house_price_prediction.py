import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv("train.csv")

# Select only required columns
data = data[["GrLivArea", "BedroomAbvGr", "SalePrice"]]

# Remove missing values
data = data.dropna()

# Split features and target
X = data[["GrLivArea", "BedroomAbvGr"]]
y = data["SalePrice"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
predictions = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Predict price for a new house
new_house = pd.DataFrame(
    [[1500, 3]],
    columns=["GrLivArea", "BedroomAbvGr"]
)

predicted_price = model.predict(new_house)
print(f"Predicted House Price: ₹{predicted_price[0]:,.2f}")
