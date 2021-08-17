#!/usr/bin/env python
# coding: utf-8

# In[9]:


numero_placa = input('Insira o número da placa: \n')
velocidade = int(input('Insira aqui a velocidade do carro: \n'))
limite_da_via = int(input('Insira aqui o limite da via: \n'))

if velocidade >= (limite_da_via + (0.51*limite_da_via)):
    print(f'Carro placa {numero_placa} cometeu infração gravíssima. Pague R$ 880,41')
elif velocidade >= (limite_da_via + (0.21*limite_da_via)):
    print(f'Carro placa {numero_placa} cometeu infração grave. Pague R$ 195,23')
elif velocidade > limite_da_via:
    print(f'Carro placa {numero_placa} cometeu infração media. Pague R$ 130,16')
else:
    print(f'Carro placa {numero_placa} não cometeu infração')


# In[ ]:





# In[ ]:




