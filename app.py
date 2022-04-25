from email.mime import image
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='analisis de apps', layout='wide', menu_items=None)
st.title('Apps similares')



col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
with col1:
    st.write("Didi")
    st.image('https://play-lh.googleusercontent.com/qhYA6gj59gBwAsmsHb6WlvKP-sNelNvv_wMyZcWRNfR7dd8OyWW2OLDjyN0YrL8ENFQ=s180-rw')
with col2:
    st.write("Mandados")
    st.image('https://play-lh.googleusercontent.com/8Ja1G5jkOPU_GGIxmXMCaldG8nfD0poRr8FXMQJL4WWIKOaen1wkehhlE6iNKRDGP5Y=s180-rw')
with col3:
    st.write("Picap")
    st.image('https://play-lh.googleusercontent.com/FnvBuLjNcF9l_gggVw5LBChwE_PcHZj4QMO5uZWk-mSiiX0HL-BgMMh5dtxdKmKriw=s180-rw')

with col4:
    st.write("Pibox")
    st.image('https://play-lh.googleusercontent.com/aclsTlMWy7Gybv__CiQngtB7UU-YuFd1yi1dRJCXhdBF-2iglRZo5elNu-0bxZp7Y_g=s180-rw')
with col5:
    st.write("Presgo")
    st.image('https://play-lh.googleusercontent.com/wS5BCxgjqHjLdhMcDppEG9pNpY8pqcA2EHRPWhBpc3ajG_L-5CnyDhep3REWV9VtZQ=s180-rw')
with col6:
    st.write("Yavoy")
    st.image('https://play-lh.googleusercontent.com/cfSlFG_Cay3SbKW1vsyLrWACWlJ2pKNC5XfXuo6mXZN5vPMinW1OI9RRrvgk6Tt_kA=s180-rw')
with col7:
    st.write("Repartidores redy")
    st.image('https://play-lh.googleusercontent.com/1ktgA0uketKH2z9_ckdNiCxsa_wwwuvvo9QD8LwlZFqU2IKrZIWrx1QjJLEWeBHQvC4=s180-rw')
with col8:
    st.write("Va express")
    st.image('https://play-lh.googleusercontent.com/tS-6gmCTAPJ0BsOhb1Vrrmsk59qLOACDk8RwBOczu51FJjF0d_oraaTs7ImdT-iygrU=s180-rw')
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
with col1:
    st.write("Idomi")
    st.image('https://play-lh.googleusercontent.com/6o2nILcrIjiXESNlv3tWJR6aKz8RQNXX9KdLJGtULRzfRN8YRLBYlkJEACvevoQG5pNL=s180-rw')
with col2:
    st.write("Xigo")
    st.image('https://play-lh.googleusercontent.com/sA3xn2XsTO9rRo-0mIFFmr4izyWpI360AC-Q3rlCkHx6BqhSbR-8upwrRuYuqBMyrkmo=s180-rw')
with col3:
    st.write("Ya voy moto")
    st.image('https://play-lh.googleusercontent.com/lYJtF_OPaKa8dkFDTrmk8-iJejRMEPdlI0wBLwxHloYbYmRsK-7yHcii-USJjzVqFmM=s180-rw')
with col4:
    st.write("El mandadito")
    st.image('https://play-lh.googleusercontent.com/ECSF1bJCNykhgO3AFO8_NQo_OS9vWBA_9noqLsxmQ5vWHE_evpmJuWhD-1cpXhJErg=s180-rw')

with col5:
    st.write("Soy Pídelo")
    st.image('https://play-lh.googleusercontent.com/5VgfODjtzWVMAEiU-Vi1usWYXqfC9ct9PJegGuc-bK_YZbCKPza49tc4AqQ6_GYqhzU=s180-rw')
with col6:
    st.write("Repartidores favor")
    st.image('https://play-lh.googleusercontent.com/vZvvcSchUrKn-9os4Vbf3lqcBwkDh3S3jKyHtDCnsszQ6D_pZMQf58UskwKNbJGEeak=s180-rw')
with col7:
    st.write("Wokhy repartidor")
    st.image('https://play-lh.googleusercontent.com/oRxqJLch7Q2hn4rBTo4AO82oDWK8GJFqImwktq17Hw1A0zz6atM8Q45hKLGVosntKFc=s180-rw')
with col8:
    st.write("Ya voy mototaxi")
    st.image('https://play-lh.googleusercontent.com/q0G1BDLvrb4b9WBJcA1BZ0tJjnd7IkJcJ7iaR8u-np-zgDHWlE8XFXPTSx8E0C1tTYo=s180-rw')

st.markdown("---")
st.write('El mercado de las apps en especial de delivery y transporte esta enfocado a los carros, los envíos son realizados por empresas subcontratantes y no directamente con cliente/conductor.')
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.write("# Ventajas globales")
    st.markdown('* Creas una empresa la cual te generara ingresos a futuro')
    st.markdown('* Tendrás la oportunidad de generar como mínimo 5 empleos directos')
    st.markdown("---")
    st.markdown('# Idea')
    st.write('Nosotros como emprendedores buscamos generar ingresos directos y empleos a las personas conductoras de motocicletas que se dedican al mototaxismo, Crear una app de mensajería y que esta cuente con un sistema de transporte para persona y envío de mercancías')

with col2:
    st.write('# Desventajas globales')
    st.markdown('* El mercado ya posee un gran abanico de estas apps') 
    st.markdown('* Es difícil competir teniendo en cuenta la mala gestión de Montería')
    st.markdown("---")
    st.markdown('# Función')
    st.write('Llevar personas a su lugar de destino, enviar mensajería y paquetes de usuarios en tiempo real y que esta pueda ser monitoreada por el usuario que las envía.')
    st.write('El sistema funcionará como una app de suscripción donde las personas mototaxistas solicitan un servicio y el conductor se compromete a llevar a la persona o la mercancía a su lugar de destino')
