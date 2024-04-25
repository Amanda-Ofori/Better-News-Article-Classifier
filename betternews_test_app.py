import streamlit as st
from betternews_testmodel import load_models_and_vectorizer, make_prediction, preprocess_article_text
import fitz  # PyMuPDF

# Specify the directory name where the models are stored
models_dir = "models"

# Load the vectorizer and trained models
vectorizer, trained_models = load_models_and_vectorizer(models_dir)
print("Vectorizer and models loaded successfully.")

def extract_text_from_pdf(pdf_file):
    # Open the PDF from the uploaded file object
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Streamlit app
def main():
    st.title("Better-News Article Classifier")
    
     # Link to MLflow UI
    st.markdown("View the [MLflow tracking UI](http://localhost:5000)", unsafe_allow_html=True)


    # Toggle between text input and file upload
    input_option = st.radio("Choose input method:", ("Enter text", "Upload PDF"))

    if input_option == "Enter text":
        article_text = st.text_area("Enter the text of a news article:")
    elif input_option == "Upload PDF":
        pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
        article_text = ""
        if pdf_file is not None:
            article_text = extract_text_from_pdf(pdf_file)

    if st.button("Classify"):
        if not article_text:
            st.warning("Please enter some text or upload a PDF.")
        else:
            # Preprocess the input text
            processed_article_text = preprocess_article_text(article_text)
            # Make prediction
            prediction = make_prediction(processed_article_text)
            st.success(f"The predicted category is: {prediction}")

if __name__ == "__main__":
    main()


