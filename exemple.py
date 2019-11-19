# -*- coding: utf-8 -*-


## """Exemple d'utilisation du module main.py avec les donnees de l'ADEME"


   ## """importation des packages"
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
import ensae_teaching_cs.data

    ##"""importation du module"
import Module.main as main
from Module.main import *
     ##"""importation des donnees"
from ensae_teaching_cs.data import deal_flow_espace_vert_2018_2019
filenames = deal_flow_espace_vert_2018_2019()

df19 = pd.read_excel(filenames[0], decimal=',')
df18 = pd.read_csv(filenames[1], encoding='Windows-1252', sep=';', decimal=',')

#main.plot_geo_time_value(data,variable_of_interest,coordinates,nb_of_periods,titles)
try:
    main.piechart_num(df18.SOUS_DOMAINE, df19.SOUS_DOMAINE,df18.iMontantTotal , df19['iMontant total'], '2018', '2019', 'Investissements par domaine')
    main.piechart_string(df18.SOUS_DOMAINE, df19.SOUS_DOMAINE, df18.DOSSIER_CODE, df19.DOSSIER_CODE, '2018', '2019', "Nombre d'investissements par domaine")
except:
    main.piechart_num(df18['SOUS_DOMAINE'], df19['SOUS_DOMAINE'],df18['iMontantTotal'] , df19['iMontant total'], '2018', '2019', 'Investissements par domaine')
    main.piechart_string(df18['SOUS_DOMAINE'], df19['SOUS_DOMAINE'], df18['DOSSIER_CODE'], df19['DOSSIER_CODE'], '2018', '2019', "Nombre d'investissements par domaine")

main.barplot_variations(df18['iMontantTotal'], df19['iMontant total'],df18.SOUS_DOMAINE,"Evolution des montants investis selon les différents domaines par l'ADEME entre 2018 et 2019 en pourcentage", 'Sous domaines', 'Montant investi',5)

#barplot_variations(a,b,h1,h2,absc,ordo,z,title,df19,df18)

barplot_variations("iMontantTotal","iMontant total","SOUS_DOMAINE","SOUS_DOMAINE","Sous-domaine","Variation en %",7,"Variation en % des montants investis par sous-domaine entre 2019 et 2018",df19,df18)

#plot_geo_time_value(data,variable_of_interest,coordinates,titles,nb_of_periods,title='Titre',plots_per_row=2,plots_per_column=2, scale = 1/3):

lim_metropole = [-5, 10, 41, 52]

df18d = df18.dropna()
df19d = df19.dropna()


df18d_metro = df18d[((df18d.COMMUNE_X >= lim_metropole[0]) & (df18d.COMMUNE_X <= lim_metropole[1]) &
                (df18d.COMMUNE_Y >= lim_metropole[2]) & (df18d.COMMUNE_Y <= lim_metropole[3]))]
    
df19d_metro = df1d[((df19d.COMMUNE_X >= lim_metropole[0]) & (df19d.COMMUNE_X <= lim_metropole[1]) &
                (df19d.COMMUNE_Y >= lim_metropole[2]) & (df19d.COMMUNE_Y <= lim_metropole[3]))]


data = [df18d_metro,df19d_metro,df18d_metro,df19d_metro,df18d_metro,df19d_metro,df18d_metro,df19d_metro] # vecteur contenant les df nettoyés
variable_of_interest = ['iMontantTotal','iMontant total','iMontantTotal','iMontant total','iMontantTotal','iMontant total','iMontantTotal','iMontant total'] # le nom de la colonne contenant la variable que l'on veut présenter
coordinates = [['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y']] # vecteur de vecteur de coordonées
titles = ['France 2018 \n Investissements Verts', 'France 2019 \n Investissements Verts','France','Test','France 2018 \n Investissements Verts', 'France 2019 \n Investissements Verts','France','Test']# vecteur de titres

carte=plot_geo_time_value(data = [df18d_metro,df19d_metro,df18d_metro,df19d_metro,df18d_metro,df19d_metro,df18d_metro,df19d_metro],
                          variable_of_interest = ['iMontantTotal','iMontant total','iMontantTotal','iMontant total','iMontantTotal','iMontant total','iMontantTotal','iMontant total'],
                          
