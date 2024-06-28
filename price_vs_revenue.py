#importing all the necessary libraries

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df=pd.read_csv("supply_chain_data.csv")
df.head()

# Bar graph of Price vs Revenue generated
plt.bar(df["Price"], df["Revenue generated"])
plt.xlabel("Price")
plt.ylabel("Revenue")
plt.title("Price vs Revenue generated")
plt.show()
