import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("C:\\Users\\Shihabul Islam\\Desktop\\book1.csv")
    
    blood_group = pd.DataFrame(df["blood group"].value_counts())
    
    blood_group.plot.pie(y="count",
                         autopct="%1.1f%%",
                         figsize=(10,8))
    
    plt.show()
    
    # print(blood_group)
    
    
    
if __name__ == "__main__":
    main()