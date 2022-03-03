import pandas as pd
import plotly.express as px

df = pd.read_csv("D:\The Archive\Projects and Games\Python Projects\Covid Statistics\Copy+of+data+-+data.csv")
fig = px.scatter(df, x = "date", y = "cases", color = "country")
fig.show()