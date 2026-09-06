import pandas as pd
 
class StudentAnalyzer:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        print(" Data loaded!")


    def show_summary(self):
        print("Student Report:")
        print("="*40)
        print(f"Total students: {len(self.df)}")
        print(f"Average marks: {self.df["Marks"].mean():.2f}")
        print(f"Highest Marks: {self.df["Marks"].max()}")
        print(f"Lowest Marks: {self.df["Marks"].min()}")
    def get_toppers(self, n =3):
        return self.df.sort_values("Marks", ascending=False).head(n)
    def city_wise_report(self):
        return self.df.groupby("City")["Marks"].mean().round(2)
    def save_report(self, filename="report.csv"):
        self.df.to_csv(filename,index=False)
        print(f"Report saved to {filename}")
analyzer= StudentAnalyzer("students.csv")
analyzer.show_summary()
print("\n Top 3 students: ")
print(analyzer.get_toppers(3))
print("\n City wise Report:")
print(analyzer.city_wise_report())
analyzer.save_report("final_report.csv")
