# main.py
from datetime import datetime
import data_retrieval
import technical_indicators
import decision_making
import pandas as pd

# Parameters
start_date = "2023-01-01"
end_date = "2024-09-30"

# Step 1: Retrieve data
data = data_retrieval.get_currency_data(start_date, end_date)

# Step 2: Calculate Technical Indicators
data = technical_indicators.calculate_moving_average(data, window=20)
data = technical_indicators.calculate_bollinger_bands(data, window=20)
data = technical_indicators.calculate_cci(data, window=20)

# Step 3: Make Decision
data = decision_making.make_decision(data)

# Save results to CSV for PowerPoint reference
data.to_csv("eur_inr_analysis.csv", index=True)
print("Analysis complete and saved to eur_inr_analysis.csv")
# from requests_html import HTMLSession

# session = HTMLSession()
# response = session.get('https://youtube.com')
# print(response.html.html)  # Should print HTML content of the page if working
