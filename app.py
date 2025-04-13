import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
df= pd.read_csv('pizzas.csv')



modelo= LinearRegression()
x= df[['diametro']]
y= df[['preco']]
modelo.fit(x,y)

st.title("Previsão dos preços das pizzas")
st.write("Esse é um modelo de previsão de preços das pizzas com base no seu diametro.")
st.divider()

diametro= st.number_input("Qual o diametro da pizza?")

if diametro:
    preco_previsto= modelo.predict([[diametro]])[0][0]
    st.write(f"O preço previsto para uma pizza de {diametro} cm é R${preco_previsto:.2f}")