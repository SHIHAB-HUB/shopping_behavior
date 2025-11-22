import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

class Shoping_Behavior:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.figure_size = (18, 9)
        print("Dataframe initialization successful!!")   
        
    @staticmethod
    def __color_genarator(df):
        return plt.cm.viridis(np.linspace(0, 1, len(df)))
    
    def __gender_and_item_separator(self, gender, item):
        gender_df = self.df[self.df["Gender"] == gender]
        gender_and_item_df = pd.DataFrame(gender_df[item].value_counts())
        gender_and_item_df = gender_and_item_df.rename(columns={"count": "Value"})
        gender_and_item_df = gender_and_item_df.reset_index()
        return gender_and_item_df
    
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
                           figsize = self.figure_size,
                           textprops={'fontsize': 14})
        
        plt.title("Customer analysis with Gender", size=20)
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
                                 figsize = self.figure_size,
                                 textprops={'fontsize': 14})

        plt.title("Customer analysis with age", fontsize=20)
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
        
        colour = self.__color_genarator(items_df)
        
        # Creating bar chart
        plt.figure(figsize=self.figure_size)
        
        plt.barh(items_df["Item Purchased"],
                 items_df["Value"],
                 color=colour)
        
        for index, value in enumerate(items_df["Value"]):
            plt.text(value, index, f"{value}", va="center")
        
        plt.xticks(np.arange(0, items_df["Value"].max() + 10 ,10))
        
        plt.xlabel("Purchased Amount", fontsize = 14)
        plt.ylabel("Name of Items", fontsize = 14)
        plt.title("Customer analysis with Item Purchased", size=20)
        plt.tight_layout()
        plt.show()

    # ================================
    # Catagory separation
    # ================================
    def category(self):
        category_df = pd.DataFrame(self.df["Category"].value_counts())
        category_df = category_df.rename(columns={"count": "Value"})
        category_df = category_df.reset_index()
        
        category_df.plot.pie(y="Value",
                             labels=category_df["Category"],
                             autopct="%1.1f%%",
                             shadow=True,
                             figsize=self.figure_size,
                             textprops={"fontsize": 14})
        
        plt.title("Shopping analysis with Category", fontsize=20)
        plt.tight_layout()
        plt.show()

    # ================================
    # Purchase Amount Analysis
    # ================================
    def purchase_amount(self):
        
        # Creating Histogram
        plt.figure(figsize=self.figure_size)
        plt.hist(self.df["Purchase Amount (USD)"],
                 bins=25,
                 edgecolor="#002358",
                 color="#458ffd")
        
        plt.xlabel("Purchase Amount (USD)", fontsize=14)
        plt.ylabel("Count", fontsize=14)
        plt.title("Shopping analysis by Purchase Amount (USD)", fontsize=20)
        plt.tight_layout()
        plt.show()

    def color_analysis(self):
        # color DataFrame
        color_df = pd.DataFrame(self.df["Color"].value_counts())
        color_df = color_df.rename(columns={"count": "Value"})
        color_df = color_df.reset_index()
        
        colors = self.__color_genarator(color_df)
        
        # Plotting the Horizontal Bar Chart
        plt.figure(figsize=self.figure_size)
        
        plt.barh(color_df["Color"],
                 color_df["Value"],
                 color=colors)
        
        for index, value in enumerate(color_df["Value"]):
            plt.text(value, index, f"{value}", va="center")
        
        plt.xlabel("Value", fontsize=14)
        plt.ylabel("Colors", fontsize=14)
        plt.title("Shopping analysis with colors", fontsize=20)
        plt.tight_layout()
        plt.show()
    
    def payment_method(self):
        # Payment Methods DataFrame
        payment_method_df = pd.DataFrame(self.df["Payment Method"].value_counts())
        payment_method_df = payment_method_df.rename(columns={"count": "Value"})
        payment_method_df = payment_method_df.reset_index()
        
        # Plotting the Pie Chart
        payment_method_df.plot.pie(y="Value",
                                   labels= payment_method_df["Payment Method"],
                                   autopct= "%1.1f%%",
                                   shadow= True,
                                   figsize=self.figure_size,
                                   textprops={"fontsize": 14})

        plt.title("Shopping analysis with Payment Methods", fontsize=20)
        plt.tight_layout()
        plt.show()
        
        
    def frequency_purchases(self):
        # Frequency of Purchases DataFrame
        frequency_purchases_df = pd.DataFrame(self.df["Frequency of Purchases"].value_counts())
        frequency_purchases_df = frequency_purchases_df.rename(columns={"count": "Value"})
        frequency_purchases_df = frequency_purchases_df.reset_index()
        
        colors = self.__color_genarator(frequency_purchases_df)
        
        # Plotting bar char for Frequency of Purchases
        plt.figure(figsize=self.figure_size)
        
        plt.bar(frequency_purchases_df["Frequency of Purchases"],
                frequency_purchases_df["Value"],
                color=colors)
        
        plt.xlabel("Frequency of Purchases", fontsize=14)
        plt.ylabel("Value", fontsize=14)
        plt.title("Shopping analysis with Frequency of Purchases", fontsize=20)
        plt.tight_layout()
        plt.show()
    
    def gender_based_purchase(self):
        male_based_df = self.__gender_and_item_separator(gender="Male", item="Item Purchased")
        female_based_df = self.__gender_and_item_separator(gender="Female", item="Item Purchased")
        
        plt.figure(figsize=self.figure_size)
        
        plt.scatter(male_based_df["Item Purchased"],
                    male_based_df["Value"],
                    label="Male",
                    color="skyblue",
                    alpha=0.8,
                    s=100)
        
        plt.scatter(female_based_df["Item Purchased"],
                    female_based_df["Value"],
                    label="Female",
                    color="orange",
                    alpha=0.8,
                    s=100)
        
        plt.xlabel("Item Purchased", fontsize=14)
        plt.ylabel("Values", fontsize=14)
        plt.title("Gender and Item Purchased Comparison", fontsize=20)
        plt.tight_layout()
        plt.legend()
        plt.show()
        
    def gender_based_category(self):
        male_based_df = self.__gender_and_item_separator(gender="Male", item="Category")
        female_based_df = self.__gender_and_item_separator(gender="Female", item="Category")
        
        plt.figure(figsize=self.figure_size)
        
        plt.scatter(male_based_df["Category"],
                    male_based_df["Value"],
                    label="Male",
                    color="skyblue",
                    alpha=0.8,
                    s=100)
        
        plt.scatter(female_based_df["Category"],
                    female_based_df["Value"],
                    label="Female",
                    color="orange",
                    alpha=0.8,
                    s=100)
        
        plt.xlabel("Category", fontsize=14)
        plt.ylabel("Values", fontsize=14)
        plt.title("Gender and Category Comparison", fontsize=20)
        plt.tight_layout()
        plt.legend()
        plt.show()
    
    def spending_pattern(self):
        pass
    
    def age_purchase_behavior(self):
        pass
    
    
