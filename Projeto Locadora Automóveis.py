#!/usr/bin/env python
# coding: utf-8

# In[132]:


#VARIAVEIS

aluguel_carro_diaria = {'Economico': 50.00, 'Sedan': 70.00, 'SUV': 100.00}

seguro_carro_diaria = 20.00

taxa_admin = 75.00

itens_extras = {'GPS': 12.00, 'Bebê conforto': 15.00, 'Cadeira de bebê': 15.00, 'Assento de elevação': 15.00}

soma_itens_extras = 0

chaves_itens = []
valores_itens = []


#INPUT DE DADOS

qtdd_diarias = int(input('Insira aqui o numero de diarias: \n'))

tipo_carro = input(f'Selecione o tipo de carro que deseja usar: {aluguel_carro_diaria} \n')

for i in itens_extras:
    pergunta = print(f'Voce deseja levar {i}? Custa R${itens_extras[i]}')
    resposta = input('Digite sim ou nao: \n')
    if resposta == 'sim':
        soma_itens_extras += itens_extras[i]
        chaves_itens.append(i)
        valores_itens.append(itens_extras[i])
    
new_dict = dict(zip(chaves_itens, valores_itens))
    

#CALCULO FINAL 



def valor_total(valor):
    if qtdd_diarias >= 7:
        aluguel_c_disct = 0.75*aluguel_carro_diaria[tipo_carro]       
    soma_total = qtdd_diarias*(aluguel_c_disct + seguro_carro_diaria + soma_itens_extras) + taxa_admin
    return soma_total


valor_total(qtdd_diarias)

   


# In[134]:


#TRANSFORMAR EM DOCUMENTO

def argumentos_finais():
    print(f'Tipo de carro selecionado: {tipo_carro} \n==========')
    print(f'Diárias: {qtdd_diarias} \n==========')
    print(f'Custos com carro: {qtdd_diarias} X {aluguel_carro_diaria[tipo_carro]} = {qtdd_diarias*aluguel_carro_diaria[tipo_carro]} \n==========')

    for i in new_dict:
        print(f'Custos com {i}: {qtdd_diarias} X {new_dict[i]} = {qtdd_diarias*new_dict[i]} \n==========')

    print(f'Custos com seguro: {qtdd_diarias} X {seguro_carro_diaria} = {qtdd_diarias*seguro_carro_diaria} \n==========')
    print(f'Valor taxa administrativa: {taxa_admin} \n==========')
    print(f'Valor total pela locação: {valor_total(qtdd_diarias)} \n==========')
    
argumentos_finais()


# In[146]:


def get_nota_fiscal():
    extras = [f'Custos com {i}: {qtdd_diarias} X {new_dict[i]} = {qtdd_diarias*new_dict[i]}' for i in new_dict]
    nota_fiscal_extras = '\n'.join(extras)
    
    nota_fiscal = f"""
Tipo de carro selecionado: {tipo_carro}
============
Diárias: {qtdd_diarias}
============
Custos com carro: {qtdd_diarias} X {aluguel_carro_diaria[tipo_carro]} = {qtdd_diarias*aluguel_carro_diaria[tipo_carro]} 
============
{nota_fiscal_extras}
============
Custos com seguro: {qtdd_diarias} X {seguro_carro_diaria} = {qtdd_diarias*seguro_carro_diaria}
============
Valor taxa administrativa: {taxa_admin}
============
Valor total pela locação: {valor_total(qtdd_diarias)}
    """
    return nota_fiscal

print(get_nota_fiscal())


# In[149]:


with open("teste.txt", "w") as file:
    file.write(get_nota_fiscal())


# In[ ]:




