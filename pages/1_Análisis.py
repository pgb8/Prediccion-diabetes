
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')
from PIL import Image
import base64
import io
import plotly.graph_objects as go

os.chdir ('c:\\Users\\polga\\.vscode\\samplerepo\\Proyecto_final\\')
df = pd.read_csv(r"datos\\diabetes_prediction.csv")

st.set_page_config(page_title = 'Análisis', layout="wide", page_icon="📊")
st.set_option('deprecation.showPyplotGlobalUse', False)        
st.echo(False) 

# Mostrar logo en sidebar
file = open("img/Recurso_5.png", "rb")
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

st.header("Análisis de datos 📊")

# Creamos un desglose para visualizar el df
expander = st.expander("Mostrar DataFrame Diabetes")
with expander:
    st.dataframe(df)
    st.write(df.shape)
    st.write("https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset")

st.markdown("")

# Guardamos las variables con los conteos
num_gender = df['gender'].value_counts()
num_hypertens = df['hypertension'].value_counts()
num_heart = df['heart_disease'].value_counts()
num_diabetes = df['diabetes'].value_counts()
num_smoking = df['smoking_history'].value_counts()
bmi = df['bmi']
age = df['age']
hba1c = df['HbA1c_level']
blood_glu = df['blood_glucose_level']

# Creamos tablas
tab1, tab2, tab3, tab4 = st.tabs(["Graficas", "Histplots", "Heatmap", "Relación de las columnas"])

# Tabla 1 Graficas
with tab1:
    col1, col2 = st.columns(2)
    with col1:

        st.write("Diabetes")
        num_diabetes = df['diabetes'].value_counts()
        num_diabetes.plot.bar(figsize=(10, 8), color=['firebrick','limegreen'])
        eje_x = ['No', 'Yes']
        for i, x in enumerate(num_diabetes):
            plt.text(i, x, str(x), ha='center', va='bottom')
        plt.title("Diabetes")
        plt.ylabel('Counts')
        plt.xticks(range(len(num_diabetes.index)), eje_x, rotation= 45)
        st.bar_chart(num_diabetes)

        st.write("Enfermedades cardiacas")
        num_heart = df['heart_disease'].value_counts()
        num_heart.plot.bar(figsize=(10, 8), color=['firebrick','limegreen'])
        eje_x = ['No', 'Yes']
        for j, z in enumerate(num_heart):
            plt.text(j, z, str(z), ha='center', va='bottom')
        plt.title("Heart disease")
        plt.ylabel('Counts')
        plt.xticks(range(len(num_heart.index)), eje_x, rotation= 0)
        st.bar_chart(num_heart)

        st.write("Historial fumador")
        num_smoking = df['smoking_history'].value_counts()
        num_smoking.plot.bar(figsize=(10, 8), color=['tomato', 'royalblue', 'yellowgreen', 'palevioletred', 'gray', 'y'])
        for i, x in enumerate(num_smoking):
            plt.text(i, x, str(x), ha='center', va='bottom')
        plt.title("Smoking Counts")
        plt.ylabel('Counts')
        plt.xlabel('Smoking')
        plt.xticks(rotation= 0)
        st.bar_chart(num_smoking)
        

    
    with col2:

        st.write("Genero")
        num_gender = df['gender'].value_counts()
        num_gender.plot.bar(figsize=(10, 8), color=['tomato', 'royalblue', 'green'])
        for i, v in enumerate(num_gender):
            plt.text(i, v, str(v), ha='center', va='bottom')
        plt.title("Distribution Sex")
        plt.ylabel('Counts')
        plt.xlabel('sex')
        plt.xticks(rotation= 45)
        st.bar_chart(num_gender)

        st.write("Hipertensión")
        num_hypertens = df['hypertension'].value_counts()
        num_hypertens.plot.bar(figsize=(10, 8), color=['firebrick','limegreen'])
        eje_x = ['No', 'Yes']
        for i, x in enumerate(num_hypertens):
            plt.text(i, x, str(x), ha='center', va='bottom')
        plt.title("Hypertension")
        plt.ylabel('Counts')
        plt.xticks(range(len(num_hypertens.index)), eje_x, rotation= 0)
        st.bar_chart(num_hypertens)

        
