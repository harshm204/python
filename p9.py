import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SalesDataAnalyzer:

    def __init__(self):
        self.df=None
        self.plots={}

    def load_data(self):
        try:
            print("\n== Load Dataset ==")
            data_frame=input("Enter the path of the dataset (csv file): ").strip()
            self.df=pd.read_csv(data_frame)
            print("Dataset loaded Successfully!\n")
        except FileNotFoundError:
            print("\nError: File not found. Please check the file path.\n")

    def head(self):
        try:
            print("\nDisplay the first 5 row.\n")
            print(self.df.head(),"\n")
        except Exception as e:
            print("Error:", e)

    def tail(self):
        try:
            print("\nDisplay the last 5 row.\n")
            print(self.df.tail(),"\n")
        except Exception as e:
            print("Error:", e)

    def colume(self):
        try:
            print("\nColumes Name are :")
            print(self.df.columns,"\n")
        except Exception as e:
            print("Error:", e)

    def dtype(self):
        try:
            print("\nDataFrame DataTypes are:")
            print(self.df.dtypes,"\n")
        except Exception as e:
            print("Error:", e)

    def explore_data(self):
        try:
            print("\n")
            print(self.df.info(),"\n")
        except Exception as e:
            print("Error:", e)

    def sort_df(self):
        try:
            print("\nColumes Name are :")
            print(self.df.columns,"\n")
            od=input("Enter Sorting by Ascending or Descending (A or D): ").upper()
            col=input("Enter colume Name to sort: ").strip()
            if od=="A":
                a_sort=self.df.sort_values(by=col)
                print("\nSort by Asecending:")
                print(a_sort,"\n")
            elif od=="D":
                d_sort=self.df.sort_values(by=col, ascending=False)
                print("\nSort by Asecending:")
                print(d_sort,"\n")
            else:
                print("\nInvalided Choice..")
        except KeyError:
            print(f"This {col} is not a valid column name...")
        except Exception as e:
            print("Error:", e)

    def Filter(self):
        try:
            print("\nAvailable Columns:")
            print(self.df.columns)
            col = input("\nEnter column name to filter: ").strip()
            condition = input("Enter condition (>, <, ==): ")
            value = float(input("Enter value: "))
            if condition == ">":
                result = self.df[self.df[col] > value]
            elif condition == "<":
                result = self.df[self.df[col] < value]
            elif condition == "==":
                result = self.df[self.df[col] == value]
            else:
                print("Invalid condition")
                return
            print("\nFiltered DataFrame:")
            print(result)
        except KeyError:
            print(f"\n'{col}' is not a valid column name.")
        except Exception as e:
            print("Error:", e)

    def missing_value(self):
        try:
            print("\nRows with Missing Values:\n")
            missing_rows = self.df[self.df.isnull().any(axis=1)]
            if missing_rows.empty:
                print("No missing values found in the dataset!")
            else:
                print(missing_rows)
        except Exception as e:
            print("Error:", e)

    def missing_fill(self):
        try:
            print("\nFilling missing values with column mean...\n")
            if self.df.isnull().values.any():
                self.df.fillna(self.df.mean(numeric_only=True), inplace=True)
                print("Missing values filled with mean successfully!")
            else:
                print("No missing values found in the dataset!")
        except Exception as e:
            print("Error:", e)

    def Replace_missing_values(self):
        try:
            col = input("Enter column name: ").strip()
            value = input("Enter value to replace missing data: ")
            if col in self.df.columns:
                self.df[col].fillna(value, inplace=True)
                print(f"\nMissing values in '{col}' replaced with {value}")
            else:
                print("\nInvalid column name!")
        except Exception as e:
            print("Error:", e)

    def dropping_missing_value(self):
        try:
            print("\nDropping rows with missing values...\n")
            if self.df.isnull().values.any():
                self.df.dropna(inplace=True)
                print("Rows with missing values removed successfully!")
            else:
                print("No missing values found in the dataset!")
        except Exception as e:
            print("Error:", e)

    def  Descriptive_Statistics(self):
        try:
            print("\nDescriptive Statistics:\n")
            print(self.df.describe(),"\n")
        except Exception as e:
            print("Error:", e)

    def bar_plot(self):
        try:
            print("\n== Bar Plot ==")
            print("\nColumns:", self.df.columns)
            x = input("Enter column name for x-axis (category): ").strip()
            y = input("Enter column name for y-axis (numeric): ").strip()
            if x not in self.df.columns or y not in self.df.columns:
                print("\nInvalid column name.")
                return
            print("Generating Bar plot...")
            fig = plt.figure(figsize=(8,5))
            plt.bar(self.df[x], self.df[y], color="green")
            plt.title("Bar Plot")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.xticks(rotation=45)
            plt.tight_layout()
            self.plots["bar"] = fig 
            plt.show()
            print("Bar plot displayed successfully!")
        except Exception as e:
            print("Error:", e)

    def line_plot(self):
        try:
            print("\n== Line Plot ==")
            print("\nColumns:", self.df.columns)
            x = input("Enter x-axis column name: ").strip()
            y = input("Enter y-axis column name: ").strip()
            if x not in self.df.columns or y not in self.df.columns:
                print("\nInvalid column name.")
                return
            print("Generating line plot...")
            fig = plt.figure(figsize=(10,5))
            plt.plot(self.df[x], self.df[y], marker='o', color="blue")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("Line Plot")
            plt.xticks(rotation=45)
            plt.tight_layout()
            self.plots["line"] = fig
            plt.show()
            print("Line plot displayed successfully!")
        except Exception as e:
            print("Error:", e)

    def scatter_plot(self):
        try:
            print("\n== Scatter Plot ==")
            print("\nColumns:", self.df.columns)
            x = input("\nEnter x-axis column name: ").strip()
            y = input("Enter y-axis column name: ").strip()
            if x not in self.df.columns or y not in self.df.columns:
                print("\nInvalid column name.")
                return
            print("Generating scatter plot...")
            fig = plt.figure(figsize=(8,5))
            plt.scatter(self.df[x], self.df[y])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("Scatter Plot")
            self.plots["scatter"] = fig
            plt.show()
            print("Scatter plot displayed successfully!")
        except Exception as e:
            print("Error:", e)

    def pie_chart(self):
        try:
            print("\n== Pie Chart ==")
            print("\nColumns:", self.df.columns)
            col = input("Enter column name for categories: ").strip()
            val = input("Enter column name for values: ").strip()
            if col not in self.df.columns or val not in self.df.columns:
                print("\nInvalid column name.")
                return
            print("Generating pie chart...")
            data = self.df.groupby(col)[val].sum()
            fig = plt.figure(figsize=(7,7))
            plt.pie(data, labels=data.index, autopct='%1.1f%%')
            plt.title("Pie Chart")
            self.plots["pie"] = fig
            plt.show()
            print("Pie chart displayed successfully!")
        except Exception as e:
            print("Error:", e)

    def histogram(self):
        try:
            print("\n== Histogram ==")
            print("\nColumns:", self.df.columns)
            col = input("Enter numeric column name: ").strip()
            if col not in self.df.columns:
                print("\nInvalid column name.")
                return
            print("Generating histogram...")
            fig = plt.figure(figsize=(8,5))
            plt.hist(self.df[col], bins=20, color="purple", edgecolor="black")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.title("Histogram")
            fig = plt.figure(figsize=(8,5))
            plt.show()
            print("Histogram displayed successfully!")
        except Exception as e:
            print("Error:", e)

    def stack_plot(self):
        try:
            print("\n== Stack Plot ==")
            print("\nColumns:", self.df.columns)
            x = input("Enter x-axis column name: ").strip()
            y1 = input("Enter first numeric column: ").strip()
            y2 = input("Enter second numeric column: ").strip()
            if x not in self.df.columns or y1 not in self.df.columns or y2 not in self.df.columns:
                print("\nInvalid column name.")
                return
            print("Generating stack plot...")
            fig = plt.figure(figsize=(10,5))
            plt.stackplot(self.df[x], self.df[y1], self.df[y2],labels=[y1, y2])
            plt.legend()
            plt.xlabel(x)
            plt.ylabel("Values")
            plt.title("Stack Plot")
            self.plots["stack"] = fig
            plt.show()
            print("Stack plot displayed successfully!")
        except Exception as e:
            print("Error:", e)

    def save_plot(self):
        try:
            print("\n== Save Visualization ==")
            if not self.plots:
                print("No plots available to save!")
                return
            file_name = input("Enter file name (example: bar_plot.png): ").strip().lower()
            if "bar" in file_name and "bar" in self.plots:
                fig = self.plots["bar"]
            elif "line" in file_name and "line" in self.plots:
                fig = self.plots["line"]
            elif "scatter" in file_name and "scatter" in self.plots:
                fig = self.plots["scatter"]
            elif "pie" in file_name and "pie" in self.plots:
                fig = self.plots["pie"]
            elif "hist" in file_name and "hist" in self.plots:
                fig = self.plots["hist"]
            elif "stack" in file_name and "stack" in self.plots:
                fig = self.plots["stack"]
            else:
                print("Plot type not found. Use names like bar_plot.png or line_plot.png")
                return
            fig.savefig(file_name)
            print(f"Visualization saved as {file_name} successfully!")
        except Exception as e:
            print("Error saving visualization:", e)

    def __del__(self):
        pass

