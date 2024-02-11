import streamlit as st
# from PIL import Image
import pandas as pd
# import pygsheets
# from google.oauth2 import service_account

#########################################################################################################################
# Page Config y estilo
#########################################################################################################################

st.set_page_config(
    page_title="Tablero Estudiantes TEA",
    # page_icon=Image.open("assets/favicon geoagro nuevo-13.png"),
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:mbonelli95@gmail.com?subject=[GitHub]proyecto_estudiantes_tea',
        'Report a bug': "mailto:mbonelli95@gmail.com?subject=[GitHub]proyecto_estudiantes_tea",
        'About': "Desarrollado por Mariano Bonelli"
    }
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#########################################################################################################################
# Título
#########################################################################################################################

st.header('Tablero', anchor=False)

#########################################################################################################################
# Autorización y Lectura del df -> https://www.youtube.com/watch?v=ncnCS8IDZg8
#########################################################################################################################

# scopes = ['https://www.googleapis.com/auth/spreadsheets']

# # Construye el diccionario de credenciales a partir de los secretos
# creds_info = {
#     "type": st.secrets['gcp_service_account']['type'],
#     "project_id": st.secrets['gcp_service_account']['project_id'],
#     "private_key_id": st.secrets['gcp_service_account']['private_key_id'],
#     "private_key": st.secrets['gcp_service_account']['private_key'],
#     "client_email": st.secrets['gcp_service_account']['client_email'],
#     "client_id": st.secrets['gcp_service_account']['client_id'],
#     "auth_uri": st.secrets['gcp_service_account']['auth_uri'],
#     "token_uri": st.secrets['gcp_service_account']['token_uri'],
#     "auth_provider_x509_cert_url": st.secrets['gcp_service_account']['auth_provider_x509_cert_url'],
#     "client_x509_cert_url": st.secrets['gcp_service_account']['client_x509_cert_url']
# }

# credentials = service_account.Credentials.from_service_account_info(creds_info, scopes=scopes)

# # Usa las credenciales para autorizar pygsheets
# gc = pygsheets.authorize(custom_credentials=credentials)

# # Acceso a la hoja de cálculo y carga de datos
# spreadsheet_url = st.secrets['gcp_service_account']['spreadsheet_url']
# sh = gc.open_by_url(spreadsheet_url)
# wks = sh.worksheet_by_title('Hoja 1')
# data = wks.get_all_values(include_tailing_empty=False, include_tailing_empty_rows=False)

# # Conversión de los datos a DataFrame y muestra en Streamlit
# df = pd.DataFrame(data[1:], columns=data[0])  # Asume que la primera fila contiene los encabezados
# st.dataframe(df)

#########################################################################################################################
# Autenticación y conección a google sheets
#########################################################################################################################
# https://docs.streamlit.io/library/api-reference/connections/st.connection
# https://www.youtube.com/watch?v=HwxrXnYVIlU

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Establecer la conexión con Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Leer los datos de la hoja especificada
df = conn.read(worksheet="Hoja 1", ttl=1)

# Limpiar los datos eliminando filas y columnas completamente vacías
df_clean = df.dropna(how='all').dropna(axis=1, how='all')

# # Calcular 'In. totales'
# df_clean['In. totales'] = df_clean['In. justificadas'] + df_clean['In. injustificadas']

# # Permitir al usuario editar los datos en la UI de Streamlit
# df_clean = st.data_editor(
#     df_clean, 
#     column_config={
#         'DNI' : st.column_config.NumberColumn(disabled = True),
#         'Apellido y nombre' : st.column_config.TextColumn(disabled = True),
#         'Año' : st.column_config.SelectboxColumn(options=['1°', '2°', '3°', '4°', '5°', '6°']),
#         'División' : st.column_config.SelectboxColumn(options=['A', 'B', 'C']),
#         'Turno' : st.column_config.SelectboxColumn(options=['Mañana', 'Tarde']),
#         'In. justificadas' : st.column_config.NumberColumn(disabled = True),
#         'In. injustificadas' : st.column_config.NumberColumn(disabled = True),
#         'In. totales' : st.column_config.NumberColumn(disabled = True),
#         'Preceptor' : st.column_config.SelectboxColumn(options=['Juan', 'Tadeo', 'Florencia', 'Paola', 'Lorena', 'Bautista']),
#         'Tutor' : st.column_config.TextColumn(disabled = True),
#         'Teléfono del tutor' : st.column_config.NumberColumn(disabled = True),
#         'Correo electrónico del tutor' : st.column_config.TextColumn(disabled = True),
#         }
#     )

# # El recálculo de 'In. totales' se mueve dentro del condicional del botón
# if st.button('Update Worksheet'):
        
#     # Actualizar la hoja de cálculo con los datos editados
#     conn.update(worksheet='Hoja 1', data=df_clean)
    
#     # Opcionalmente, puedes resetear la conexión o la caché si es necesario
#     conn.reset()
    
#     # Mostrar un mensaje de éxito al usuario
#     st.success('Worksheet Updated!')

st.dataframe(df_clean)