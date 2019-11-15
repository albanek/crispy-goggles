##Fichier contenant les fonctions de notre module

##Fonction pour faire des pie-charts avec des variables numériques

def piechart_num(a,b,z,w,n,m,name):
    """La fonction piechart_num permet, à partir de 7 variables, d'afficher deux pie charts.
    L'argument a correspond à une vecteur catégorielle d'une année n d'une base de donnée
    L'argument b correspond à une vecteur catégorielle d'une année m d'une base de donnée
    L'argument z correspond à une vecteur quantitative de l'année n d'une base de donnée
    L'argument w correspond à une vecteur quantitative de l'année m d'une base de donnée
    L'argument n correspond à une année donnée
    L'argument m correspond à une autre année donnée, supposée supérieure à n
    L'argument name correspond au nom que l'on veut donner à la représentation"""
    c=a.unique()
    d=b.unique()
    list1=[]
    for v in c:
        print(v)
        x_v=0
        x_v+=sum(z[i] for i in range(len(z)) if a[i]==v)
        print(x_v)
        list1.append(x_v)
    print(list1)
    list2=[]
    for v in d:
        print(v)
        x_v=0
        x_v+=sum(w[i] for i in range(len(w)) if b[i]==v)
        print(x_v)
        list2.append(x_v)
    print(list2)
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=[n, m])
    fig.add_trace(go.Pie(labels=c,values=list1,scalegroup="one", name=n),1,1)
    fig.add_trace(go.Pie(labels=d,values=list2,scalegroup="one", name=m),1,2)
    fig.update_layout(title_text=name)
   

##Fonction pour faire des pie-charts avec des variables catégorielles

def piechart_string(a,b,z,w,n,m,name):
    """La fonction piechart_mon_reuf permet, à partir de 7 variables, d'afficher deux pie charts.
    L'argument a correspond à une vecteur catégorielle d'une année n d'une base de donnée
    L'argument b correspond à une vecteur catégorielle d'une année m d'une base de donnée
    L'argument z correspond à une vecteur de string de l'année n d'une base de donnée
    L'argument w correspond à une vecteur de string de l'année m d'une base de donnée
    L'argument n correspond à une année donnée
    L'argument m correspond à une autre année donnée, supposée supérieure à n
    L'argument name correspond au nom que l'on veut donner à la représentation"""
    c=a.unique()
    d=b.unique()
    list1=[]
    for v in c:
        print(v)
        x_v=0
        for i in range(len(a)):
            if a[i]==v:
                x_v+=1 
        print(x_v)
        list1.append(x_v)
    print(list1)
    list2=[]
    for v in d:
        print(v)
        x_v=0
        for i in range(len(b)):
            if b[i]==v:
                x_v+=1 
        print(x_v)
        list2.append(x_v)
    print(list2)
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=[n, m])
    fig.add_trace(go.Pie(labels=c,values=list1,scalegroup="one", name=n),1,1)
    fig.add_trace(go.Pie(labels=d,values=list2,scalegroup="one", name=m),1,2)
    fig.update_layout(title_text=name)
   
## Fonction pour les cartes

def plot_geo_time_value(data,variable_of_interest,coordinates,nb_of_periods,title='Titre',plots_per_row=2,plots_per_column=2, scale = 1/40):
    
    """ data, variable_of_interest, coordinates déjà présentés
    nb_of_periods : le nombre de cartes que l'on veut représenter
    title : le titre que l'on veut donner aux cartes
    plots_per_row : nb de cartes par ligne
    plots_per_columns : nb de cartes par colonne"""
    
    
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

# La fonction barplot permet de réaliser un histogramme 

def barplot_variations(a,b,f,absc,ordo,z,title):
    """ a = titre de la colonne provenant du dataframe de la valeur pour l'année t
    b = titre de la colonne provenant du dataframe de la valeur pour l'année t+1
    f = titre de la colonne provenant du dataframe des catégories représentées en abscisse
    title = titre du graphique
    absc = nom de l'axe des abcsisses
    ordo = nom de l'axe des ordonnées
    z = nombre de catégories du barplot """

    dft1.groupby("f")["a"].sum()

    dft1sum = (dft1.groupby("f")["b"].sum())

    dftsum = (dft.groupby("f")["a"].sum())
         
    dftsum=pd.DataFrame(dftsum)
    dft1sum=pd.DataFrame(dft1sum)
    dftsum.rename(columns={'a': 'Valeur 1'}, inplace=True)
    dft1sum.rename(columns={'b': 'Valeur 2'}, inplace=True)
    df2=pd.merge(dftsum,dft1sum, on='f' )
    df2['Variation']=(df2['Valeur 2']-df2['Valeur 1'])*100/df2['Valeur 1']
    df2['f'] =  df2.index


    plt.bar(x=np.arange(1,z-1),height=df2['Variation'])
    plt.title("title")
    plt.xlabel("absc")
    plt.ylabel("ordo")
    plt.xticks(np.arange(1,z-1), df2['f'], rotation=90)


