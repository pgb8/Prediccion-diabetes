
import streamlit as st
import os
import pandas as pd
from PIL import Image
import base64
import io


os.chdir ('c:\\Users\\polga\\.vscode\\samplerepo\\Proyecto_final\\')
df = pd.read_csv(r"datos\\diabetes_prediction.csv")

st.set_page_config(page_title = 'Machine Learning', layout="centered", page_icon="🤖")

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

st.header("Machine Learning" "🤖")

st.markdown("----")

# Mostramos captura de pantalla del df y el resultado del modelo aplicado
st.image("img/categoricas.png")

st.markdown("")

st.image("img/train_models.png")

st.markdown("")

st.image("img/test.png")