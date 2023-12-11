import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config('Tap Code Translate', page_icon='👩‍💻')
st.header('Tap Code Translate', divider= 'rainbow')
st.subheader(':green[Utilize o alfabeto para escrever o seu código!]')
st.image('https://www.cachesleuth.com/images/tap/tapcode.png')
st.title('Traduzir de Tap Code para palavras')
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
codigo += '  '


for cod in codigo:
    if cod == ' ':
        samo +=1
    if cod == '/':
        texto = texto + '  '
    if samo < 2:
        tradu = tradu + cod
    if samo == 2:
        if tradu == '. .':
            texto = texto + 'A'
        if tradu == '. ..':
            texto = texto + 'B'
        if tradu == '. ...':
            texto = texto + 'C'
        if tradu == '. ....':
            texto =  texto + 'D'
        if tradu == '. .....':
            texto = texto + 'E'
        if tradu == '.. .':
            texto = texto + 'F'
        if tradu == '.. ..':
            texto = texto + 'G'
        if tradu == '.. ...':
            texto = texto + 'H'
        if tradu == '.. ....':
            texto = texto + 'I'
        if tradu == '.. .....':
            texto = texto + 'J'
        if tradu == '... .':
            texto = texto + 'L'
        if tradu == '... ..':
            texto = texto + 'M'
        if tradu == '... ...':
            texto = texto + 'N'
        if tradu == '... ....':
            texto = texto + 'O'
        if tradu == '... .....':
            texto = texto + 'P'
        if tradu == '.... .':
            texto = texto + 'Q'
        if tradu == '.... ..':
            texto = texto + 'R'
        if tradu == '.... ...':
            texto = texto + 'S'
        if tradu == '.... ....':
            texto = texto + 'T'
        if tradu == '.... .....':
            texto = texto + 'U'
        if tradu == '..... .':
            texto = texto + 'V'
        if tradu == '..... ..':
            texto = texto + 'W'
        if tradu == '..... ...':
            texto = texto + 'X'
        if tradu == '..... ....':
            texto = texto + 'Y'
        if tradu == '..... .....':
            texto = texto + 'Z'
        tradu = ''
    if samo ==3:
        samo = 0
if butao:
    with st.spinner('Carregando...'):
        time.sleep(5)
    st.caption(f':violet[{texto}]')

st.divider()
