import streamlit as st
import pandas as pd
import wikipedia as wiki
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk import tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

nltk.download('stopwords')
nltk.download('rslp')
nltk.download('punkt')

wiki.set_lang('pt')
title = st.text_input('Artigo da Wikipédia', 'Roda de samba')
extra_sw = st.text_input('Stop words adicionais', '')

text = wiki.page(title).content

text = tokenize.word_tokenize(text, language='portuguese')
custom_sw = nltk.corpus.stopwords.words('portuguese')
custom_sw += title.split()
custom_sw += extra_sw

text = [w for w in text if w not in custom_sw]

if st.checkbox('Usar apenas radicais?'):
  text = [RSLPStemmer().stem(w) for w in text]
  
wordcloud = WordCloud().generate(' '.join(text))

fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)
