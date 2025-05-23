# -*- coding: utf-8 -*-
"""Mapa de densidade demográfica.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sIK-aSCGOM_65K_EF0iAketblTKfNmQT
"""

#Av1 Modelagem paramétrica e simulações digitais

# equipe: Larissa Rios, Sofia Brêda, Gabriella Carvalho, Maria Fernanda Libório

#instalando
# !pip install geopandas shapely mapclassify libpysal splot esda pysal contextily
# !pip install --upgrade pyshp
# !pip install --upgrade descartes
# !pip install --upgrade fiona

#importando os pacotes que serão utilizados
import pandas as pd
import numpy as np
import zipfile

#para a parte dos gráficos
import matplotlib.pyplot as plt
import seaborn as sns

#dados espaciais
import geopandas as gp

import mapclassify as mc
import contextily as cx

#baixando os arquivos disponibilizados
!wget https://255ribeiro.github.io/curso_python_gis/geo_py/BA_Malha_Preliminar_2022.zip

#Extraindo do arquivo zip
with zipfile.ZipFile("BA_Malha_Preliminar_2022.zip", 'r') as zip_ref:
  zip_ref.extractall("./BA_Malha_Preliminar_2022")

#Carregando GeoJson
df_geo = gp.read_file("./BA_Malha_Preliminar_2022/BA_Malha_Preliminar_2022.json")

#Informações do arquivo
df_geo.shape

df_geo.info()

df_geo.describe()

df_geo.head()

pd.set_option('display.max_columns', None)
df_geo.head()

#Plotagem utilizando o geopandas
df_geo.plot()

fig, ax = plt.subplots(figsize=(6,6))
df_geo.plot(ax=ax, column = "v0001")
fig.show()

fig, ax = plt.subplots(figsize=(6,6))
df_geo.boundary.plot(ax=ax, edgecolor="blue")
fig.show()

fig, ax = plt.subplots(figsize=(6,6))
df_geo.boundary.plot(ax=ax, edgecolor="yellow", lw=.5)
fig.show()

df_geo["v0001"] = df_geo["v0001"].astype(int)
df_geo["v0002"] = df_geo["v0002"].astype(int)
df_geo["v0003"] = df_geo["v0003"].astype(int)
df_geo["v0004"] = df_geo["v0004"].astype(int)
df_geo["v0005"] = df_geo["v0005"].astype(float)
df_geo["v0006"] = df_geo["v0006"].astype(float)
df_geo["v0007"] = df_geo["v0007"].astype(int)

# Gerando novas colunas
df_geo["densidade_pop"] =  df_geo["v0001"]/df_geo["AREA_KM2"]

df_geo.info()

df_geo.describe()

fig, ax = plt.subplots(figsize=(6,6))

df_geo.plot(ax=ax, column = "densidade_pop",
            #  scheme="quantiles",

            legend_kwds={"title": "Habitantes por km²"}
            )

fig, ax = plt.subplots(figsize=(6,6))

df_geo.plot(ax=ax, column = "densidade_pop",
            scheme="quantiles",
            cmap='viridis',
            legend=True,
            legend_kwds={"title": "Habitantes por km²"}
            )

from matplotlib import colors as mcolors

c_list = ["darkred","red","orangered", "salmon"]

c_map = mcolors.ListedColormap(c_list)

fig, ax = plt.subplots(figsize=(6,6))

df_geo.plot(ax=ax, column = "densidade_pop",
             scheme="quantiles",
             cmap=c_map,
             legend=True,
             legend_kwds={"title": "Habitantes por km²"}
             )

c_list = ["#33cccc","#0099cc","#3366cc","#33ccff","#99ccff"]

print(c_list)

c_map = mcolors.ListedColormap(c_list)


fig, ax = plt.subplots(figsize=(6,6))

df_geo.plot(ax=ax, column = "densidade_pop",
             scheme="quantiles",
             cmap=c_map,
             legend=True,
             legend_kwds={"title": "Habitantes por km²"}
             )

fltr = df_geo["NM_MUN"] == "Salvador"
df_geo_ssa = df_geo[fltr]
df_geo_ssa.shape, df_geo.shape

df_geo_ssa.info()

df_geo_ssa.plot()

#crs do geodataframe
df_geo_ssa.crs

#alterando o crs do dataframe para mostrar novo crs
df_geo_ssa = df_geo_ssa.to_crs("EPSG:31984")
df_geo_ssa.crs

# anexando Geojson
with open("SSA_BA_Malha_Preliminar_2022.json" , 'w') as file:
    file.write(df_geo_ssa.to_json())

# GeoJson
df_2 = gp.read_file("SSA_BA_Malha_Preliminar_2022.json")
df_2.info()

df_2.plot()

# Identificando parte indesejada: tipo 01
df_2['coords'] = df_2['geometry'].apply(lambda x: x.representative_point().coords[0])