def main():
    csv_file_path = "deta_set/shopping_behavior.csv"
    analyze = Shoping_Behavior(csv_file_path)
    
    while True:
        print("=====================================")
        print("=====     Shopping Behavior     =====")
        print("=====================================")
        print("1. Gender Analysis")
        print("2. Age Analysis")
        print("3. Item Analysis")
        print("4. Category Analysis")
        print("5. Purchase Amount analysis")
        print("6. Color Analysis")
        print("7. Payment Method Analysis")
        print("8. Frequency of Purchases analysis")
        print("9. Gender and Item purchase comparison")
        print("10.  Gender and Category comparison")
        print("Exit\n")

        
        option = input("Select an option: ").lower()
        print("\n")
        
        match (option):
            case "1":
                analyze.gender_count()
            case "2":
                analyze.age_separation()
            case "3":
                analyze.item_list()
            case "4":
                analyze.category()
            case "5":
                analyze.purchase_amount()
            case "6":
                analyze.color_analysis()
            case "7":
                analyze.payment_method()
            case "8":
                analyze.frequency_purchases()
            case "9":
                analyze.gender_based_purchase()
            case "10":
                analyze.gender_based_category()
            case "exit":
                sys.exit()
            case _:
                print("Enter a wrong option!!\n")
        
  
if __name__ == "__main__":
    main()
    
    