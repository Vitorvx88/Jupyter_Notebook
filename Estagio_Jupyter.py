#!/usr/bin/env python
# coding: utf-8

# # Primeira questao
# 

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBacked.figure_formats = ['svg']")


# # Bibliotecas
# 
# 

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# # Importando o arquivo de dados do  Google Drive

# In[3]:


#dados = pd.read_csv("C:\Users\Vitor_2\Desktop\Estágio\dados.txt",sep='\t')
url = 'https://drive.google.com/file/d/1Y6VCYmSDjQ9NqQFMTApaX6PydAB6t3Y6/view?usp=sharing'
url2 = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
dados = pd.read_csv(url2, sep = '\t')


# # Imprimindo todo o conteudo do arquivo
# 

# In[4]:


dados


# # Ordenando por Data

# In[5]:


dados.sort_values("dt_pag")


# # Separando a Data de Cada Mês

# In[6]:


Jan=dados[dados['dt_pag'].between('2020-01-01', '2020-01-31')]
Fer=dados[dados['dt_pag'].between('2020-01-01', '2020-02-28')]
Mar=dados[dados['dt_pag'].between('2020-01-01', '2020-03-31')]
Abr=dados[dados['dt_pag'].between('2020-01-01', '2020-04-30')]
Mai=dados[dados['dt_pag'].between('2020-01-01', '2020-05-31')]
Jun=dados[dados['dt_pag'].between('2020-01-01', '2020-06-30')]
Julh=dados[dados['dt_pag'].between('2020-01-01', '2020-07-31')]
Agos=dados[dados['dt_pag'].between('2020-01-01', '2020-08-31')]
Setem=dados[dados['dt_pag'].between('2020-01-01', '2020-09-30')]
Out=dados[dados['dt_pag'].between('2020-01-01', '2020-010-31')]
Nov=dados[dados['dt_pag'].between('2020-01-01', '2020-011-30')]
Dez=dados[dados['dt_pag'].between('2020-01-01', '2020-012-31')]
#print(Jan, Fer, Mar, Abr,  Mai, Jun,Julh, Agos, Setem, Out, Nov, Dez)
#print(Jan)


#REMOVENDO OS 95% DOS VALORES MAIS BAIXO E DEIXANDO APENAS OS 5% MAIORES
Jan = Jan["vl_pag"]
print("Jan percentil:", Jan.quantile(0.95))
Jan = np.where(Jan >119759.45, 119759.45,Jan)
#Jan["vl_pag"] =np.where(Jan["vl_pag"] >119759.45, 119759.45,Jan["vl_pag"])
Fer = Fer["vl_pag"]
print("Fer percentil:",Fer.quantile(0.95))
Fer = np.where(Fer >301876.10, 301876.10,Fer)

Mar = Mar["vl_pag"]
print("Mar percentil:",Mar.quantile(0.95))
Mar = np.where(Mar >211317.90, 211317.90,Mar)

Abr = Abr["vl_pag"]
print("Abr percentil:",Abr.quantile(0.95))
Abr = np.where(Abr >221152.42, 221152.42,Abr)

Mai = Mai["vl_pag"]
print("Mai percentil:",Mai.quantile(0.95))
Mai = np.where(Mai >221679.91, 221679.91,Mai)

Jun = Jun["vl_pag"]
print("Jun percentil:",Jun.quantile(0.95))
Jun = np.where(Jun >221071.27, 221071.27,Jun)

Julh = Julh["vl_pag"]
print("Julh percentil:",Julh.quantile(0.95))
Julh = np.where(Julh >217839.06, 217839.06,Julh)

Agos = Agos["vl_pag"]
print("Agos percentil:",Agos.quantile(0.95))
Agos = np.where(Agos >205873.59, 205873.59,Agos)

Setem = Setem["vl_pag"]
print("Setem percentil:",Setem.quantile(0.95))
Setem = np.where(Setem >211618.70, 211618.70,Setem)

Out = Out["vl_pag"]
print("Out percentil:",Out.quantile(0.95))
Out = np.where(Out >119759.45, 119759.45,Out)

Nov = Nov["vl_pag"]
print("Nov percentil:",Nov.quantile(0.95))
Nov = np.where(Nov >119759.45, 119759.45,Nov)

Dez = Dez["vl_pag"]
print("Dez percentil:",Dez.quantile(0.95))
Dez = np.where(Dez >119759.45, 119759.45,Dez)

#ARMAZENANDO TODOS OS MESES EM UMA UNICA VARIAVEL
Ano = [Jan,Fer,Mar,Abr,Mai,Jun,Julh,Agos,Setem,Out,Nov,Dez]


# # Gerando o Diagrama de Caixa

# In[7]:


plt.boxplot(Ano, showfliers = True)
plt.xticks([],[])
plt.show()


# In[8]:


sns.boxplot(data = Ano)
plt.xticks([],[])
plt.show()


# # 

# # 

# # Terceira questão
# 

# # Media
# 

# In[17]:


valor = dados['vl_pag'].mean()
print("Media dos valores pagos:" , valor)
print(" ")
dias = dados['dias_para_pagamento'].mean()
print("Media dos dias:", dias)


# # Mediana

# In[18]:


valor = dados['vl_pag'].median()
print("Mediana dos valores pagos:" , valor)
print(" ")
dias = dados['dias_para_pagamento'].median()
print("Mediana dos dias:", dias)


# # Quantil

# In[21]:


valor = dados['vl_pag'].quantile()
print("Quantil dos valores pagos:" , valor)
print(" ")
dias = dados['dias_para_pagamento'].quantile()
print("Quantil dos dias:", dias)

print(" ")
valor = dados['vl_pag'].quantile(q=0.25)
print("Quantil dos valores pagos com 25%:" , valor)
print(" ")
dias = dados['dias_para_pagamento'].quantile(q=0.25)
print("Quantil dos dias com 25%:", dias)


# # Moda
# 

# In[22]:


valor = dados['vl_pag'].mode()
print("Moda dos valores pagos:" , valor)
print(" ")
dias = dados['dias_para_pagamento'].mode()
print("Moda dos dias:", dias)


# # Amplitude

# In[24]:


valor = (dados['vl_pag'].max() - dados['vl_pag'].min())
print("Amplitude dos valores pagos:" , valor)

dias = (dados['dias_para_pagamento'].max() - dados['dias_para_pagamento'].min())
print("Moda dos dias:", dias)


# # Variância
# 

# In[25]:


valor = dados['vl_pag'].var()
print("Variancia dos valores pagos:" , valor)
print(" ")
dias = dados['dias_para_pagamento'].var()
print("Variancia dos dias:", dias)


# # Desvio Padrão
# 

# In[26]:


valor = dados['vl_pag'].std()
print("Desvio Padrao dos valores pagos:" , valor)
print(" ")
dias = dados['dias_para_pagamento'].std()
print("Desvio Padrao dos dias:", dias)


# # Desvio absoluto
# 

# In[27]:


valor = dados['vl_pag'].mad()
print("Desvio absoluto dos valores pagos:" , valor)
print(" ")
dias = dados['dias_para_pagamento'].mad()
print("Desvio absoluto dos dias:", dias)


# # Covariancia

# In[28]:


print(dados.cov())


# In[29]:


print(dados.corr())


# In[ ]:




