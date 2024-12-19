# Fraud Detection Analysis

By Jonas Elterich, Adam Karner, Jean Ryan-Lozon, Julian Kim

This project performs an analysis of credit card transaction data to detect fraudulent activities using machine learning techniques. It leverages various libraries such as pandas, sklearn, and SQLAlchemy, as well as a PostgreSQL database to store and manage the data.

## Table of Contents

1. [Installation](#installation)
2. [Dependencies](#dependencies)
3. [Project Structure](#project-structure)
4. [Database Configuration](#database-configuration)
5. [Data Loading](#data-loading)
6. [Data Processing](#data-processing)
7. [Visualizations](#visualizations)
8. [Model Development](#model-development)
9. [Running the Analysis](#running-the-analysis)
10. [Results](#results)
11. [License](#license)

---

## Installation

### Prerequisites:
Ensure that you have `Python 3.x` and the following libraries installed:

- pandas
- numpy
- matplotlib
- sqlalchemy
- kagglehub
- scikit-learn

You can install these dependencies using pip:

```bash
pip install pandas numpy matplotlib sqlalchemy kagglehub scikit-learn
```

### Database Setup:
This project requires a PostgreSQL database to store and manage the data. Make sure you have a running PostgreSQL instance and access to the database. The database should allow the creation of tables to store transaction data.

---

## Dependencies

The following libraries are required to run the analysis:

- `pandas` - For data manipulation and analysis.
- `numpy` - For numerical operations.
- `matplotlib` - For data visualization.
- `sqlalchemy` - For database connection and interaction.
- `kagglehub` - For downloading the Kaggle dataset.
- `scikit-learn` - For machine learning algorithms, preprocessing, and evaluation.

---

## Project Structure

The project contains the following components:

- **Data Loading and Database Management**: Functions to load datasets into PostgreSQL and manage database connections.
- **Data Processing**: Functions to preprocess and extract useful features from the transaction data.
- **Visualization**: Functions to create various plots for data analysis, including fraud distribution, time-based fraud patterns, and amount analysis.
- **Model Development**: Pipeline for building a machine learning model, including feature scaling and classification using logistic regression.
- **Evaluation**: Performance metrics (confusion matrix, classification report, and ROC AUC score) to assess the model.

---

## Database Configuration

The database connection is configured through a JSON file called `db_config.json`. This file should be structured as follows:

```json
{
    "user": "your_db_user",
    "password": "your_db_password",
    "host": "your_db_host",
    "port": "your_db_port",
    "database": "your_db_name"
}
```
Example JSON file: 

{"host": "localhost",
    "port": 5432,
    "database": "fraud_detection",
    "user": "postgres",
    "password": "password"}

Make sure to replace the values with your actual PostgreSQL credentials.

---

## Data Loading

The dataset used in this project is from Kaggle (available at [fraud-detection dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection)).

### Data Loading Functions:
- **`load_data_to_postgres()`**: This function downloads the dataset from Kaggle and loads it into PostgreSQL tables (`fraud_train` and `fraud_test`).
- **`load_fraud_data()`**: This function queries the PostgreSQL database to load only the necessary columns from the training and testing datasets.

---

## Data Processing

The dataset includes a `trans_date_trans_time` column that contains transaction timestamps. The **`extract_time_features()`** function extracts various time-based features from this timestamp, such as:
- Hour of the transaction
- Day, month, and day of the week
- Whether the transaction occurred on a weekend or during business hours

---

## Visualizations

Several visualizations are generated to understand the characteristics of fraudulent transactions:
1. **Fraud Distribution**: A bar chart showing the count of fraudulent vs. non-fraudulent transactions.
2. **Time-based Fraud Patterns**: A set of bar charts visualizing fraud patterns across different times of day, days of the week, and months.
3. **Transaction Amount Analysis**: A comparison of transaction amounts for fraudulent vs. non-fraudulent transactions using histograms and box plots.

---

## Model Development

The analysis uses logistic regression to classify transactions as fraudulent or non-fraudulent. The data is preprocessed using the `StandardScaler` to normalize numerical features. The model pipeline is created using scikit-learn's `Pipeline` class.

### Steps:
1. **Preprocessing**: The numeric features are scaled using `StandardScaler` for consistency.
2. **Logistic Regression**: A logistic regression model is used for classification.
3. **Model Evaluation**: The model is evaluated using a confusion matrix, classification report, and ROC AUC score.

---

## Running the Analysis

### Step 1: Load Data
Before running the analysis, ensure the data is loaded into PostgreSQL by executing the `load_data_to_postgres()` function. This step will download the Kaggle dataset and insert it into the database.

### Step 2: Data Processing
The `extract_time_features()` function will preprocess the dataset by adding useful time-based features.

### Step 3: Visualizations
Visualize the data using the provided plotting functions to get insights into fraud patterns and transaction amounts.

### Step 4: Train and Evaluate the Model
The logistic regression model will be trained on the training dataset and evaluated on the test dataset. The evaluation results (confusion matrix, classification report, and ROC AUC score) will be displayed.

---

## Results

The following results will be provided after executing the analysis:

- **Confusion Matrix**: To visualize the true positives, true negatives, false positives, and false negatives.
- **Classification Report**: Contains precision, recall, and F1-score for both classes (fraud and non-fraud).
- **ROC AUC Score**: Measures the model's ability to distinguish between the two classes.

---

## License

This project is licensed under the MIT License.

---

### Notes:
- Ensure that the PostgreSQL instance is running and accessible.
- Modify `db_config.json` to match your database credentials.
- The Kaggle dataset is required for this analysis; the script will download it automatically if needed.