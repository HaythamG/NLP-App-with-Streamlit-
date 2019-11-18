#pip install streamlit
import streamlit as st

#NLP Pkgs
import spacy
import re
from textblob import TextBlob
from spacy import displacy
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator










# Tokenisation Model
def text_analyzer(my_text):
    nlp =  spacy.load("en_core_web_sm")
    docx = nlp(my_text) 
    filtered_sent=[]
    for word in docx:
        if word.text in nlp.Defaults.stop_words:
            continue
        if word.is_punct:
            continue
            
        filtered_sent.append(word)
    allData = [('"Token"={}/"Lemma"={}/"POS"={}'.format(token.text,token.lemma_,token.pos_))for token in filtered_sent] 
    print(filtered_sent)
    return allData 

# Entities Model
def Entities(my_text):
    nlp =  spacy.load("en_core_web_sm")
    nytimes= nlp(my_text)
    entities=[(i, i.label_, i.label) for i in nytimes.ents]
    allData = ['"Entities":{}'.format(entities)]
    return allData



#Pkgs


def main():
	""" NLP App with Streamlit """
	st.title("NLPT With Streamlit ")
	st.subheader(" This App is for applied some concept in NLP ")

	# Tokenisation Interface  
	if st.checkbox(" Show Tokens and Lemma "):
		st.subheader(" Tokenize Your Text ")
		message=st.text_area(" Entre Your Text ","  ")
		if st.button("Analyse"):
			nlp_result = text_analyzer(message)
			st.json(nlp_result)

	# Named Entity Interface 
	if st.checkbox(" Show Named Entities "):
		st.subheader(" Extract Entities from Your Text ")
		message=st.text_area(" Entre Your Text ","  ")
		if st.button("Extract"):
			nlp_result = Entities(message)
			st.json(nlp_result)

	# Sentiment Analysis
	if st.checkbox("Show Sentiment Analysis"):
		st.subheader("Analyse Your Text")

		message = st.text_area("Enter Text","Type Here ")
		if st.button("Analyze"):
			blob = TextBlob(message)
			result_sentiment = blob.sentiment
			st.success(result_sentiment)

	
	
	#WordCloud
	
	if st.checkbox("WordCloud"):
			raw_text = st.text_area("Enter News Here","Type Here")
			c_text = raw_text
			if st.button("Extract"):
				wordcloud = WordCloud().generate(c_text)
				plt.imshow(wordcloud,interpolation='bilinear')
				plt.axis("off")
				st.pyplot()



				


	# Text Summarization 

if __name__ =='__main__':
	main()
