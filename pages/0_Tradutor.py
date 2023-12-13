import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config('Tap Code Translate', page_icon='👩‍💻')
st.header('Tap Code Translate', divider= 'rainbow')
st.subheader(':green[Utilize o alfabeto para escrever o seu código!]')
st.divider()
col1, col2, col3 = st.columns(3)
with col2:
    st.title('Alfabeto')
    st.image('https://www.cachesleuth.com/images/tap/tapcode.png')
st.divider()
st.title('Traduzir de Tap Code para palavras')
code = ['.','..','...','....','.....', 'print']
code1 = ['.','..','...','....','.....', 'print']
codem = ['']
abc = [' ','A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

codu = ''
codi = ''
i = 0
abc2 =['. .','. ..','. ...','. ....','. .....','.. .','.. ..','.. ...','.. ....','.. .....','... .','... ..','... ...','... ....', '... .....','.... .','.... ..','.... ...','.... ....', '.... .....','..... .','..... ..', '..... ...','..... ....','..... .....']
lista = ['. . ','. .. ','. ... ','. .... ','. ..... ','.. . ','.. .. ','.. ... ','.. .... ','.. ..... ','... . ','... .. ','... ... ','... .... ', '... ..... ','.... . ','.... .. ','.... ... ','.... .... ', '.... ..... ','..... . ','..... .. ', '..... ... ','..... .... ','..... ..... ']
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
    if samo < 2:
        tradu = tradu + cod
    if cod == '/':
        texto = texto + ' '
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

st.title('Traduzir de palavras para Tap Code')
frase = st.text_input('Digite o código para o tradutor codificar')
botao = st.button('Codificar')  
for letra in frase:
    i = 0
    lista.append(letra)
    if letra == ' ':
        codu = '/' + ' '
        space = True
    if letra == 'A':
        codu = lista[0]
    if letra == 'B':
        codu = lista[1]
    if letra == 'C':
        codu = lista[2]
    if letra == 'D':
        codu = lista[3]
    if letra == 'E':
        codu = lista[4]
    if letra == 'F':
        codu = lista[5]
    if letra == 'G':
        codu = lista[6]
    if letra == 'H':
        codu = lista[7]
    if letra == 'I':
        codu = lista[8]
    if letra == 'J':
        codu = lista[9]
    if letra == 'L':
        codu = lista[10]
    if letra == 'M':
        codu = lista[11]
    if letra == 'N':
        codu = lista[12]
    if letra == 'O':
        codu = lista[13] 
    if letra == 'P':
        codu = lista[14]
    if letra == 'Q':
        codu = lista[15]
    if letra == 'R':
        codu = lista[16]
    if letra == 'S':
        codu = lista[17]
    if letra == 'T':
        codu = lista[18]
    if letra == 'U':
        codu = lista[19]
    if letra == 'V':
        codu = lista[20]
    if letra == 'W':
        codu = lista[21] 
    if letra == 'X':
        codu = lista[22]
    if letra == 'Y':
        codu = lista[23]
    if letra == 'Z':
        codu = lista[24] 
    if space == False:
        codi = codi + codu + ' '
    if space == True:
        codi = codi + codu

st.text(codi)
st.divider()
