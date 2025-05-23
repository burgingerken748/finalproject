import pandas as pd

def main():
    # Load and display data from CSV file
    df = pd.read_csv("data.csv")
    print(df)

if __name__ == "__main__":
    main()
