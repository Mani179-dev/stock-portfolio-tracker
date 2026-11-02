import csv
import os
from datetime import datetime

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_FILE = os.path.join(
    BASE_DIR, "sp500_ticker_dataset.csv"
)

OUTPUT_FILE = os.path.join(
    BASE_DIR, "portfolio_summary.csv"
)

# Portfolio storage
portfolio = {}


# 1. Load S&P 500 companies
def load_companies():
    if not os.path.exists(DATASET_FILE):
        print("Dataset file not found!")
        return []

    try:
        with open(DATASET_FILE, "r",
                  encoding="utf-8-sig",
                  newline="") as file:

            reader = csv.DictReader(file)
            companies = list(reader)

        print(f"Successfully loaded {len(companies)} companies.")
        return companies

    except (OSError, csv.Error) as error:
        print("Error loading dataset:", error)
        return []


# 2. Search companies
def search_company(companies, keyword):
    keyword = keyword.lower()
    results = []

    for company in companies:
        ticker = company["Symbol"].lower()
        name = company["Security"].lower()
        sector = company["GICS Sector"].lower()

        if (keyword in ticker or
                keyword in name or
                keyword in sector):

            results.append(company)

    return results


# 3. Display companies
def display_companies(results):
    if not results:
        print("No matching companies found.")
        return

    for company in results:
        print("------------------------------")
        print("Ticker:", company["Symbol"])
        print("Company:", company["Security"])
        print("Sector:", company["GICS Sector"])


# 4. Add stock to portfolio
def add_holding(companies):
    ticker = input("Enter stock ticker: ").strip().upper()

    company = None

    for item in companies:
        if item["Symbol"].strip().upper() == ticker:
            company = item
            break

    if company is None:
        print("Invalid ticker symbol!")
        return

    if ticker in portfolio:
        print("Stock already exists in portfolio!")
        return

    try:
        buy_price = float(input("Enter purchase price: "))
        quantity = int(input("Enter number of shares: "))

        if buy_price <= 0 or quantity <= 0:
            print("Price and quantity must be positive.")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    portfolio[ticker] = {
        "company": company["Security"],
        "buy_price": buy_price,
        "quantity": quantity,
        "current_price": None
    }

    print(f"{ticker} added successfully!")
    print("current portfolio:",portfolio)


# 5. Update current stock price
def update_current_price():
    if not portfolio:
        print("Portfolio is empty!")
        return

    ticker = input("Enter ticker to update: ").strip().upper()

    if ticker not in portfolio:
        print("Stock not found!")
        return

    try:
        price = float(input("Enter current stock price: "))

        if price <= 0:
            print("Price must be greater than zero.")
            return

    except ValueError:
        print("Enter a valid price.")
        return

    portfolio[ticker]["current_price"] = price

    print(f"{ticker} price updated successfully!")


# 6. Calculate performance
def calculate_performance():
    print("Calculating portfolio performance...",portfolio)
    if not portfolio:
        print("\nportfolio is empty")
        return None

    results = []
    total_investment = 0
    total_current_value = 0

    all_prices_available = True

    print("\n========== PORTFOLIO PERFORMANCE ==========")

    for ticker, details in portfolio.items():

        buy_price = details["buy_price"]
        quantity = details["quantity"]
        current_price = details["current_price"]

        investment = buy_price * quantity
        total_investment += investment
        print("\n------------------------------")
        print("Ticker:", ticker)
        print("Company:", details["company"])
        print("Purchase Price:", buy_price)
        print("Quantity:", quantity)
        print("Total Investment:", round(investment, 2))

        current_value = ""
        profit_loss = ""
        percentage = ""
        if current_price is  None:
            all_prices_available = False
            print("current price not entered")
        else:
            current_value = current_price * quantity
            profit_loss=current_value-investment
            percentage=(profit_loss/investment)*100
            total_current_value+=current_value
            print("current price:",current_price)
            print("current value:",round(current_value,2))
            print("profit/loss:",round(profit_loss,2))
            print("gain/loss:",round(percentage,2),"%")
        #store calculated details
        results.append({"ticker":ticker,"company":details["company"],"buy_price":buy_price, 
                        "current_price":current_price,"quantity":
                        quantity,"investment":investment,"current_value":current_value,"profit_loss":profit_loss,"percentage":percentage
                        })  
        summary = None
        if all_prices_available:
            overall_profit_loss = (total_current_value - total_investment)
            overall_percentage=(overall_profit_loss/total_investment)*100
            summary={"total_investment":total_investment,
                     "total_current_value":total_current_value,
                     "total_profit_loss":overall_profit_loss,
                     "overall_percentage":overall_percentage
                     }  
            print("\n========== TOTAL SUMMARY ==========") 
            print("Total Investment:",round(total_investment,2))
            print("Total Current Value:",round(total_current_value,2))
            print("Total Profit/Loss:",round(overall_profit_loss,2))
            print("Overall Gain/Loss Percentage:",round(overall_percentage,2),"%")
        return results,summary    

                       
 # 7. Export portfolio to CSV
