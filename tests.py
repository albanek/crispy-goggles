# -*- coding: utf-8 -*-


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

from ensae_teaching_cs.data import deal_flow_espace_vert_2018_2019
filenames = deal_flow_espace_vert_2018_2019()


lim_metropole = [-5, 10, 41, 52]
df18 = pd.read_csv(filenames[1], encoding="Windows-1252", sep=";", decimal=',')
df19 = pd.read_excel(filenames[0], decimal=',')


df18 = df18.dropna()
df19 = df19.dropna()


df18_metro = df18[((df18.COMMUNE_X >= lim_metropole[0]) & (df18.COMMUNE_X <= lim_metropole[1]) &
                (df18.COMMUNE_Y >= lim_metropole[2]) & (df18.COMMUNE_Y <= lim_metropole[3]))]
    
df19_metro = df19[((df19.COMMUNE_X >= lim_metropole[0]) & (df19.COMMUNE_X <= lim_metropole[1]) &
                (df19.COMMUNE_Y >= lim_metropole[2]) & (df19.COMMUNE_Y <= lim_metropole[3]))]


data = [df18_metro,df19_metro,df18_metro,df19_metro,df18_metro,df19_metro,df18_metro,df19_metro] # vecteur contenant les df nettoyés
variable_of_interest = ['iMontantTotal','iMontant total','iMontantTotal','iMontant total','iMontantTotal','iMontant total','iMontantTotal','iMontant total'] # le nom de la colonne contenant la variable que l'on veut présenter
coordinates = [['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y'],['COMMUNE_X','COMMUNE_Y']] # vecteur de vecteur de coordonées
titles = ['France 2018 \n Investissements Verts', 'France 2019 \n Investissements Verts','France','Test','France 2018 \n Investissements Verts', 'France 2019 \n Investissements Verts','France','Test']# vecteur de titres

carte=plot_geo_time_value(data = [df18_metro,df19_metro,df18_metro,df19_metro,df18_metro,df19_metro,df18_metro,df19_metro],
                          variable_of_interest = ['iMontantTotal','iMontant total','iMontantTotal','iMontant total','iMontantTotal','iMontant total','iMontantTotal','iMontant total'],
                          

      








