import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("../data/supply_chain_data.csv")

# Cost distribution by transportation mode
cost_dist = px.bar(df, x="Transportation modes", y="Costs", title="Cost distribution by transportation mode")
cost_dist.show()

transportation_cost = px.pie(df, values="Costs", names="Transportation modes", title="Cost distribution by transportation mode", hole=0.50, color_discrete_sequence=px.colors.qualitative.G10)
transportation_cost.update_traces(textposition="inside", textinfo="percent+label")
transportation_cost.show()
