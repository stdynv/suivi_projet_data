<img src="https://images.unsplash.com/photo-1511512578047-dfb367046420?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2671&q=80">
<div align="center">
  <strong>Data Analysis Project</strong>
</div>
<div align="center" style="size:20px">
  :chart_with_downwards_trend::bar_chart::chart_with_upwards_trend:
</div>
<h1 align="center">Video Games Sales</h1>
<br />
<div align="center">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/stdynv/suivi_projet_data?style=for-the-badge">
  <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/stdynv/suivi_projet_data?style=for-the-badge">
  <img alt="GitHub commit activity (branch)" src="https://img.shields.io/github/commit-activity/w/stdynv/suivi_projet_data/main?style=for-the-badge">
  <img alt="GitHub" src="https://img.shields.io/github/license/stdynv/suivi_projet_data?style=for-the-badge">
</div>

<div align="center">
  <sub> Analyser le marché des jeux vidéos au fil de la période 1994-2021
</div>

## Table of Contents
- [Description du Projet](#description-du-projet)
  - [Contributeurs](#contributeurs)
  - [Technologies Utilisées](#technologies-utilisées)
  - [Dataset](#dataset)
- [Analyse Statistiques](#analyse-statistiques)
  - [Exploration de Données](#exploration-données)
  - [Analyse Prédective](#analyse-prédective)
- [Machine Learning](#machine-learning)
### Description du projet
  ![video-games-rise](https://user-images.githubusercontent.com/78117993/166926993-b8f26bd6-588c-4371-b5d5-7b9995f9da27.jpg)
  - le chiffre d’affaire de l’industrie des jeux vidéos à atteint $165B en 2020 
  - les jeux vidéos sur le mobile en 2020 génère plus que le double des revenue sur des PCs et des consoles ce qui explique l'accessibilité des jeux pour les        utilisateurs 
- le marché des jeux vidéo va atteindre $200B et 3B d’utilisateurs en 2023
### Dataset
  - le jeu de données contient plus 100.000 données de jeux et keurs revenues en ce basant par les platforms , genres années ... 


| Fields          | Description                                |
| :--------       |:-------------------------                  |
| `Rank`          |Classement des jeux videos                  |
| `Name`          |Nom du jeu                                  |
| `Platform`      |Plate-forme de sortie du jeu                |
| `Year`          |Année de sortie du jeu                      |
| `Genre`         |Genre du jeu                                |
| `Publisher`     |Editeur du jeu                              |
| `NA Sales`      |Ventes en Amérique du Nord (en millions)    |              
| `EU Sales`      |Ventes en Europe (en millions)              |
| `JP Sales`      |Ventes en Japon (en millions)               |
| `Other Sales`   |Ventes dans le reste du monde (en millions) |
| `Global Sales`  |Ventes dans le monde entier (en millions)   |

[Get Data](https://www.kaggle.com/datasets/gregorut/videogamesales)

### Contributeurs
<table>
  <tr>
    <td align="center"><a href="https://github.com/stdynv"><img src="https://avatars.githubusercontent.com/u/78117993?s=400&u=305e97e37db3124de830f504aa0282434ed9e77e&v=4" width="100px;" alt=""/><br /><sub><b>Mohamed Yassine Essamadi</b></sub></a><br /><a href="#question-kentcdodds" title="Answering Questions">💬</a> <a href="https://github.com/stdynv" title="Documentation">📖</a> <a href="https://github.com/stdynv" title="Reviewed Pull Requests">👀</a> <a href="#talk-kentcdodds" title="Talks">📢</a></td>
    <td align="center"><a href="https://github.com/DiogoA78"><img src="https://avatars.githubusercontent.com/u/93249422?v=4" width="100px;" alt=""/><br /><sub><b>Diogo Almeida </b></sub></a><br /><a href="https://github.com/DiogoA78" title="Documentation">📖</a> <a href="https://github.com/DiogoA78" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/DiogoA78" title="Tools">🔧</a></td>
  </tr>
</table>
### Technologies Utilisées

### Analyse Statistiques
  - notre problématique est de suivre l'évolution du marché des jeux vidéos au courd de l'année 1994 et 2021 
  ### Exploration Données
  #### Nombre de jeux vendus par Plateforme
  ![image](https://user-images.githubusercontent.com/78117993/167117747-cc4d99a2-9c04-4968-8aae-5d913e561117.png)
  - la majorité des jeux sont joué en PS2 
  - la PS2 est la platforme la plus jouable vu qu'elle a réaliser 1.2 billion de dollars
  #### Combien de Jeux sont sortis par année et qui est l'éditeur qui vent le plus
  ```
  plt.figure(figsize=(30, 15))
  g = sns.barplot(x='Year', y='Count', data=top_publisher_count)
  index = 0
  for value in top_publisher_count['Count'].values:
     g.text(index, value + 5, str(publisher[index] + '----' +str(value)), color='#000', size=14, rotation= 90, ha="center")
     index += 1
  plt.xticks(rotation=90)
  plt.show()
  ```
  ![image](https://user-images.githubusercontent.com/78117993/167119436-491fd90c-8493-4162-b4e0-4cd6cd77cbab.png)
  - ce graphique nous expliquent combien de jeux sont sortie par année et aussi l'éditeur qui réalise le plus des ventes
  - on regarde une augmentation des ventes entre 1980 et 2009 et une baisse de vente entre 2010 et 2020 ce qui confus le marché des jeux vidéos qui est a $169B       ce qui explique que les ventes calculé sont sur des ventes physiques et non pas numériques
  #### La Moyenne Des Ventes Par Region
  ```
  north_amera_sales = df['NA_Sales'].mean() * 1000000
  europe_sales = df['EU_Sales'].mean() * 1000000
  japon_sales = df['JP_Sales'].mean() * 1000000
  other_sales = df['Other_Sales'].mean() * 1000000

  columns = ['North America','Europe','Japon','Other']
  values = [north_amera_sales,europe_sales,japon_sales,other_sales]
  plt.figure(figsize=(10,5))
  plt.title('La Moyenne des vente Par Region')
  plt.xlabel('Region')
  plt.bar(columns,values)
  ```
  ![image](https://user-images.githubusercontent.com/78117993/167122361-1e5040fe-0d95-466e-bb49-d7983003e782.png)
  - L'Amérique du Nord a les ventes moyennes les plus élevées de 264 667,430 $ 
  #### les jeux qui réalisent actuellement le plus de ventes dans le monde ?
  ```
  top = pd.DataFrame(df.groupby("Name")[["Global_Sales"]].sum().sort_values(by=['Global_Sales'],ascending=False).reset_index())
  top_10 = pd.DataFrame(top.head(10))
  ax = sns.barplot(x='Global_Sales', y='Name', data=top_10)
  ax.set_title('Les Meilleurs Jeux Globalement')
  ax.set_xlabel('Global Sales')
  ```
  ![image](https://user-images.githubusercontent.com/78117993/167123197-72deff0d-4aff-436b-bd36-0d3717b0f4dd.png)
  - Wii Sports est le jeu qui réalise le plus de vente dans le monde une revenue plus de $80 millions
  #### Les Meilleurs Jeux Par Region 
  ```
  region_JP = pd.DataFrame(df.groupby('Name')[['JP_Sales']].mean().sort_values(by=['JP_Sales'],ascending=False).reset_index())
  region_NA = pd.DataFrame(df.groupby('Name')[['NA_Sales']].mean().sort_values(by=['NA_Sales'],ascending=False).reset_index())
  region_EU = pd.DataFrame(df.groupby('Name')[['EU_Sales']].mean().sort_values(by=['EU_Sales'],ascending=False).reset_index())
  region_OTH = pd.DataFrame(df.groupby('Name')[['Other_Sales']].mean().sort_values(by=['Other_Sales'],ascending=False).reset_index())
  ax = sns.barplot(x='RegionName_Sales', y='Name', data=region_Name[:5])
  ax.set_title('Les Meilleurs Jeux en Region Name')
  ax.set_xlabel('Jeux')
  ```
  ![image](https://user-images.githubusercontent.com/78117993/167123967-970b2076-2631-49ef-aff8-9c2936bd7e19.png)
  ![image](https://user-images.githubusercontent.com/78117993/167124001-781922a8-92ed-41da-9112-b549e62d3fb3.png)
  ![image](https://user-images.githubusercontent.com/78117993/167124076-2f1ebce6-1e7b-4574-bcf1-90b6a628916a.png)
  ![image](https://user-images.githubusercontent.com/78117993/167124106-623838af-b49f-42fd-87dc-627358370198.png)
  - Pokemon Red/Pokemon Blue est le jeux préféré au Japon
  - Wii Sports est le jeux préféré en Amérique du Nord , Europe et le Reste du Monde
  #### Les Genres qui réalisent les plus de ventes 
  ```
  genre_df = df.groupby("Genre")[["Global_Sales"]].sum().sort_values(by=['Global_Sales'],ascending=[False]).reset_index()
  fig , ax = plt.subplots(figsize=(14,6))
  ax = sns.barplot(x='Genre', y='Global_Sales', data=genre_df)
  ax.set_ylabel('Global Sales in Millions ')
  ax.set_title('Top genres')
  ax.set_xlabel('Genre')
  ```
  ![image](https://user-images.githubusercontent.com/78117993/167124547-ac5b743b-8d1a-40b6-a1c7-57877b5ed899.png)
  - Les jeux d'action sont les plus appréciés dans le monde avec un total presque de 1750 millions de dollars.
  
  #### Les éditeurs qui ont réaliser le plus de ventes en Monde
  ```
  publisher_glb =df.groupby('Publisher')[['Publisher','Global_Sales']].sum().sort_values('Global_Sales', ascending = False).head(20)

  publisher_glb['Global_Sales'].plot(kind = 'bar', 
                            figsize = (11,6), 
                            colormap = 'Set3', 
                            ylabel = 'Global Sales (Millions)', 
                            title = 'Global Video Games Sales by Publisher')
  ```
  ![image](https://user-images.githubusercontent.com/78117993/167125038-c9454d46-1a7d-4ad8-93d6-43683f6cc47e.png)
  - Nintendo est le top éditeur au monde qui réalise un total de 1.75 Billions de dollars
  ### Analyse Prédective
  - Implementer des modèles de machine learning (Linear Regression - Dicision Tree Classifier - Random Forest Classifier )
  - Définir L'algorithme le plus puissant en evaluant chaque modèle 
### Machine Learning
 - Première étape est de séparer notre jeu de données  entre des données d'entrainement(tain) pour entrainer nos données sur le modèle préciser et des données de test pour évaluer notre modèle
 ```
 from sklearn.model_selection import train_test_split
x = df.drop(labels=['Rank','Year','Name','Platform','Genre','Publisher' ,'Global_Sales'],axis=1)
y = df['Global_Sales']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.20,random_state = 42)
 ```
- Implementer Les modèles 
  - Regression Linéaire
  ```
  from sklearn.linear_model import LinearRegression
  LR = LinearRegression()
  model = LR.fit(x_train,y_train)
  y_predict = model.predict(x_test)
  ```
  - Decision Tree Regressor
  ```
  from sklearn.tree import DecisionTreeRegressor
  regressor_Tree = DecisionTreeRegressor()
  regressor_Tree.fit(x_train,y_train)
  y_pred = regressor_Tree.predict(x_test)
  ```
    - Random Forest Regressor
  ```
  from sklearn.ensemble import RandomForestRegressor
  regressor_Forest = RandomForestRegressor(random_state=42)
  regressor_Forest.fit(x_train,y_train)
  y_pred = regressor_Forest.predict(x_test)
  ```
- Evaluer Les modèles 
  ![image](https://user-images.githubusercontent.com/78117993/169816757-1a891aba-67c9-4e73-a33b-5f6c55ee52f4.png)
  - La Regression lineaire est l'algorithme le plus puissant avec un score de 99%
- Camparaison des Valeurs 
  - ce graph visualise les données coorectes dans notre jeu de données en rouge et les données prédite avec notre modèle
  - en  camparant le y_predict et le y_test les valeurs sont un peu près les mêmes . 
  ![image](https://user-images.githubusercontent.com/78117993/169818381-0caa39c5-c968-43b5-bad7-687ad431b87c.png)


 
