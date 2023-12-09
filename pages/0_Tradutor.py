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
codigo = st.text_input('Digite o código para o tradutor decodificar')
for cod1 in codigo:
  abc.append(cod1)
  texto = texto + tradu
  if codigo == '  ':
    tradu = ' '
  if codigo == '. .':
    tradu = abc[1]
  if codigo == '. ..':
    tradu = abc[2]
