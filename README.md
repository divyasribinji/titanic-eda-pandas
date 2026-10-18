# Exploratory Data Analysis (EDA) on Titanic Dataset

A comprehensive data analysis project using **Python** and **Pandas** to clean, analyze, and discover statistical survival insights from the classic Titanic passenger manifest.

## 📊 Project Overview
This repository satisfies the requirements for **Project 01: Exploratory Data Analysis (EDA)**. The core goal is to clean missing demographic variables, run descriptive operations, and answer targeted statistical questions regarding passenger survival traits.

## ⚙️ Core Requirements Covered
* **DataFrame Operations:** `shape`, `head()`, `info()`, and `describe()` structure baseline profiling.
* **Data Cleaning:** Imputed missing `age` values based on sub-demographics (`pclass` and `sex`), filled `embarked` using mode metrics, and handled dropped structural columns.
* **Aggregations & Groupings:** Layered analysis using `groupby` configurations alongside custom age binning via `pd.cut`.

## 🛠️ Tech Stack & Libraries
* **Language:** Python 3.10+
* **Libraries:** Pandas, Seaborn

## 📈 Key Findings & Insights
* **Gender Factor:** Women achieved a significantly higher survival rate (**74%**) than men (**19%**).
* **Socioeconomic Influence:** 1st Class passengers had the highest survival priority rate (**63%**) compared to 3rd Class passengers (**24%**).
* **Age Distribution:** Children (ages 0-12) saw a strong survival preference (**50%**), while seniors (ages 60+) suffered the lowest outcome rates (**27%**).
