{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b6b59341",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from sklearn.datasets import load_iris\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "093c8e1e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title('Calculadora Mills')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c6a9ef77",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9642857142857143"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('iris.csv')\n",
    "df[\"Species\"] = df[\"Species\"].str.replace(\"Iris-setosa\",'Tesoura Eletrica')\n",
    "df[\"Species\"] = df[\"Species\"].str.replace(\"Iris-virginica\",'Guindaste')\n",
    "df[\"Species\"] = df[\"Species\"].str.replace(\"Iris-versicolor\",'Plataforma elevatoria')\n",
    "df= df.rename(columns = {\"Species\":\"Equipamento\",\n",
    "                             'SepalLengthCm':'Altura máxima',\n",
    "                             'SepalWidthCm':\"Altura mínima\",\n",
    "                             'PetalLengthCm':'Peso máximo',\n",
    "                             'PetalWidthCm':'Peso mínimo'})\n",
    "df = df.drop(columns ='Id')\n",
    "x_teste, x_treino, y_teste, y_treino =  train_test_split(df.drop(columns='Equipamento'),\n",
    "                                                         df.Equipamento,\n",
    "                                                         test_size=0.25, \n",
    "                                                         random_state=42)\n",
    "modelo = KNeighborsClassifier(n_neighbors=3)\n",
    "modelo.fit(x_treino,y_treino)\n",
    "teste = modelo.predict(x_teste)\n",
    "accuracy_score(teste, y_teste)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
