import pandas as pd
import seaborn as sns

print("====================================================")
print(" EXPLORATORY DATA ANALYSIS (EDA) ON TITANIC DATASET ")
print("====================================================\n")

# 1. Load the dataset
df = sns.load_dataset('titanic')

# 2. Look at the basic structure
print("--- 1. DATASET SHAPE ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n--- 2. INITIAL MISSING VALUES ---")
print(df.isna().sum())

# 3. Fix missing values with structural logic
# Fill Age using the median of their passenger class and sex group
df['age'] = df['age'].fillna(df.groupby(['pclass', 'sex'])['age'].transform('median'))
# Fill Embarked with the most common port
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
# Drop the highly incomplete 'deck' column
df = df.drop(columns=['deck'])

print("\n--- 3. MISSING VALUES AFTER CLEANING ---")
print(df.isna().sum())

# 4. Check for duplicate rows
print(f"\n--- 4. DUPLICATE ROWS ---")
print(f"Number of duplicate rows: {df.duplicated().sum()}")

# 5. Group and Compare survival rates to answer our key questions
print("\n====================================================")
print("             SURVIVAL RATE ANALYSIS                 ")
print("====================================================")

print("\n--- Survival Rate by Sex ---")
print(df.groupby('sex')['survived'].mean().round(2))

print("\n--- Survival Rate by Ticket Class (Socioeconomic) ---")
print(df.groupby('pclass')['survived'].mean().round(2))

print("\n--- Survival Rate by Age Bands ---")
df['age_band'] = pd.cut(df['age'], bins=[0, 12, 19, 40, 60, 100], 
                        labels=["Child", "Teen", "Adult", "Middle-aged", "Senior"])
print(df.groupby('age_band', observed=True)['survived'].mean().round(2))
