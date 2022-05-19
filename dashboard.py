import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np 
import altair as alt


df = pd.read_csv("./data/vgsales.csv")
df = df.dropna()
df = df.astype({"Year": int}, errors='raise') 

st.title("Games Sales since 1980")



#Platform_Sales
st.header("Platforms Sales")

platforms =  df.groupby("Platform").sum().sort_values(by="Global_Sales", ascending = False)

df_platform = pd.DataFrame(data=platforms['Global_Sales'], columns=['Platform', 'Global_Sales'])
df_platform['Platform'] = df_platform.index

plat = st.multiselect("Platforms Sales", df_platform['Platform'], default=df_platform['Platform'])

plot_platform = df_platform[df_platform.Platform.isin(plat)]

essai = alt.Chart(plot_platform).mark_bar().encode(x='Global_Sales', y=alt.Y("Platform",sort=alt.EncodingSortField(field="Global_Sales", order="descending")), color='Platform')

st.altair_chart(essai, use_container_width=True)

#Gender
st.header("Gender")

genders = df.groupby("Genre").sum().sort_values(by="Global_Sales", ascending=False)

df_gender= pd.DataFrame(data=genders['Global_Sales'], columns=['Gender', 'Global_Sales'])
df_gender['Gender'] = df_gender.index

gender = st.multiselect("Genders Sales", df_gender['Gender'], default=df_gender['Gender'])

plot_gender = df_gender[df_gender.Gender.isin(gender)]

essai = alt.Chart(plot_gender).mark_bar().encode(x='Global_Sales', y=alt.Y("Gender",sort=alt.EncodingSortField(field="Global_Sales", order="descending")), color='Gender')

st.altair_chart(essai, use_container_width=True)


#Year
st.header("Year")

#Publisher
st.header("Publisher")

publishers = df.groupby(['Publisher']).sum().sort_values(by="Global_Sales",ascending=False)

df_publisher= pd.DataFrame(data=publishers['Global_Sales'], columns=['Publisher', 'Global_Sales'])
df_publisher['Publisher'] = df_publisher.index

publisher = st.multiselect("Publishers Sales", df_publisher['Publisher'], default=df_publisher['Publisher'].head(20))

plot_publisher = df_publisher[df_publisher.Publisher.isin(publisher)]

essai = alt.Chart(plot_publisher).mark_bar().encode(x='Global_Sales', y=alt.Y("Publisher",sort=alt.EncodingSortField(field="Global_Sales", order="descending")), color='Publisher')

st.altair_chart(essai, use_container_width=True)



#Sales_Continent
st.header("Sales by Continent")
df_country_sales = df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum()
df_country_sales = pd.DataFrame(data = df_country_sales, columns=['Continent'])
df_country_sales = pd.DataFrame(data = df_country_sales["Continent"], columns=['Continent', "Sales"])
df_country_sales['Sales'] = df_country_sales["Continent"]
df_country_sales['Continent'] = df_country_sales.index


essai = alt.Chart(df_country_sales).mark_bar().encode(x="Continent", y=alt.Y("Sales",sort=alt.EncodingSortField(field="Continent", order="descending")), color='Continent')

st.altair_chart(essai, use_container_width=True)


#Data
st.header("Data")
"""
To download:
```python
import pandas as pd
df = pd.read_csv("./data/vgsales.csv")
df = df.astype({"Year": str}, errors='raise')
```
"""

st.dataframe(df)

