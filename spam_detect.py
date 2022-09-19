import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
import pickle


with open(r"email_classifier",'rb') as file:
    v,clf = pickle.load(file)

st.title("Email Spam Classifier")

def predict(mail):
    spam = clf.predict([mail])[0]
    if spam:
        st.error("It's a spam email")
    else:
        st.success("It's not a spam email")

mail = st.text_area("Enter the mail")
bt = st.button("Detect", on_click=predict(mail))

