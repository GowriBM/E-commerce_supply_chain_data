import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("../data/supply_chain_data.csv")

# Shipping cost of carriers
ship_cost = px.bar(df, x="Shipping carriers", y="Shipping costs", title="Shipping cost of carriers")
ship_cost.show()
