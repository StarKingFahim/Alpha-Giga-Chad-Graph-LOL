import pandas as pd
import plotly.express as px

df = pd.read_csv(r"C:\Users\ranam\Desktop\Python\P-103\Copy+of+data+-+data (1).csv")
fig = px.scatter(df, x="date", y="cases",color="country",title='Corona Cases')
fig.show()  