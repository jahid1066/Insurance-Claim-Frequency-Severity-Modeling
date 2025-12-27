# Insurance Claims Modeling Project

This project focuses on modeling insurance claims using **Generalized Linear Models (GLM)** for **claim frequency** and **claim severity**. The goal is to predict the expected claim cost (**pure premium**) for insurance policies.

The project follows a **modular, reproducible, and industry-aligned structure**, commonly used in actuarial science, insurance analytics, and data science roles.

---

## Dataset

The dataset contains the following key variables:

- **IDpol**: Policy ID  
- **ClaimNb**: Number of claims filed (frequency)  
- **Exposure**: Policy exposure in years  
- **VehPower**: Vehicle power  
- **VehAge**: Vehicle age  
- **DrivAge**: Driver age  
- **BonusMalus**: Bonus–malus score  
- **Density**: Population density of region  
- **ClaimAmount**: Claim amount (severity)  
- **PurePremium**: Calculated as Frequency × Severity  
- **Categorical features**: Region indicators (Region[T.Rxx]), Vehicle brand, fuel type, etc.

---

## Methodology

### Exploratory Data Analysis (EDA)

- Analyzed distribution of claim frequency and severity  
- Examined relationships between risk factors and claims  
- Handled missing values and encoded categorical features  

---

### Frequency Model (Poisson GLM)

- **Target**: ClaimNb  
- **Features**: VehPower, VehAge, DrivAge, BonusMalus, Density  
- **Offset**: log(Exposure)  

**Performance Metrics**
- MSE: 0.0412  
- RMSE: 0.2030  
- R²: 0.0197  

---

- **Target**: ClaimAmount (policies with ClaimNb > 0)  
- **Features**: VehPower, VehAge, DrivAge, BonusMalus, Density  

**Performance Metrics**
- MSE: 66,295,705  
- RMSE: 8,142  
- R²: 0.00064  

---

### Pure Premium Calculation

- **Pure Premium = Predicted Frequency × Predicted Severity**
- Represents the expected annual claim cost per policy  

---

### Model Validation

- Evaluation using **MSE, RMSE, and R²**
- Comparison of predicted vs observed values  

---

## Installation

Clone the repository:

git clone https://github.com/jahid1066/Insurance-Claim-Frequency-Severity-Modeling.git

cd Insurance-Claim-Frequency-Severity-Modeling

jupyter notebook


## **Usage**

- Place the dataset in Data/raw/insurance_claims.csv

- Run data_exploration.ipynb for exploratory analysis

- Train models using:

- frequency_models.ipynb

- severity_models.ipynb

- Validate models and compute pure premiums using model_validation.ipynb

## **Skills Demonstrated**

- Insurance analytics and actuarial modeling
- Claim frequency and severity modeling
- Generalized Linear Models (Poisson & Gamma)
- Statistical evaluation (MSE, RMSE, R²)
- Data preprocessing and feature engineering
- Reproducible, modular Python project structure

---

## **Author**

Md Jahidul Islam

---

## **License**

This project is for **educational and portfolio purposes**.
