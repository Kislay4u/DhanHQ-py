from dhanhq import DhanContext, MarketFeed
from dhanhq._portfolio import Portfolio
from utils import MarketDataFilter
import pandas as pd
from dhanhq._historical_data import HistoricalData

# Initialize the DhanContext with your API key
client_id = "1104739857"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzQyMDUxODIwLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwNDczOTg1NyJ9.WHmh4wTO_JRN_UiUjgnHK5hm6rgAUb8fzw8tu4p7I77OMerjqNTK3UPa2216CBLOkZsVbREwrkEZD-DqeXW9Kg"


# Define and use your dhan_context if you haven't already done so like below:
dhan_context = DhanContext(client_id,access_token)

# Structure for subscribing is (exchange_segment, "security_id", subscription_type)

instruments = [(MarketFeed.NSE, "1333", MarketFeed.Ticker),   # Ticker - Ticker Data
    (MarketFeed.NSE, "1333", MarketFeed.Quote),     # Quote - Quote Data
    (MarketFeed.NSE, "1333", MarketFeed.Full),      # Full - Full Packet
    (MarketFeed.NSE, "11915", MarketFeed.Ticker),
    (MarketFeed.NSE, "11915", MarketFeed.Full)]

version = "v2"          # Mention Version and set to latest version 'v2'

def fetch_open_positions(dhan_context):
    try:
        positions = Portfolio.get_positions(dhan_context)
        return positions
    except Exception as e:
        print(f"Error fetching open positions: {e}")
        return None

# Fetch and print current open positions
open_positions = fetch_open_positions(dhan_context)
if open_positions:
    print("Current Open Positions:")
    for position in open_positions:
        print(position)
else:
    print("No open positions found.")

# In case subscription_type is left as blank, by default Ticker mode will be subscribed.
def fetch_historical_data(dhan_context, instrument, interval, start_time, end_time):
    try:
        historical_data = HistoricalData.intraday_minute_data(
            dhan_context, instrument, MarketFeed.NSE, "EQ", start_time, end_time, interval
        )
        return historical_data
    except Exception as e:
        print(f"Error fetching historical data: {e}")
        return None

# Define the instrument, interval, and time range
instrument = "1333"
interval = 1
start_time = "2023-10-10T09:00:00Z"  # Example start time
end_time = "2023-10-10T15:30:00Z"    # Example end time

# Fetch and print historical data
historical_data = fetch_historical_data(dhan_context, instrument, interval, start_time, end_time)
if historical_data:
    print("Historical Data:")
    print(pd.DataFrame(historical_data))
else:
    print("No historical data found.")


myFilter = MarketDataFilter()
try:
    data = MarketFeed(dhan_context, instruments, version)
    while True:
        data.run_forever()
        response = data.get_data()
        # Initialize the filter
        
        # print(pd.DataFrame.from_dict([response]))
        result = myFilter.filter_data([response])
        # Retrieve DataFrames
        print(myFilter.get_dataframe("Quote Data"))

except Exception as e:
    print(e)

# Close Connection
data.disconnect()

# Subscribe instruments while connection is open
sub_instruments = [(MarketFeed.NSE, "14436", MarketFeed.Ticker)]

data.subscribe_symbols(sub_instruments)

# Unsubscribe instruments which are already active on connection
unsub_instruments = [(MarketFeed.NSE, "1333", 16)]

data.unsubscribe_symbols(unsub_instruments)