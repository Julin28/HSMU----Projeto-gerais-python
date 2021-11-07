import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('/Users/Adelino/Desktop/julho_py2.csv', sep=';')

def  main():
    st.title('App de avaliacao de transito') 
    st.text('Visualizando os dados iniciais')
    slider = st.slider('Valores', 0, 100)
    st.dataframe(df.tail(slider))

if __name__ == '__main__':
    main()

st.header('Gráfico teste 01')
contagem_gravidade = df['grav_tipo'].value_counts().reset_index().rename(
    columns={'index': 'Gravidade', 'grav_tipo': 'Total_infracoes'})
fig = px.bar(contagem_gravidade,x='Gravidade', y='Total_infracoes')
st.write(fig)
