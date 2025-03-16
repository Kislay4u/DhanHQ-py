import pandas as pd

class MarketDataFilter:
    def __init__(self):
        self.data_store = {
            "Ticker Data": [],
            "Previous Close": [],
            "Quote Data": [],
            "Full Data": []
        }
    
    def add_data(self, data):
        """
        Adds a new market data entry to the appropriate category based on 'type'.
        """
        data_type = data.get("type")
        if data_type in self.data_store:
            self.data_store[data_type].append(data)
    
    def get_dataframe(self, data_type):
        """
        Returns a Pandas DataFrame for a given data type.
        """
        if data_type in self.data_store and self.data_store[data_type]:
            return pd.DataFrame(self.data_store[data_type])
        else:
            return pd.DataFrame()  # Return empty DataFrame if no data available
    
    def filter_data(self, data_list):
        """
        Filters multiple JSON entries and categorizes them.
        """
        for data in data_list:
            self.add_data(data)

# # Example Usage:
# data_entries = [
#     {'type': 'Ticker Data', 'exchange_segment': 1, 'security_id': 1333, 'LTP': '1689.25', 'LTT': '15:59:54'},
#     {'type': 'Previous Close', 'exchange_segment': 1, 'security_id': 1333, 'prev_close': '1691.20', 'prev_OI': 0},
#     {'type': 'Quote Data', 'exchange_segment': 1, 'security_id': 1333, 'LTP': '1689.25', 'LTQ': 100, 'LTT': '15:59:54', 'avg_price': '1690.66', 'volume': 6686457},
#     {'type': 'Full Data', 'exchange_segment': 1, 'security_id': 11915, 'LTP': '16.88', 'LTQ': 1200, 'LTT': '15:58:57', 'avg_price': '16.95', 'volume': 61451832}
# ]

# # Initialize the filter
# market_filter = MarketDataFilter()
# market_filter.filter_data(data_entries)

# # Retrieve DataFrames
# ticker_df = market_filter.get_dataframe("Ticker Data")
# prev_close_df = market_filter.get_dataframe("Previous Close")
# quote_df = market_filter.get_dataframe("Quote Data")
# full_df = market_filter.get_dataframe("Full Data")

# # Display DataFrames
# print(ticker_df, prev_close_df, quote_df, full_df)
