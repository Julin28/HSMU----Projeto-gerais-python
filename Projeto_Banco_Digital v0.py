#!/usr/bin/env python
# coding: utf-8

# In[75]:


import random


class Conta:
    def __init__(self, numero_ag, numero_conta, nome_prop, renda_mensal, saldo):
        self.numero_ag = numero_ag
        self.numero_conta = numero_conta
        self.nome_prop = nome_prop
        self.renda_mensal = renda_mensal
        self.saldo = saldo
    
    def get_numero_ag(self):
        self.numero_ag = random.randint(100000, 999999)
        return self.numero_ag
    
    def get_numero_conta(self):
        self.numero_conta = random.randint(100, 999)
        return self.numero_conta
    
    def get_deposito(self, valor_deposito):
        self.saldo += valor_deposito
        
    
    def get_saque(self, valor_saque):
        self.saldo -= valor_saque
        
    
    def get_saldo(self):
        return self.saldo
    
    def get_credito(self, valor_credito):
        taxa = valor_credito*0.0199
        valor_maximo_liberado = random.randint(self.renda_mensal, 2*self.renda_mensal)
        if valor_credito > valor_maximo_liberado:
            print(f'O valor exigido está {valor_credito - valor_maximo_liberado} reais acima do disponível. Seu limite é de R${valor_maximo_liberado}')
        else:
            self.saldo -= (valor_credito + taxa)
            print(f'Seu saque de crédito especial foi realizado no valor de {valor_credito + taxa} e seu saldo atual é de {self.saldo}')

    
    


# In[76]:


conta_teste = Conta(0, 0, 'jose', 100, 100)

conta_teste.get_numero_ag()
conta_teste.get_numero_conta()
conta_teste.get_deposito(100)
conta_teste.get_deposito(60)
conta_teste.get_saque(50)


# In[73]:


print(conta_teste.get_saldo())


# In[77]:


conta_teste.get_credito(95)


# In[ ]:





# In[ ]:




