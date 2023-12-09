import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config('Tap Code Translate', page_icon='👩‍💻')
st.header('Tap Code Translate', divider= 'rainbow')

code = ['.','..','...','....','.....', 'print']
code1 = ['.','..','...','....','.....', 'print']
codem = ['']
abc = [' ','A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
tradu = ''
texto = ''
codu = ''
codi = ''
i = 0
abc2 =['. .','. ..','. ...','. ....','. .....','.. .','.. ..','.. ...','.. ....','.. .....','... .','... ..','... ...','... ....', '... .....','.... .','.... ..','.... ...','.... ....', '.... .....','..... .','..... ..', '..... ...','..... ....','..... .....']
lista = ['. .','. ..','. ...','. ....','. .....','.. .','.. ..','.. ...','.. ....','.. .....','... .','... ..','... ...','... ....', '... .....','.... .','.... ..','.... ...','.... ....', '.... .....','..... .','..... ..', '..... ...','..... ....','..... .....']
bra = [' ']
codigo = ''
for i in range(1,241):
    codigo = st.text_area('Digite o código para o tradutor decodificar', key='str')
    butao = st.button('Decodificar')   
    for cod1 in codigo:
        abc.append(cod1)
        texto = texto + tradu
        if cod1 == " " + " ":
            tradu = abc[0]
        if cod1 == ". .":
            tradu = abc[1]
        if cod1 == ". ..":
            tradu = abc[2]
        if butao:
            st.write(texto)
