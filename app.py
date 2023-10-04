from transformers import pipeline
import streamlit as st

# Load the translation pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")

def main():
    st.title('Translation English-Hindi')
    english_sentence = st.text_area("English Sentence", height=100)
    if st.button('Translate'):
        translated_text = pipe(english_sentence, max_length=50)[0]['translation_text']

        st.write(translated_text)

if __name__ == "__main__":
    main()
