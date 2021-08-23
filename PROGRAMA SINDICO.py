#!/usr/bin/env python
# coding: utf-8

# In[15]:


chapas = {'Azul': 0, 'Amarelo': 0, 'Vermelho': 0, 'Nulo': 0, 'Branco': 0}

print("""Para Chapa Azul, digite 01 \n
Para Chapa Amarela, digite 02 \n
Para Chapa Vermelho, digite 03 \n
Para Chapa Nulo, digite 04 \n
Para Chapa Branco, digite 05 \n
                 """)


for number in range(0, 5):
    voto = input('Escolha seu voto: \n')
    if voto == '01':
        chapas['Azul'] += 1
    elif voto == '02':
        chapas['Amarelo'] +=1
    elif voto == '03':
        chapas['Vermelho'] +=1
    elif voto == '04':
        chapas['Nulo'] +=1
    elif voto == '05':
        chapas['Branco'] +=1
        

max_key = max(chapas, key=chapas.get)

total_votos = 5
lista_votos = list(chapas.values())

for i in range(len(lista_votos)):
    lista_votos[i] = lista_votos[i]/total_votos


    
print(f'O resultado final da eleição foi de {chapas}',
      f'A chapa vencedora foi a {max_key}',
      f'A distribuição de votos foi de {lista_votos}', sep='\n')

        


# 

# In[ ]:




