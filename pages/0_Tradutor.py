import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config('Tap Code Translate', page_icon='👩‍💻')
st.header('Tap Code Translate', divider= 'rainbow')

code = ['.','..','...','....','.....', 'print']
code1 = ['.','..','...','....','.....', 'print']
codem = ['']
abc = [' ','A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

codu = ''
codi = ''
i = 0
abc2 =['. .','. ..','. ...','. ....','. .....','.. .','.. ..','.. ...','.. ....','.. .....','... .','... ..','... ...','... ....', '... .....','.... .','.... ..','.... ...','.... ....', '.... .....','..... .','..... ..', '..... ...','..... ....','..... .....']
lista = ['. .','. ..','. ...','. ....','. .....','.. .','.. ..','.. ...','.. ....','.. .....','... .','... ..','... ...','... ....', '... .....','.... .','.... ..','.... ...','.... ....', '.... .....','..... .','..... ..', '..... ...','..... ....','..... .....']
bra = [' ']




codigo = st.text_area('Digite o código para o tradutor decodificar')
butao = st.button('Decodificar')  
texto = ''
samo = 0
tradu = ''
codigo += ' '


for cod in codigo:
    if samo == ' ':
        samo += 1
    if samo < 2:
        tradu = tradu + cod
    if samo == 2:
        if tradu == '. .':
            texto = texto + 'A'
        if tradu == '. ..':
            texto = texto + 'B'
        tradu = ''
        soma = 0
if butao:
    st.write(texto)