df_2['coords']

df_2.plot()
for idx, row in df_2.iterrows():
    plt.annotate(text=row['id'], xy=row['coords'],
                 horizontalalignment='center')

# Identificando parte indesejada: tipo 02
df_2['AREA_KM2'].max()

fltr = df_2['AREA_KM2'] == df_2['AREA_KM2'].max()
df_2[fltr].plot()
df_2[fltr].shape, df_2[fltr]["id"].values

# Removendo a parte indesejada
fltr = df_2["id"] != "21881"
df_2 = df_2[fltr]

# mapa
fig, ax = plt.subplots(1)
df_2.plot(ax = ax, column="NM_SUBDIST" ,cmap="cubehelix", legend=True, legend_kwds={'bbox_to_anchor': (1.5, 1)})

# Juntando com o dissolve
df_3 = df_2[['NM_SUBDIST', "v0001",'v0005', "geometry"]]
df_3 = df_3.dissolve(by='NM_SUBDIST', aggfunc='sum', as_index=False)

df_3.head()

fig, ax = plt.subplots(1)
df_3.plot(ax = ax,column="NM_SUBDIST", cmap="cubehelix", legend=True, legend_kwds={'bbox_to_anchor': (1.5, 1)})
plt.xticks(rotation=90) # Rotacionamos valores numéricos no eixo x

# mapas de fundo
fig, ax = plt.subplots(1, figsize=(6,6))
df_2.plot(ax = ax, column="v0001", cmap='flare',legend=True )
cx.add_basemap(ax=ax, crs=df_2.crs)

# Abaixo temos provedores de mapas online da biblioteca contextily
cx.providers

fig, ax = plt.subplots(1, figsize=(6,6))
df_2.plot(ax = ax, column="densidade_pop", cmap='flare',legend=True )
cx.add_basemap(ax=ax, source=cx.providers.CartoDB.Voyager ,  crs=df_2.crs)

alpha = .5
fig, ax = plt.subplots(1, figsize=(6,6))
df_2.plot(ax = ax, column="densidade_pop",
          cmap='OrRd',
          scheme = "quantiles",
          legend=True,
          alpha=alpha,

          )
cx.add_basemap(ax, source=cx.providers.CartoDB.PositronNoLabels, zoom=12, crs=df_2.crs)
cx.add_basemap(ax, source=cx.providers.CartoDB.PositronOnlyLabels, zoom=15, crs=df_2.crs)

# Determinamos um ponto por coordenadas (Terreno Brotas)
from shapely.geometry import Point
# substituimos os valores de latitue e longitude pelos valores do seu ponto
# colocamos pontos para separar os decimais
lat = -12.592998
lon = -38.291159
pt_terreno = Point(lon, lat)

# Sistema de coordenadas
loc_terreno= gp.GeoDataFrame([1], geometry=[pt_terreno], crs="EPSG:4326")

loc_terreno.head()

loc_terreno = loc_terreno.to_crs(df_2.crs)

alpha = 1
fig, ax = plt.subplots()

df_2.plot(ax=ax, column= 'densidade_pop', cmap="flare", alpha = alpha)
loc_terreno.plot(ax=ax)
plt.xticks(rotation=90)

# Geramos uma região de 1km ao redor do ponto do terreno
entorno = loc_terreno.buffer(1000)

# Feição do terreno
fig, ax = plt.subplots()
plt.grid(alpha = .2) # grid no gráfico
df_2.plot(ax=ax, column= 'densidade_pop', cmap="flare")
entorno.plot(ax=ax)

plt.xticks(rotation=90)
fig.show()

# Gerando um geodataframe
fltr = df_2.intersects(entorno[0])
df_4 = df_2[fltr]

# Gráfico
fig, ax = plt.subplots()
fig.suptitle("Densidade populacional do entorno", fontsize=20) # título da figura
# plotagem dos setores censitários
df_4.plot(ax=ax,
          column= "densidade_pop", # coluna a ser plotada
          cmap="flare" # paleta de cores
          )
# plotagem da localização do terreno
loc_terreno.plot(ax=ax,
                 marker= 'o', # tipo de marcador
                 color= 'teal', # cor do marcador
                 markersize= 100 # tamanho do marcador
                 )
# escreve texto no ponto do terreno
ax.annotate("Terreno", # Texto a escrever
            xy= (loc_terreno.iloc[0].geometry.x, loc_terreno.iloc[0].geometry.y), # posição do texto
            xytext=(3, 3), # Deslocamento do texto em relação ao ponto
            textcoords="offset points" # tipo de deslocamento do texto
            )
plt.xticks(rotation=90) # rotacionando textos do eixo x para melhor leitura
ax.ticklabel_format(style='plain') # remove notação científica
#salvando figura
fig.savefig('./entorno.svg')
fig.show()