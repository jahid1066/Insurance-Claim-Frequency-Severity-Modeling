# Insurance Claims Modeling Project

This project focuses on modeling insurance claims using **Generalized Linear Models (GLM)** for frequency and severity. The aim is to predict the number of claims (frequency) and the claim amount (severity) to calculate the **pure premium** for insurance policies. The project is designed for reproducibility, modularity, and clear demonstration of data analysis and machine learning techniques applied to insurance datasets.


## **Dataset**

The dataset contains the following columns:

- `IDpol`: Policy ID  
- `ClaimNb`: Number of claims filed  
- `Exposure`: Policy exposure in years  
- `VehPower`: Vehicle power (horsepower)  
- `VehAge`: Vehicle age  
- `DrivAge`: Driver age  
- `BonusMalus`: Bonus-malus score  
- `Density`: Population density in the region  
- `ClaimAmount`: Claim amount (severity)  
- `PurePremium`: Calculated as `Frequency * Severity`  
- Region and vehicle categorical features (`Region[T.Rxx]`, `VehBrand`, etc.)


## **Methodology**

1. **Exploratory Data Analysis (EDA)**  
   - Analyzed distribution of claims and claim amounts  
   - Studied relationships between features and claims  
   - Handled missing values and performed feature encoding

2. **Frequency Model (Poisson GLM)**  
   - Target: `ClaimNb`  
   - Features: `VehPower`, `VehAge`, `DrivAge`, `BonusMalus`, `Density`  
   - Offset: `log(Exposure)`  
   - Performance:
     ```
     MSE: 0.0412
     RMSE: 0.2030
     R2: 0.0197
     ```

3. **Severity Model (Gamma GLM)**  
   * Target: `ClaimAmount` (only policies with claims > 0)  
   * Features: `VehPower`, `VehAge`, `DrivAge`, `BonusMalus`, `Density`  
   * Performance:
     ```
     MSE: 66,295,705
     RMSE: 8,142
     R2: 0.00064
     ```

4. **Pure Premium Calculation**  
   - Predicted claim frequency × predicted severity  
   - Used as the expected claim amount per policy  

5. **Validation**  
   - Metrics: MSE, RMSE, R²  
   - Predictions compared with observed data  


## **Installation**

1. Clone the repository:

```bash
 https://github.com/jahid1066/Insurance-Claim-Frequency-Severity-Modeling.git
cd Insurance-Claim-Frequency-Severity-Modeling

2. Install required packages:

pip install -r requirements.txt

3. Launch Jupyter notebooks:

jupyter notebook


## **Usage**

1. Place your dataset in data/raw/insurance_claims.csv

2. Run 01_data_exploration.ipynb to explore and visualize the data

3. Fit frequency and severity models using 02_frequency_model.ipynb and 03_severity_model.ipynb

4. Validate models and calculate predicted pure premiums using 04_model_validation.ipynb


## **Skills Demonstrated**

* Data preprocessing and feature engineering

* Exploratory data analysis and visualization

* Generalized Linear Models (Poisson and Gamma)

* Model evaluation using MSE, RMSE, R²

* Insurance analytics (claim frequency and severity modeling)

* Modular Python project structure


## **Authors**

Md Jahidul Islam

## **License**

This project is for educational and portfolio purposes.
