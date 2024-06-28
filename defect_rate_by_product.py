import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("../data/supply_chain_data.csv")

# Defect rate of product while shipping
defect_rates = df.groupby("Product type")["Defect rates"].mean().reset_index()

fig = px.bar(defect_rates, x="Product type", y="Defect rates", title="Defect rate of product while shipping")
fig.show()
