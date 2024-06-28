import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("../data/supply_chain_data.csv")

# Analyzing Sales by Product Type
sales_data = df.groupby("Product type")["Number of products sold"].sum().reset_index()

pie_chart = px.pie(sales_data, values="Number of products sold", names="Product type", title="Sales by Product Type", color_discrete_sequence=px.colors.qualitative.Antique)
pie_chart.update_traces(textposition="inside", textinfo="percent+label")
pie_chart.show()
