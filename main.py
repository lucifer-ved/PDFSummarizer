import streamlit as st
from txtai.pipeline import Summary
from PyPDF2 import PdfReader

choice = st.sidebar.selectbox("Select your choice",["Summarize Text", "Summarize Document"])

@st.cache_resource
def summarize_text(text):
    summary = Summary()
    text = (text)
    result = summary(text)
    return result

# Extract text from PDF file using PyPDF2
def extract_text(filepath):
    with open(filepath,'rb') as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text(page)
    return text

def handle_text():
    st.subheader("Summarize Text")
    input_text = st.text_area("Enter your text")
    if st.button("Summarize Text") and input_text:
        col1, col2 = st.columns([1,1])
        with col1:
            st.markdown("*** Your input text ***")
            st.info(input_text)
        with col2:
            result = summarize_text(input_text)
            st.markdown("*** Your summarize text ***")
            st.success(result)

def handle_document():
    st.subheader("Summarize Document")
    input_file = st.file_uploader("Upload your document", type=["pdf"])
    if st.button("Summarize Document") and input_file:
        col1, col2 = st.columns([1,1])
        with col1:
            st.markdown("*** Extracted text from document ***")
            extracted_text = extract_text()
        with col2:
            result = extract_text(input_file)
            st.markdown("*** Summarize Document ***")
            st.success(result)

if choice == "Summarize Text":
    handle_text()
else:
    handle_document()


