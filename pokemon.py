#importando a biblioteca requests
import requests

#definindo uma url padrão para os  pokemons da primeira geração
url = 'https://pokeapi.co/api/v2/pokemon/?limit=151'

#fazendo a requisição através da biblioteca requests e transformando em JSON
pokemons = requests.get(url)
nomes_response = pokemons.json()
nomes_response

#buscando todos os nomes dos pokemons e armazenando em uma lista
nomes = []

for pokemom in nomes_response['results']:
  nomes.append(pokemom['name'])

#buscando os pesos de todos os pokemons e armazenando em uma lista
pesos = []

for peso in range(0,151):
  pesos.append(requests.get(nomes_response['results'][peso]['url']).json()['weight'])

#convertendo os pesos para kilos
pesos_kilos = []

for x in pesos:
  pesos_kilos.append(x/10)
#buscando altura de todos os pokemons e armazenando em uma lista
altura = []

for x in range(0,151):
  altura.append(requests.get(nomes_response['results'][x]['url']).json()['height'])

#convertendo altura para metros

altura_metros = []

for x in altura:
  altura_metros.append(x/10)

#Buscando os tipos dos pokemons e colocando em uma lista

tipo1 = []
tipo2 = []


for i in range(0,151):
  tipo1.append(requests.get(nomes_response['results'][i]['url']).json()['types'][0]['type']['name'])

for x in range(0,151):
  try:
    tipo2.append(requests.get(nomes_response['results'][x]['url']).json()['types'][1]['type']['name'])
  except IndexError:
    tipo2.append('None')

# importando biblioteca pandas
import pandas as pd

#criando um dataframe com informações obtidas

df = pd.DataFrame(list(zip(nomes,pesos_kilos,altura_metros,tipo1,tipo2)), columns=['Nome','Pesos em kilos','Altura em metros ','Tipo 1','Tipo 2'])


#salvando o arquivo em extensão csv

df.to_csv('pokemons.csv')
