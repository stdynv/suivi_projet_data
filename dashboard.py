import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np 
import altair as alt


df = pd.read_csv("./data/vgsales.csv")
df = df.dropna()
df = df.astype({"Year": int}, errors='raise') 

st.title("Games Sales since 1980")

st.markdown("Un **_jeu vidéo_** est un jeu électronique doté d'une interface utilisateur permettant une interaction humaine ludique en générant un retour visuel sur un dispositif vidéo. Le joueur de jeu vidéo dispose de périphériques pour agir sur le jeu et percevoir les conséquences de ses actes sur un environnement virtuel.")

#Platform_Sales
st.header("Platforms Sales")

st.markdown("Différents types de systèmes sur lesquels le jeu vidéo se pratique coexistent, et de nombreux jeux sont dorénavant disponibles sur ces plates-formes. Les consoles de jeux, les bornes d'arcade et les ordinateurs, en sont les trois principaux vecteurs.")


platforms =  df.groupby("Platform").sum().sort_values(by="Global_Sales", ascending = False)

df_platform = pd.DataFrame(data=platforms['Global_Sales'], columns=['Platform', 'Global_Sales'])
df_platform['Platform'] = df_platform.index

plat = st.multiselect("Platforms Sales", df_platform['Platform'], default=df_platform['Platform'])

plot_platform = df_platform[df_platform.Platform.isin(plat)]

essai = alt.Chart(plot_platform).mark_bar().encode(x='Global_Sales', y=alt.Y("Platform",sort=alt.EncodingSortField(field="Global_Sales", order="descending")), color='Platform')

st.altair_chart(essai, use_container_width=True)


col1, col2, col3 = st.columns([3,8,3])
with col2:
    st.image("https://www.cdiscount.com/pdt2/9/2/1/1/550x550/0711719901921/rw/console-sony-ps-two-console-ps2.jpg", width = 350, caption="Ps2, console ayant vendu le plus de jeu")


#Gender
st.header("Gender")

st.markdown("Les jeux vidéos sont catégorisés par genre. **_Ex: Action, sport, simulation..._**")


genders = df.groupby("Genre").sum().sort_values(by="Global_Sales", ascending=False)

df_gender = pd.DataFrame(data=genders['Global_Sales'], columns=['Gender', 'Global_Sales'])
df_gender['Gender'] = df_gender.index

gender = st.multiselect("Genders Sales", df_gender['Gender'], default=df_gender['Gender'])

plot_gender = df_gender[df_gender.Gender.isin(gender)]

essai = alt.Chart(plot_gender).mark_bar().encode(x='Global_Sales', y=alt.Y("Gender",sort=alt.EncodingSortField(field="Global_Sales", order="descending")), color='Gender')

st.altair_chart(essai, use_container_width=True)


col1, col2, col3 = st.columns([3,8,3])
with col2:
    st.image("https://image.jeuxvideo.com/medias-sm/163129/1631287693-7688-jaquette-avant.jpg", width = 350, caption="Gta 5, jeux d'action ayant été vendu le plus")


#Year
st.header("Year")

st.markdown("La vente de jeux vidéo a subi une explosion au début des années 2000 en atteignant son maximum en 2008")

years = df.groupby(['Year']).sum().sort_values(by="Global_Sales",ascending=False)


df_year = pd.DataFrame(data=years['Global_Sales'], columns=['Year', 'Global_Sales'])
df_year['Year'] = df_year.index


year = st.multiselect("Years Sales", df_year['Year'], default=df_year['Year'].head(20))

plot_year = df_year[df_year.Year.isin(year)]

essai = alt.Chart(plot_year).mark_bar().encode(x='Year', y=alt.Y("Global_Sales",sort=alt.EncodingSortField(field="Year", order="descending")), color='Global_Sales')

st.altair_chart(essai, use_container_width=True)

col1, col2, col3 = st.columns([3,8,3])
with col2:
    st.image("data:image/jpeg;base64,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", width = 350, caption="Mario Kart Wii, jeux ayant été vendu le plus en 2008")

#Publisher
st.header("Publisher")

st.markdown("Qu’ils développent des **_jeux vidéo_** avec leurs studios internes ou qu’ils éditent simplement les productions de développeurs indépendants, les **_éditeurs_** jouent un rôle crucial de financement, de conseil et de communication sur les projets dont ils s’occupent.")

publishers = df.groupby(['Publisher']).sum().sort_values(by="Global_Sales",ascending=False)

df_publisher = pd.DataFrame(data=publishers['Global_Sales'], columns=['Publisher', 'Global_Sales'])
df_publisher['Publisher'] = df_publisher.index

publisher = st.multiselect("Publishers Sales", df_publisher['Publisher'], default=df_publisher['Publisher'].head(20))

plot_publisher = df_publisher[df_publisher.Publisher.isin(publisher)]

essai = alt.Chart(plot_publisher).mark_bar().encode(x='Global_Sales', y=alt.Y("Publisher",sort=alt.EncodingSortField(field="Global_Sales", order="descending")), color='Publisher')

st.altair_chart(essai, use_container_width=True)

col1, col2, col3 = st.columns([3,8,3])
with col2:
    st.image("data:image/png;base64,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", width = 350, caption="Nintendo, éditeur ayant été vendu le plus de jeux")


#Sales_Location
st.header("Sales by Location")

df_country_sales = df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum()
df_country_sales = pd.DataFrame(data = df_country_sales, columns=['Location'])
df_country_sales = pd.DataFrame(data = df_country_sales["Location"], columns=['Location', "Sales"])
df_country_sales['Sales'] = df_country_sales["Location"]
df_country_sales['Location'] = df_country_sales.index

country_sales = st.multiselect("Location Sales", df_country_sales['Location'], default=df_country_sales['Location'].head(20))

plot_country_sales = df_country_sales[df_country_sales.Location.isin(country_sales)]

essai = alt.Chart(plot_country_sales).mark_bar().encode(x="Location", y=alt.Y("Sales",sort=alt.EncodingSortField(field="Location", order="descending")), color='Location')

st.altair_chart(essai, use_container_width=True)

col1, col2, col3 = st.columns([3,8,3])
with col2:
    st.image("https://medias.voyageons-autrement.com/album/Carte_Amrique_du_Nord.jpg", width = 350, caption="Amérique du nord, continent ou il y a eu le plus de ventes de jeux")


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

