            
"""Défintion des fonctions de notre module"""
   
   ## Importation des packages

import numpy as np
import pandas as pd
import chardet
import matplotlib.pyplot as plt
from plotly import tools
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import cartopy.crs as ccrs
import cartopy.feature as cfeature


def piechart_num(var_cat_1,var_cat_2,var_num_1,var_num_2,year_1,year_2,name):
    
    """La fonction piechart_num permet, �   partir de 7 variables, d'afficher deux pie charts.
    L'argument var_cat_1 correspond �   un vecteur catégorielle d'une année n d'une base de donnée
    L'argument var_cat_2 correspond �   un vecteur catégorielle d'une année m d'une base de donnée
    L'argument var_num_1 correspond �   un vecteur de variables quantitatives de l'année year_1 d'une base de donnée
    L'argument var_num_2 correspond �   un vecteur de variables quantitatives de l'année year_2 d'une base de donnée
    L'argument year_1 correspond �   une année donnée
    L'argument year_2 correspond �   une autre année donnée, supposée supérieure �  year_1
    L'argument name correspond au nom que l'on veut donner �   la représentation"""
    
    c=var_cat_1.unique()
    d=var_cat_2.unique()
    
    list1=[]
    
    for v in c:
        print(v)
        x_v=0
        x_v+=sum(var_num_1[i] for i in range(len(var_num_1)) if var_cat_1[i]==v)
        print(x_v)
        list1.append(x_v)
    print(list1)
    list2=[]
    for v in d:
        print(v)
        x_v=0
        x_v+=sum(var_num_2[i] for i in range(len(var_num_2)) if var_cat_2[i]==v)
        print(x_v)
        list2.append(x_v)
    print(list2)
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=[year_1, year_2])
    fig.add_trace(go.Pie(labels=c,values=list1,scalegroup="one", name=year_1),1,1)
    fig.add_trace(go.Pie(labels=d,values=list2,scalegroup="one", name=year_2),1,2)
    fig.update_layout(height = 1100,width= 1100, title_text=name)
    fig.show()
    
    
def piechart_string(var_cat_1,var_cat_2,var_str_1,var_str_2,year_1,year_2,name):
    
    """La fonction piechart_string permet, �   partir de 7 variables, d'afficher deux pie charts.
    L'argument var_cat_1 correspond �   un vecteur catégoriel d'une année n d'une base de donnée
    L'argument var_cat_2 correspond �   un vecteur catégoriel d'une année m d'une base de donnée
    L'argument var_str_1 correspond �   un vecteur de string de l'année year_1  d'une base de donnÃ©e
    L'argument var_str_2 correspond �   un vecteur de string de l'année year_2 d'une base de donnÃ©e
    L'argument year_1 correspond �   une année donnée
    L'argument year_2 correspond �   une autre année donnée, supposée supérieure �   year_2
    L'argument name correspond au nom que l'on veut donner �   la représentation"""
    
    c=var_cat_1.unique()
    d=var_cat_2.unique()
    
    list1=[]
    
    for v in c:
        print(v)
        x_v=0
        for i in range(len(var_cat_1)):
            if var_cat_1[i]==v:
                x_v+=1 
        print(x_v)
        list1.append(x_v)
    print(list1)
    list2=[]
    for v in d:
        print(v)
        x_v=0
        for i in range(len(var_cat_2)):
            if var_cat_2[i]==v:
                x_v+=1 
        print(x_v)
        list2.append(x_v)
    print(list2)
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=[year_1, year_2])
    fig.add_trace(go.Pie(labels=c,values=list1,scalegroup="one", name=year_1),1,1)
    fig.add_trace(go.Pie(labels=d,values=list2,scalegroup="one", name=year_2),1,2)
    fig.update_layout(height = 1100,width= 1100,title_text=name)
    fig.show()
   
   
    
    ## Fonction pour les cartes

def plot_geo_time_value(data,lim_metropole,variable_of_interest,coordinates,titles,nb_of_periods,title='Titre',plots_per_row=2,plots_per_column=2, scale = 1/3):
    
    """ data : vecteur des dataframes indexés de telle sorte que le datframe le plus récent soit en position 0 variable_of_interest : vecteur qui regroupe les colonnes contenant les valeurs �  représenter et indexé de telle sorte �  correspondre aux datframes contenus dans le vecteur data, 
    coordinates : vecteur de vecteurs de coordonnées et même logique d'indexation
    nb_of_periods : le nombre de cartes que l'on veut représenter
    title : le titre que l'on veut donner aux cartes
    titles : vecteurs de titres �  donner individuellement aux cartes
    plots_per_row : nb de cartes par ligne
    plots_per_columns : nb de cartes par colonne
    scale : scalaire qui représente la grandeur désirée des cercles"""
    
    
    fig = plt.figure(figsize=(15,10)) 

    color_ticker = ['green','orange','red','mediumpurple','blue','black','olivedrab','firebrick','aqua','lightcoral','gold','teal','mediumorchid','coral','yellow','lightblue','fuschia']
    

    for i in range(1,nb_of_periods+1):
    
        ax = fig.add_subplot(plots_per_column,plots_per_row,i,projection=ccrs.PlateCarree())
        ax.set_extent(lim_metropole)
        ax.add_feature(cfeature.OCEAN.with_scale('50m'))
        ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
        ax.add_feature(cfeature.RIVERS.with_scale('50m'))
        ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle=':')
        ax.scatter(data[i-1][coordinates[i-1][0]], data[i-1][coordinates[i-1][1]],
           s=data[i-1][variable_of_interest[i-1]] ** scale, alpha=0.5, color = color_ticker[i-1])
        ax.set_title(titles[i-1])

    fig.suptitle(title, fontsize=16)
    fig.show()


    ## La fonction barplot permet de réaliser un histogramme avec des variables catégorielles
    
    """ 
    var_t0 = nom de la variable de la colonne provenant du dataframe de la valeur pour l'annee t
    var_t1 = nom de la variable de la colonne provenant du dataframe de la valeur pour l'annee t+1
    pivot_t1 = nom de la variable de la colonne provenant du dataframe df19 des catégories représentées en abscisse
    pivot_t0 = nom de la variable de la colonne provenant du dataframe df18 des catégories représentées en abscisse  
    absc = titre de l'axe des abcsisses
    ordo = titre de l'axe des ordonnées
    title = titre du graphique
    nb_of_categories = nombre de catégories du barplot
    df19 = nom du dataframe de l'annee t+1
    df18 = nom du dataframe de l'annee t
    
    """

def barplot_variations(var_t0,var_t1,pivot_t1,pivot_t0,absc,ordo,nb_of_categories,title,df19,df18):  
    
    df19sum = df19.groupby(pivot_t1)[var_t1].sum()

    df18sum = df18.groupby(pivot_t0)[var_t0].sum() 
    
    df18sum=pd.DataFrame(df18sum)
    df19sum=pd.DataFrame(df19sum)
    df18sum.rename(columns={var_t0: 'V1'}, inplace=True)
    df19sum.rename(columns={var_t1: 'V2'}, inplace=True)
    df2=pd.merge(df18sum,df19sum, on=pivot_t1 )
    df2['Variation']=(df2['V2']-df2['V1'])*100/df2['V1']
    df2['Categories'] =  df2.index


    plt.bar(x=np.arange(1,nb_of_categories),height=df2['Variation'])
    plt.title(title)
    plt.xlabel(absc)
    plt.ylabel(ordo)
    plt.xticks(np.arange(1,nb_of_categories), df2['Categories'], rotation=90)

    plt.show()
    
