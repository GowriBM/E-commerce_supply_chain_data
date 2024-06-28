import pandas as pd
import plotly.graph_objects as go

# Load data
df = pd.read_csv("../data/supply_chain_data.csv")

# Total revenue generated from shipping carriers
total_revenue = df.groupby("Shipping carriers")["Revenue generated"].sum().reset_index()

fig = go.Figure()
fig.add_trace(go.Bar(x=total_revenue["Shipping carriers"], y=total_revenue["Revenue generated"]))
fig.update_layout(title="Total revenue generated from shipping carriers", xaxis_title="Shipping carriers", yaxis_title="Revenue Generated")
fig.show()
