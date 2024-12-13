import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import kagglehub

def create_db_engine():
    """Create PostgreSQL database connection"""
    # Update these parameters with your PostgreSQL connection details
    db_params = {
        'host': 'localhost',
        'database': 'fraud_detection',
        'user': 'postgres',
        'password': 'flanel',
        'port': '5432'}
    
    engine = create_engine(
        f"postgresql://{db_params['user']}:{db_params['password']}@"
        f"{db_params['host']}:{db_params['port']}/{db_params['database']}"
    )
    return engine

def load_data_to_postgres():
    """Download data from Kaggle and load it into PostgreSQL"""
    # Download dataset
    path = kagglehub.dataset_download("kartik2112/fraud-detection")
    
    # Define file paths
    fraud_test_csv = r"C:\Users\AdamKarner\.cache\kagglehub\datasets\kartik2112\fraud-detection\versions\1\fraudTest.csv"
    fraud_train_csv = r"C:\Users\AdamKarner\.cache\kagglehub\datasets\kartik2112\fraud-detection\versions\1\fraudTrain.csv"
    
    # Read CSV files
    fraud_test_df = pd.read_csv(fraud_test_csv)
    fraud_train_df = pd.read_csv(fraud_train_csv)
    
    # Create database engine
    engine = create_db_engine()
    
    # Load dataframes to PostgreSQL
    fraud_train_df.to_sql('fraud_train', engine, if_exists='replace', index=False)
    fraud_test_df.to_sql('fraud_test', engine, if_exists='replace', index=False)
    
    print("Data successfully loaded to PostgreSQL!")

if __name__ == "__main__":
    load_data_to_postgres()