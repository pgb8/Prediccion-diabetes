
import pandas as pd
import streamlit as st
import pickle
import os
from PIL import Image
import base64
import io

# Cargamos el df y el modelo predictivo
os.chdir ('c:\\Users\\polga\\.vscode\\samplerepo\\Proyecto_final\\')
df = pd.read_csv(r"datos\\diabetes_prediction.csv")

with open(r'datos\\gbc_model1.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title = 'Predicción', layout="centered", page_icon="🔬")
st.set_option('deprecation.showPyplotGlobalUse', False)        
st.echo(False) 

# Mostrar logo en sidebar
file = open("img\Recurso_5.png", "rb")
contents = file.read()
img_str = base64.b64encode(contents).decode("utf-8")
buffer = io.BytesIO()
file.close()
img_data = base64.b64decode(img_str)
img = Image.open(io.BytesIO(img_data))
resized_img = img.resize((110, 90))  # x, y
resized_img.save(buffer, format="PNG")
img_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: url('data:image/png;base64,{img_b64}');
                background-repeat: no-repeat;
                padding-top: 50px;
                background-position: 100px 50px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Página donde se ingresan los datos
st.header('Comprueba si tienes diabetes 💉')
st.markdown("Introduzca sus datos:")

# https://www.analyticsvidhya.com/blog/2020/12/deploying-machine-learning-models-using-streamlit-an-introductory-guide-to-model-deployment/
# Crear una función para obtener los datos de entrada del usuario
def obtener_entrada_usuario():
    genero = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])
    edad = st.slider("Edad", 0, 100, 25)
    hipertension = st.selectbox("Hipertensión", ["No", "Sí"])
    enfermedad_corazon = st.selectbox("Enfermedades del corazón", ["No", "Sí"])
    hist_tabaco = st.selectbox("Historial de tabaco", ["Nunca", "Pasado", "Actual"])
    bmi = st.slider("Índice de masa corporal (BMI)", 0.0, 50.0, 24.0)
    hba1c = st.slider("Nivel de HbA1c", 0.0, 9.0, 5.7)
    glucosa_sangre = st.slider("Nivel de glucosa en sangre (mg/dl)", 0, 300, 200)

    #Otorgar datos de entrada
    datos_entrada = [[0, edad, 0, 0, 0, bmi, hba1c, glucosa_sangre]]
    if genero == "Masculino":
        datos_entrada[0][0] = 1
    if hipertension == "Sí":
        datos_entrada[0][2] = 1
    if enfermedad_corazon == "Sí":
        datos_entrada[0][3] = 1
    if hist_tabaco == "Pasado" or hist_tabaco == "Actual":
        datos_entrada[0][4] = 1
    return datos_entrada

# Obtener los datos de entrada del usuario
datos_entrada = obtener_entrada_usuario()

if st.button("Obtener predicción"):
    # Utilizar el modelo para realizar la predicción
    prediccion = model.predict(datos_entrada)

    # Mostrar la predicción en Streamlit
    if prediccion[0] == 0:
        st.success("No tiene diabetes")
    elif prediccion[0] == 1:
        st.error("📢 Tiene diabetes consulte con su médico")