# Tabla 2 Histplots
with tab2:
    cl1, cl2 = st.columns(2)

    with cl1:
        fig1 = plt.figure()
        sns.histplot(age,kde=True,bins=80, color='royalblue')
        plt.title('Distribución de edades')
        plt.xlabel('Years')
        st.pyplot(fig1)
    
        fig4 = plt.figure()
        sns.histplot(blood_glu, kde=True,bins=20, color='royalblue')
        plt.title('Glucosa en sangre')
        st.pyplot(fig4)


    with cl2:
        fig3 = plt.figure()
        sns.histplot(bmi, kde=True, bins=80, color='royalblue')
        plt.title('BMI')
        plt.xlabel('Values')
        st.pyplot(fig3)

        fig2 = plt.figure()
        sns.histplot(hba1c, kde=True,bins=20, color='royalblue')
        plt.title('HbA1c')
        st.pyplot(fig2)


    # Crea el checkbox para mostrar la tabla
    if st.checkbox("Para visualizar la tabla de valors, haz click"):
        colu1, colu2 =st.columns(2)
        with colu1:
            st.image("img/imc.jpg", width=500) 
        with colu2:
            st.image("img/glucosa.jpg", width=500) 


# Tabla 3 Heatmap
with tab3:

    # Mostrar mapa correlación de variables
    clm1, clm2 = st.columns(2)
    with clm1:
        fig5, ax1 = plt.subplots()
        sns.heatmap(df.corr(),cmap='coolwarm',annot=True)
        st.pyplot(fig5)

    with clm2:
    # Mostrar mapa correlación de variables menos la variable diabetes
        corr = df.corr(method='pearson').sort_values(by='diabetes', axis=0).sort_values(by='diabetes', axis=1)
        mask = np.triu(np.ones_like(corr, dtype=bool))
        fig6, ax2 = plt.subplots()
        sns.heatmap(corr.iloc[0:6,0:6], mask=mask[0:6,0:6], cmap="coolwarm", vmax=1, center=0,
                            square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, fmt=".2f")
        st.pyplot(fig6)

# Tabla 4 Boxplot
with tab4:
    #Mostrar graficas de relaciones entre variables
    colum1, colum2 = st.columns(2)

    with colum1:
        fig7 = plt.figure()
        sns.boxplot(data = df, x = 'diabetes', y = 'age', hue = 'gender')
        ax = plt.gca()
        ax.set_xticklabels(['No', 'Si'], rotation = 0)
        st.pyplot(fig7)

    with colum2:
        fig8 = plt.figure()
        sns.boxplot(data = df, x = 'hypertension', y = 'age', hue = 'gender')
        ax = plt.gca()
        ax.set_xticklabels(['No', 'Si'], rotation = 0)
        st.pyplot(fig8)
    
    colum3, colum4 = st.columns(2)

    with colum3:
            fig9 = plt.figure()
            sns.boxplot(data = df, x = 'smoking_history', y = 'age', hue = 'gender')
            st.pyplot(fig9)

    with colum4:
            fig10 = plt.figure()
            sns.boxplot(data = df, x = 'HbA1c_level', y = 'age', hue = 'gender')
            st.pyplot(fig10)

    colum4, colum5 = st.columns(2)
    with colum4:
            fig11 = plt.figure()
            sns.boxplot(data = df, x = 'blood_glucose_level', y = 'age', hue = 'gender')
            st.pyplot(fig11)

    with colum5:
            fig12 = plt.figure()
            sns.boxplot(data = df, x = 'heart_disease', y = 'age', hue = 'gender')
            st.pyplot(fig12)