<div align="center">

# 📊 Amazon Product Sales Dashboard

**An interactive Power BI dashboard that turns raw Amazon product data into business insights**

[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Python](https://img.shields.io/badge/Python-Data%20Cleaning-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

</div>

---

## 📖 Description
A data analytics project covering the full workflow: cleaning a raw Amazon product dataset in Python (Pandas), then visualizing it in an interactive Power BI dashboard. It lets you explore products by category, rating, price, and discount.

## 🖥️ Screenshots
![Dashboard](./Screenshots/dashboard.png)

## ❗ Problem
Raw e-commerce data is messy: prices carry currency symbols, ratings are stored as text, and values are missing. This makes it hard to see which categories, prices, and products actually perform well. This project cleans the data and presents it in one interactive view.

## 📱 Features
- **KPI cards:** total products, average customer rating, average selling price, average discount (%)
- Category-wise product analysis
- Average rating by category
- Average discount by category
- Top 10 most reviewed products
- Selling price vs customer rating analysis
- Interactive category slicer

## 🧠 How It Works
1. **Clean:** the raw dataset is cleaned in Python using Pandas.
2. **Export:** the cleaned data is saved as `amazon_cleaned_data.csv`.
3. **Visualize:** the cleaned CSV is loaded into Power BI, where the KPIs, charts, and slicer are built.

## 🧹 Data Cleaning
- Removing unnecessary columns
- Handling missing values
- Converting prices, ratings, and discounts to numeric values
- Removing special characters from currency fields
- Preparing the dataset for visualization

## 🛠️ Tech Stack
| Layer | Technology |
|------|-----------|
| Data Cleaning | Python, Pandas |
| Data Source | CSV dataset |
| Visualization | Power BI |

## 🏗️ Architecture
```
amazon-product-sales-dashboard/
├── Amazon_Product_Sales_Dashboard.pbix   # Power BI dashboard
├── README.md
├── data/
│   ├── amazon_raw_data.csv               # original dataset
│   ├── amazon_cleaned_data.csv           # cleaned output
│   └── data_cleaning.py                  # cleaning script
└── screenshots/
    └── dashboard.png                     # dashboard preview
```

## 💡 Key Insights
- Electronics contains the highest number of products in the dataset.
- Office Products has the highest average customer rating.
- Home Improvement products receive the highest average discount percentage.
- A small number of products account for the majority of customer reviews.
- Selling price does not show a strong relationship with customer ratings.

---

## 👨‍💻 Author

**Rahul Walawalkar**

GitHub: [@raahu1l](https://github.com/raahu1l)

Thanks for stopping by! I hope you enjoy exploring this project as much as I enjoyed building it.

⭐ If you like this project or find it useful, consider giving it a star!
