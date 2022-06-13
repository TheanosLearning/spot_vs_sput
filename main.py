import pandas as pd
import matplotlib.pyplot as plt

"""
SPUT pounds purchased data `u_un.csv`
source: https://sprott.com/investment-strategies/physical-commodity-funds/uranium

Uranium spot price data `uxc.csv`
source: https://tradingeconomics.com/commodity/uranium
"""

sput = pd.read_csv(R"./data/u_un.csv", parse_dates=True)  # X
spot = pd.read_csv(R"./data/uxc.csv", parse_dates=True)  # Y

sput.plot.bar()  # pounds purchased
spot.plot()  # spot price

plt.show()
