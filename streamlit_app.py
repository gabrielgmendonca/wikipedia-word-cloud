import streamlit as st
import pandas as pd
import wikipedia as wiki
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk

nltk.download('stopwords')

wiki.set_lang('pt')
title = st.text_input('Artigo da Wikipédia', 'Roda de samba')
text = wiki.page(title).content
extra_sw = []

custom_sw = nltk.corpus.stopwords.words('portuguese')
custom_sw += title.split()
custom_sw += extra_sw
wordcloud = WordCloud(stopwords=custom_sw).generate(text)

fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
# plt.show()
st.pyplot(fig)
