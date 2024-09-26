import pandas as pd

def display_dataset_details(df):
    print("Dataset Shape:", df.shape)
    print("Dataset Size:", df.size)
    print("Number of Missing Values:\n", df.isnull().sum())
    print("Dataset Columns:\n", df.columns)
    print("Dataset First Five Rows:\n", df.head())
    print("Dataset Summary Statistics:\n", df.describe())

def import_dataset(file_path):
    try:
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            return pd.read_excel(file_path)
        elif file_path.endswith('.json'):
            return pd.read_json(file_path)
        elif file_path.endswith('.txt'):
            return pd.read_csv(file_path, sep='\t')
        else:
            print("Unsupported file format.")
            return None
    except Exception as e:
        print("Error importing dataset:", str(e))
        return None
def export_dataset(df, file_path):
    try:
        if file_path.endswith('.csv'):
            df.to_csv(file_path, index=False)
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            df.to_excel(file_path, index=False)
        elif file_path.endswith('.json'):
            df.to_json(file_path, orient='records')
        elif file_path.endswith('.txt'):
            df.to_csv(file_path, sep='\t', index=False)
        else:
            print("Unsupported file format.")
    except Exception as e:
        print("Error exporting dataset:", str(e))

def main():
    file_path = input("Enter dataset file path: ")
    df = import_dataset(file_path)
    
    if df is not None:
        display_dataset_details(df)
        
        export_file_path = input("Enter export file path: ")
        export_dataset(df, export_file_path)
        
        print("Dataset exported successfully.")

if __name__ == "__main__":
    main()


