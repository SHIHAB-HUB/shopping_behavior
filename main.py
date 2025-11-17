import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

class Shoping_Behavior:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        print("Dataframe initialization successful!!")   
        
    # ================================
    # Gender count
    # ================================
    def gender_count(self):
        
        gender_df = pd.DataFrame(self.df["Gender"].value_counts())
        gender_df = gender_df.rename(columns={'count': 'Value'})
        gender_df = gender_df.reset_index()
        
        gender_df.plot.pie(y="Value",
                           labels = gender_df["Gender"],
                           autopct="%1.1f%%",
                           startangle=145,
                           shadow=True,
                           figsize = (10,8),
                           textprops={'fontsize': 14})
        
        plt.title("Customer anlysis with Gender", size=20)
        plt.show()
        

    # ================================
    # Age separation 
    # ================================
    def age_separation(self):
        # Filtering 
        child = len(self.df[self.df["Age"]<18])
        young_adult = len(self.df[(self.df["Age"]>=18) & (self.df["Age"]<25)])
        adult = len(self.df[(self.df["Age"]>=25) & (self.df["Age"]<60)])
        senior_citizen = len(self.df[(self.df["Age"]>=60)])
        
        age_df = pd.DataFrame({"Category": ["Child (0-17)", "Young Adult (18-24)", "Adult (25-60)", "Senior Citizen (>60)"],
                                "Value": [child, young_adult, adult, senior_citizen]})
        
        filtered_age_df = age_df[age_df["Value"] != 0]

        filtered_age_df.plot.pie(y="Value",
                                 labels = filtered_age_df["Category"],
                                 autopct="%1.1f%%",
                                 shadow=True,
                                 figsize = (10,8),
                                 textprops={'fontsize': 14})

        plt.title("Customer anlysis with age", fontsize=20)
        plt.show()

    # ================================
    # DataFrame with Items
    # ================================
    def item_lsit(self):
        pass

    # ================================
    # Catagory separation
    # ================================
    def Category(self):
        pass



def main():
    csv_file_path = "deta_set/shopping_behavior.csv"
    analize = Shoping_Behavior(csv_file_path)
    
    while True:
        print("=====================================")
        print("=====     Shopping Behavior     =====")
        print("=====================================")
        print("1. Gender Analysis")
        print("2. Age Analysis")
        print("Exit\n")

        
        option = input("Select an option: ").lower()
        
        if option == "1": 
            analize.gender_count()
            
        elif option == "2":
            analize.age_separation()
        elif option == "exit":
            sys.exit()
        else:
            print("Enter a wrong option!!\n")
    


if __name__ == "__main__":
    main()
    
    