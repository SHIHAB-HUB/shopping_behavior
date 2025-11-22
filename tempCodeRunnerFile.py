plt.figure(figsize=self.figure_size)
        
        plt.scatter(male_based_df["Item Purchased"],
                    male_based_df["Value"],
                    label="Male",
                    color="blue")
        
        plt.scatter(female_based_df["Item Purchased"],
                    female_based_df["Value"],
                    label="Female",
                    color="orange")
        
        plt.tight_layout()
        plt.legend()
        plt.show()