def export_portfolio():
    print("\nStarting CSV export...")
    print("Calculating performance before export...",portfolio)

    performance = calculate_performance()
    print("performance result",performance)

    print("Performance calculated successfully!")


    if performance is None:
        print("Export stopped: Portfolio is empty.")
        return

    print("Preparing CSV data...")

    results, summary = performance

    fieldnames = [
        "Date",
        "Ticker",
        "Company",
        "Purchase Price",
        "Current Price",
        "Quantity",
        "Total Investment",
        "Current Value",
        "Profit/Loss",
        "Gain/Loss Percentage"
    ]

    current_date = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    try:
        print("Creating CSV file...")

        with open(OUTPUT_FILE, "w",
                  newline="",
                  encoding="utf-8") as file:

            writer = csv.DictWriter(
                file, fieldnames=fieldnames
            )

            writer.writeheader()

            for item in results:
                writer.writerow({
                    "Date": current_date,
                    "Ticker": item["ticker"],
                    "Company": item["company"],
                    "Purchase Price": item["buy_price"],
                    "Current Price": item["current_price"],
                    "Quantity": item["quantity"],
                    "Total Investment": round(item["investment"], 2),
                    "Current Value": item["current_value"],
                    "Profit/Loss": item["profit_loss"],
                    "Gain/Loss Percentage": item["percentage"]
                })

            if summary is not None:
                writer.writerow({
                    "Date": current_date,
                    "Ticker": "TOTAL",
                    "Company": "Portfolio Summary",
                    "Total Investment": round(summary["total_investment"], 2),
                    "Current Value": round(summary["total_current_value"], 2),
                    "Profit/Loss": round(summary["total_profit_loss"], 2),
                    "Gain/Loss Percentage": round(summary["overall_percentage"], 2)
                })

        print("\nCSV exported successfully!")
        print("File location:", OUTPUT_FILE)

    except OSError as error:
        print("CSV export failed:", error)

# 8. View portfolio
def view_portfolio():
    if not portfolio:
        print("Portfolio is empty!")
        return

    print("\n========== MY PORTFOLIO ==========")

    for ticker, details in portfolio.items():

        print("\n------------------------------")
        print("Ticker:", ticker)
        print("Company:", details["company"])
        print("Purchase Price:", details["buy_price"])
        print("Current Price:", details["current_price"])
        print("Quantity:", details["quantity"])


# 9. Main menu
def main():
    companies = load_companies()

    if not companies:
        return

    while True:

        print("\n====== STOCK PORTFOLIO TRACKER ======")
        print("1. Search Companies")
        print("2. Add Stock")
        print("3. Update Current Price")
        print("4. View Portfolio")
        print("5. Calculate Performance")
        print("6. Export Portfolio to CSV")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            keyword = input(
                "Enter ticker/company/sector: "
            ).strip()

            if keyword:
                results = search_company(
                    companies, keyword
                )

                display_companies(results)

            else:
                print("Enter a search keyword.")

        elif choice == "2":
            add_holding(companies)

        elif choice == "3":
            update_current_price()

        elif choice == "4":
            view_portfolio()

        elif choice == "5":
            calculate_performance()

        elif choice == "6":
            export_portfolio()
        elif choice == "7":
            print("thank you for using the Stock Portfolio Tracker!")
            break
        else:
            print("Invalid choice! Please select a valid option.")   
#10.program excution
if __name__ == "__main__":   
    main()                  