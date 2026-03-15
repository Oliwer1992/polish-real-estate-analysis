# 🏢 Polish Real Estate Market Analysis: From Raw Data to Statistical Inference

## 📌 Project Overview
This project presents an end-to-end analytical pipeline for the Polish residential real estate market. The workflow covers the entire data lifecycle: from extracting and inspecting raw data (ETL) using SQL, through meticulous Data Cleaning and comprehensive Exploratory Data Analysis (EDA) in pandas, to advanced hypothesis testing and Econometric Modeling (Statistical Inference) to understand the underlying factors driving property prices.

## 📊 Dataset Information
The data used in this analysis comes from the **Apartment Prices in Poland** dataset available on Kaggle. It contains historical information about apartment rental prices, locations, and characteristics across 15  major Polish cities between August 2023 and June 2024.

* **Source:** https://www.kaggle.com/datasets/krzysztofjamroz/apartment-prices-in-poland 
  
## 🛠️ Tech Stack & Tools
* **Languages:** Python, SQL (SQLite3)
* **Data Manipulation:** `pandas`, `numpy`, `os`, `glob`
* **Data Visualization:** `matplotlib`, `seaborn` (custom `visualizer.py` module)
* **Statistics & Inference:** `scipy.stats` (Mann-Whitney U, Kruskal-Wallis),  `scikit-posthocs`  (Dunn's test), `statsmodels` (Ordinary Least Squares Regression, VIF)

---

## 📂 Project Architecture

The project is structured into 3 logical stages (Jupyter Notebooks), reflecting a professional Data Analytics workflow:

### 1️⃣ Phase 1: Database & Data Wrangling (SQL & Python)
*File: `01_Initial_SQL_Exploration.ipynb`*
* **ETL Pipeline:** Batch loading raw CSV files into an SQLite relational database using `os` and `glob`.
* **SQL Inspection & Standardization:** Dropping heavily corrupted columns and verifying the standardization of categorical data.
* **Feature Engineering:** Creating the core analytical metric: `price_per_m2`.
* **Business Logic & Outlier Flagging:** * Tracking ID duplicates (deliberately retained for time-series tracking in Phase 2).
  * Flagging suspiciously low and high-priced properties for detailed EDA.
  * Identifying logical anomalies (e.g., checking if the apartment floor is strictly lower than the total floors in the building).
* **Descriptive Statistics:** Aggregating min, max, average, and quartiles partitioned by city.

### 2️⃣ Phase 2: Data Cleaning & Complete EDA
*File: `02_Data_Cleaning_and_EDA.ipynb`*
* **Data Quality Checks:** Handling missing values (imputation) to ensure data integrity.
* **Anomaly Filtering:** Processing the previously flagged price outliers—dropping unrealistic entries (e.g., `price < 1000 PLN`, `price_per_m2 < 30 PLN`) while deliberately preserving the legitimate luxury market segment.
* **Correlation Analysis:** Investigating relationships between numerical features and pricing to select independent variables for modeling.
* **Time-Series Analysis:** Tracking the historical price changes of individual listings (utilizing the duplicated listing IDs) and observing the moving average price across different cities over time.

### 3️⃣ Phase 3: Statistical Inference & Regression Modeling
*File: `03_Statistical_Inference.ipynb`*
* **Hypothesis Testing (Non-parametric):**
  * *Mann-Whitney U test* to compare pricing distributions between block of flats and tenements (kamienica).
  * *Cluster Analysis:* Using *Kruskal-Wallis & Dunn's post-hoc tests* to analyze and validate statistically significant differences in both `price` and `price_per_m2` **within** as well as **between** the 3 distinct city clusters.
* **Statistical Multiple Linear Regression (Statsmodels):**
  * *Goal:* To understand feature significance and market relationships, rather than building a predictive ML model.
  * Feature selection and preprocessing categorical variables using One-Hot Encoding (OHE).
  * **Model Diagnostics:** Verifying Ordinary Least Squares (OLS) assumptions, including linearity, normality of residuals, homoscedasticity, independence of Errors and checking for multicollinearity using Variance Inflation Factor (VIF).
  * Analyzing OLS results, p-values, and coefficients.

---

## 💡 Key Business Insights (Model Findings)
Based on the final Statistical Regression model, the following market drivers were identified:
* **Property Size Impact:** Every additional square meter increases the total price by an average of **70.85 PLN**.
* **Location & Distance:** Proximity to the city center is crucial. Every kilometer away from the center decreases the property value by **141.16 PLN**.
* **City Premiums & Discounts:** Compared to the baseline (Warsaw), **Radom is the most affordable market** (offering a massive discount of 2593.51 PLN), whereas **Gdańsk** remains one of the most expensive alternatives (only 1115.84 PLN cheaper than Warsaw).
* **Building Type Valuation:** Apartment buildings command a premium of **594.23 PLN**, while classic tenements (kamienice) show a slight negative impact of **33.21 PLN** compared to standard blocks of flats.

---
## 🚀 How to Run (Local Setup)

To reproduce the analysis on your local machine, follow these steps:

**1. Clone the repository and navigate to the project directory:**
```bash
git clone https://github.com/Oliwer1992/polish-real-estate-analysis.git
cd polish-real-estate-analysis
```

**2. Set up a virtual environment (recommended):**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

**3. Install required dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the Jupyter Notebooks:**
Launch Jupyter Lab or Jupyter Notebook and execute the files in the following sequential order:
```bash
jupyter lab
```
* `01_Initial_SQL_Exploration.ipynb` (Constructs the SQLite database)
* `02_Data_Cleaning_and_EDA.ipynb` (Cleans data and generates visualizations)
* `03_Statistical_Inference.ipynb` (Runs statistical tests and OLS regression)

> **Note:** Ensure that the raw CSV data files are placed in the correct `data/` directory.