SDA=SalesDataAnalyzer()

while True:
    try:
        print("========= Data Analysis & Visualization Program =========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operation")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("="*60)
        choice=int(input("\nEnter your choice: "))

        if choice==1:
            SDA.load_data()
        elif choice==2:
            while True:
                print("\n== Explore Data ==")
                print("1. Display the first 5 rows")
                print("2. Display the last 5 rows")
                print("3. Display column name")
                print("4. Display data types")
                print("5. Display basic info")
                print("6. Go Back....")
                echoice=int(input("Enter your Choice: "))
                if echoice==1:
                    SDA.head()
                elif echoice==2:
                    SDA.tail()
                elif echoice==3:
                    SDA.colume()
                elif echoice==4:
                    SDA.dtype()
                elif echoice==5:
                    SDA.explore_data()
                elif echoice==6:
                    print("\nReturning to Main Menu....\n")
                    break
                else:
                    print("\nInvalided Choice\n")

        elif choice==3:
            while True:
                print("\n== DataFrame Operation ==")
                print("1. Sorting DataFrame")
                print("2. Filtering DataFrame")
                print("3. Go Back....")
                ochoice=int(input("Enter your choice: "))
                if ochoice==1:
                    SDA.sort_df()
                elif ochoice==2:
                    SDA.Filter()
                elif ochoice==3:
                    print("\nReturning to Main Menu....\n")
                    break
                else:
                    print("\nInvalided Choice\n")

        elif choice==4:
            while True :
                print("\n== Handle Missing Data ==")
                print("1. Display rows with missing values")
                print("2. Fill missing values with mean")
                print("3. Drop rows with missing values")
                print("4. Replace missing values with a specific value")
                print("5. Go Back...")
                hchoice=int(input("Enter your choice: "))
                if hchoice==1:
                    SDA.missing_value()
                elif hchoice==2:
                    SDA.missing_fill()
                elif hchoice==3:
                    SDA.dropping_missing_value()
                elif hchoice==4:
                    SDA.Replace_missing_values()
                elif hchoice==5:
                    print("\nReturning to Main Menu....\n")
                    break
                else:
                    print("\nInvalided Choice\n")

        elif choice==5:
            SDA.Descriptive_Statistics()
        elif choice==6:
            while True:
                print("\n== Data Visualization ==")
                print("1. Bar Plot")
                print("2. Line Plot")
                print("3. Scatter Plot")
                print("4. pie Chart")
                print("5. Histogram")
                print("6. Stack Plot")
                print("7. Go Back....")
                dchoice=int(input("Enter your Choice: "))
                if dchoice==1:
                    SDA.bar_plot()
                elif dchoice==2:
                    SDA.line_plot()
                elif dchoice==3:
                    SDA.scatter_plot()
                elif dchoice==4:
                    SDA.pie_chart()
                elif dchoice==5:
                    SDA.histogram()
                elif dchoice==6:
                    SDA.stack_plot()
                elif dchoice==7:
                    print("\nReturning to Main Menu....\n")
                    break
                else:
                    print("\nInvalided Choice\n")

        elif choice==7:
            SDA.save_plot()

        elif choice==8:
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalided Choice!\n")
    except Exception as e:
            print("Error:", e)