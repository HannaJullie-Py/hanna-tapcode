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




codigo = st.text_input('Digite o código para o tradutor decodificar')
butao = st.button('Decodificar')  
texto = ''
samo = 0
tradu = ''
codigo += ' '


for cod in codigo:
    if cod == ' ':
        samo +1
    if samo < 2:
        tradu = tradu + cod
    if samo == 2:
        if tradu == '  ':
            texto = texto + ' '
        if tradu == '. .':
            texto = texto + 'A'
        if tradu == '. ..':
            texto = texto + 'B'
        tradu = ''
    if samo >3:
        samo = 0
st.caption(texto)
st.write('https://colab.research.google.com/drive/1yPsr3BiYyA4xaDVIogUY7xyFEGsH9Xuc?usp=drive_open#scrollTo=27yaoUGuANAr')
