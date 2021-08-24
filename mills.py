import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

df = pd.read_csv('Base Mills.csv')

def combustivel(x):
    if x == "Diesel":
        return 0
    elif x == "Elétrico":
        return 1
def alcance(x):
    if x == "Sim":
        return 1
    elif x == "Não":
        return 1
def obstaculo(x):
    if x == "Sim":
        return 1
    elif x == "Não":
        return 0


df['Tipo de motor'] = df['Tipo de motor'].apply(combustivel)
df["Alcance Horizontal"] = df["Alcance Horizontal"].apply(alcance)
df['Obstáculo vertical'] = df['Obstáculo vertical'].apply(obstaculo)

x_teste, x_treino, y_teste, y_treino =  train_test_split(df.drop(columns='Equipamento'),
                                                         df.Equipamento,
                                                         test_size=0.75, 
                                                         random_state=42)

modelo = RandomForestClassifier(criterion="entropy")

modelo.fit(x_treino,y_treino)
teste = modelo.predict(x_teste)
st.write('Acurácia')
st.write(accuracy_score(teste, y_teste))


st.write('''

### Calculadora Mills

''')



st.sidebar.header('Selecione os Parametros')

def valores():
    altura = st.sidebar.slider('Altura de Trabalho (m)', min_value =5, max_value = 55)
    alcance_horizontal = st.sidebar.selectbox('Alcance Horizontal', ['Sim','Não'])
    obstaculo_vertical = st.sidebar.selectbox('Obstáculo',['Sim',"Não"])
    motor = st.sidebar.selectbox('Tipo de motor',['Elétrico','Diesel'])

    parametros = {'Altura de Trabalho (m)':altura,
                    'Tipo de motor':motor,
                    'Alcance Horizontal':alcance_horizontal,
                    'Obstáculo vertical': obstaculo_vertical,
                    }
    resultado = pd.DataFrame(parametros,index=[0])
    resultado['Tipo de motor'] = resultado['Tipo de motor'].apply(combustivel)
    resultado["Alcance Horizontal"] = resultado["Alcance Horizontal"].apply(alcance)
    resultado['Obstáculo vertical'] = resultado['Obstáculo vertical'].apply(obstaculo)
    return resultado

valor_teste = valores()

st.write(modelo.predict(valor_teste))
st.dataframe(pd.DataFrame(modelo.predict_proba(valor_teste), columns = df['Equipamento'].unique()))

if modelo.predict(valor_teste) == "Plataforma de Lança Articulada":
    st.image('./plataforma aerea de lanca articulada.jpg')
    st.write('link')
elif modelo.predict(valor_teste) =='Plataforma de Lança Telescópica':
    st.image('./plataforma aerea de lanca telescopica.png')
    st.write('link')
elif modelo.predict(valor_teste) == 'Plataforma de Trabalho Aéreo':
    st.image('./plataforma aerea de lanca telescopica.png')
    st.write('link')
elif modelo.predict(valor_teste) == 'Plataforma Tesoura a Diesel':
    st.image('./plataforma aerea de lanca telescopica.png')
    st.write('link')
elif modelo.predict(valor_teste) == 'Plataforma Tesoura Diesel':
    st.image('./plataforma aerea de lanca telescopica.png')
    st.write('link')
elif modelo.predict(valor_teste) == 'Plataforma Tesoura Elétrica':
    st.image('./plataforma aerea de lanca telescopica.png')
    st.write('link')
