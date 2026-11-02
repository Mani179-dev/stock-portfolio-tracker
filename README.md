📊 Stock Portfolio Performance Tracker

📌 Project Overview

The Stock Portfolio Performance Tracker is a Python-based application that helps users manage their stock investments and monitor portfolio performance.

Users can add stock holdings, enter purchase prices and quantities, update current stock prices, and calculate profit or loss for individual stocks and the overall portfolio.

The application also exports portfolio performance reports into a CSV file.

✨ Features

- Load 503 S&P 500 company records from a CSV dataset.
- Search companies by ticker symbol, company name, or sector.
- Add stocks to a personal portfolio.
- Update current stock prices manually.
- Calculate individual stock investment values.
- Calculate profit and loss.
- Calculate overall portfolio performance.
- Export portfolio reports to CSV.

🛠️ Technologies Used

- Python 3
- CSV Module
- Dictionaries
- Functions
- OS Module
- Datetime Module

📂 Project Structure

Stock-Portfolio-Tracker/
│
├── portfolio.py
├── sp500_ticker_dataset.csv
├── portfolio_summary.csv
└── README.md

▶️ How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Keep "portfolio.py" and "sp500_ticker_dataset.csv" in the same folder.
4. Open the project folder in VS Code.
5. Run the following command:

python portfolio.py

6. Follow the menu options to manage your portfolio.

📈 Sample Calculation

Stock| Purchase Price| Quantity| Current Price
AAPL| 8700|48800| 609000


Portfolio Summary

Description| Amount
Total Investment| 609000
Current Portfolio Value| 609000
Total Profit/Loss| 0
Overall Gain/Loss| 0%

The prices above are sample values for testing purposes, not live market prices.

📄 CSV Report

The application generates "portfolio_summary.csv", containing:

- Stock ticker
- Company name
- Purchase price
- Current price
- Quantity
- Total investment
- Current value
- Profit/Loss
- Gain/Loss percentage

🚀 Future Improvements

- Integrate live stock market prices.
- Save portfolio holdings between program sessions.
- Add graphical portfolio performance charts.
- Develop a graphical user interface.

👨‍💻 Author

Manikanta Vykuntam

Python | C | Data Structures and Algorithms

---

⭐ If you find this project useful, consider giving the repository a star!
