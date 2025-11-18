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
        
        # Filtering and Creating DataFrame 
        gender_df = pd.DataFrame(self.df["Gender"].value_counts())
        gender_df = gender_df.rename(columns={'count': 'Value'})
        gender_df = gender_df.reset_index()
        
        # Creating Pie chart
        gender_df.plot.pie(y="Value",
                           labels = gender_df["Gender"],
                           autopct="%1.1f%%",
                           startangle=145,
                           shadow=True,
                           figsize = (10,8),
                           textprops={'fontsize': 14})
        
        plt.title("Customer anlysis with Gender", size=20)
        plt.tight_layout()
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
        
        
        # Creating DataFrame 
        age_df = pd.DataFrame({"Category": ["Child (0-17)", "Young Adult (18-24)", "Adult (25-60)", "Senior Citizen (>60)"],
                                "Value": [child, young_adult, adult, senior_citizen]})
        
        filtered_age_df = age_df[age_df["Value"] != 0]

        # Pie chart
        filtered_age_df.plot.pie(y="Value",
                                 labels = filtered_age_df["Category"],
                                 autopct="%1.1f%%",
                                 shadow=True,
                                 figsize = (10,8),
                                 textprops={'fontsize': 14})

        plt.title("Customer anlysis with age", fontsize=20)
        plt.tight_layout()
        plt.show()

    # ================================
    # DataFrame with Items
    # ================================
    def item_list(self):
        # Creating DataFrame and cleaning
        items_df = pd.DataFrame(self.df["Item Purchased"].value_counts())
        items_df = items_df.rename(columns={"count": "Value"})
        items_df = items_df.reset_index()
        
        colour = plt.cm.viridis(np.linspace(0, 1, len(items_df)))
        
        # Creating bar chart
        plt.figure(figsize=(10,8))
        
        plt.barh(items_df["Item Purchased"],
                 items_df["Value"],
                 color=colour)
        
        for index, value in enumerate(items_df["Value"]):
            plt.text(value, index, f"{value}", va="center")
        
        plt.xticks(np.arange(0, items_df["Value"].max() + 10 ,10))
        
        plt.xlabel("Purchased Amount", fontsize = 14)
        plt.ylabel("Name of Items", fontsize = 14)
        plt.title("Customer anlysis with Item Purchased", size=20)
        plt.tight_layout()
        plt.show()

    # ================================
    # Catagory separation
    # ================================
    def category(self):
        category_df = pd.DataFrame(self.df["Category"].value_counts())
        category_df = category_df.rename(columns={"count": "Value"})
        category_df = category_df.reset_index()
        
        # print(category_df)
        
        category_df.plot.pie(y="Value",
                             labels=category_df["Category"],
                             autopct="%1.1f%%",
                             shadow=True,
                             figsize=(10,8),
                             textprops={"fontsize": 14})
        
        plt.title("Shopping anlysis with Category", fontsize=20)
        plt.tight_layout()
        plt.show()

    def purchase_amount(self):
        
        # Creating Histogram
        plt.figure(figsize=(10,8))
        plt.hist(self.df["Purchase Amount (USD)"],
                 bins=25,
                 edgecolor="#002358",
                 color="#458ffd")
        
        
        plt.xlabel("Purchase Amount (USD)", fontsize=14)
        plt.ylabel("Count", fontsize=14)
        plt.title("Shopping anlysis by Purchase Amount (USD)", fontsize=20)
        plt.tight_layout()
        plt.show()


def main():
    csv_file_path = "deta_set/shopping_behavior.csv"
    analize = Shoping_Behavior(csv_file_path)
    
    while True:
        print("=====================================")
        print("=====     Shopping Behavior     =====")
        print("=====================================")
        print("1. Gender Analysis")
        print("2. Age Analysis")
        print("3. Item Analysis")
        print("4. Category Analysis")
        print("5. Purchase Amount analysis")
        print("Exit\n")

        
        option = input("Select an option: ").lower()
        print("\n")
        
        match (option):
            case "1":
                analize.gender_count()
            case "2":
                analize.age_separation()
            case "3":
                analize.item_list()
            case "4":
                analize.category()
            case "5":
                analize.purchase_amount()
            case "exit":
                sys.exit()
            case _:
                print("Enter a wrong option!!\n")
        
  


if __name__ == "__main__":
    main()
    
    