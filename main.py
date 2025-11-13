import matplotlib as plt
import numpy as np
import pandas as pd

def main():
    csv_file_path = "deta_set/shopping_behavior.csv"
    df = pd.read_csv(csv_file_path)
    
    
    print(df.head(10))


if __name__ == "__main__":
    main()
    
    