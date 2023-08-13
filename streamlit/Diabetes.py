
import streamlit as st
import plotly.express as px
import pandas as pd
import os
from PIL import Image
import base64
import io
import warnings
warnings.filterwarnings('ignore')

# Configurar visualización
st.set_page_config(page_title = 'Diabetes', layout="centered", page_icon="🩺")
st.set_option('deprecation.showPyplotGlobalUse', False)        
st.echo(False)  

# Cargar csv
os.chdir ('c:\\Users\\polga\\.vscode\\samplerepo\\Proyecto_final\\')
df = pd.read_csv(r"datos\\diabetes_prediction.csv")

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




#Mostrar pag

st.header("¿Qué es la diabetes?")

st.markdown("")
st.markdown("")

# Crea columnas
c1, c2 = st.columns(2)
with c1:
    st.write("- Enfermedad crónica")
    st.write("- Pancreas no produce suficiente insulina")
    st.write("- Puede causar problemas de salud graves.")
    c3, c4 = st.columns( [0.4, 0.6])
    with c3:
        st.write("- Hay 3 tipos:")
    with c4:
        st.write("")
        st.write("")
        st.write("- Tipo1: niños/adolescentes")
        st.write("- Tipo2: adultos")
        st.write("- Tipo3: embarazo")
    st.write("- No hay cura")


with c2:
#Video
    st.video("https://www.youtube.com/watch?v=ZNSgHt5C-pw")

#Link
    st.write("URL: https://www.youtube.com/watch?v=ZNSgHt5C-pw")

st.markdown("")


st.header("Datos a nivel mundial")

# Mostrar PowerBi
power_bi_iframe_code='<iframe title="powerbi_diabetes_final" width="1140" height="700" src="https://app.powerbi.com/reportEmbed?reportId=f8462a55-224c-4b67-a6f4-6561c73b98c0&autoAuth=true&ctid=8aebddb6-3418-43a1-a255-b964186ecc64" frameborder="0" allowFullScreen="true"></iframe>'
st.markdown("""<center>{}</center>""".format(power_bi_iframe_code), unsafe_allow_html=True)

#Mostrar factores de risgo con img
st.header("Factores de riesgo")

st.image("img/risk-factor.jpg", width=600) 