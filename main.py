import streamlit as st
import pickle
st.header('Форма диагностики')
st.subheader('Заполните следующие пункты:')
age = st.slider('Возраст', 0, 100)
age_in_days = age * 365
sex = st.selectbox('Пол', ['м', 'ж'])
if sex == 'м':
    sex = 1
if sex == 'ж':
    sex = 2
height = st.slider('Рост', 0, 250)
weight = st.slider('Вес', 0, 250)
ap_hi = st.slider('Верхнее давление', 0, 250)
ap_lo = st.slider('Нижнее давление', 0, 250)
cholesterol = st.selectbox('Уровень холестерина', [1, 2, 3])
gluc = st.selectbox('Уровень глюкозы', [1, 2, 3])
smoke = int(st.checkbox ('Вы курите?'))
alco = int(st.checkbox ('Вы употребляете алкоголь?'))
active = int(st.checkbox ('Вы занимаетесь физической активностью?'))
def load():
    with open('model.pcl', 'rb') as fid:
        return pickle.load(fid)
model = load()
y_pr = model.predict_proba([[age, sex, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]])[:,1]
st.write(y_pr)
