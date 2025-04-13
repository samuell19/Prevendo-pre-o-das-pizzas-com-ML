# Previsão dos Preços das Pizzas

Este projeto utiliza **Python**, **Streamlit**, **Pandas** e **Scikit-learn** para prever o preço de pizzas com base no seu diâmetro. O modelo de aprendizado de máquina é treinado com dados históricos e permite que o usuário insira o diâmetro de uma pizza para obter o preço previsto.

## Tecnologias Utilizadas

- **Python**: 
- **Streamlit**
- **Pandas**
- **Scikit-learn**

## Como Funciona

1. **Treinamento do Modelo**: 
   - Os dados de treinamento estão no arquivo `pizzas.csv`, que contém o diâmetro e o preço de pizzas.
   - O modelo de regressão linear foi treinado usando skalearn

2. **Interface do Usuário**:
   - A interface foi feita usando streamlit
   - O usuário digita o diâmetro da pizza e terá o resultado

## Como Executar

1. Certifique-se de ter o Python instalado (versão >= 3.13).
2. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt