# House Price Prediction using Linear Regression

This project implements a simple machine learning model to predict house prices
based on key features such as living area and number of bedrooms.
The model is built using Python and Scikit-learn.

---

## 📌 Objective
To develop a Linear Regression model that predicts house prices using historical
housing data and evaluates the model using Mean Squared Error (MSE).

---

## 📂 Dataset
- Source: Kaggle (House Prices Dataset)
- File used: `train.csv`
- Features selected:
  - GrLivArea (Above ground living area in square feet)
  - BedroomAbvGr (Number of bedrooms above ground)
- Target variable:
  - SalePrice

---

## 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn

---

## ⚙️ Steps Performed
1. Loaded the dataset using Pandas
2. Selected relevant features and target variable
3. Removed missing values
4. Split the data into training and testing sets
5. Trained a Linear Regression model
6. Evaluated the model using Mean Squared Error (MSE)
7. Predicted the price of a new house

---

## ▶️ How to Run the Project
1. Clone or download the repository
2. Install required dependencies:
   ```bash
   pip install pandas scikit-learn
