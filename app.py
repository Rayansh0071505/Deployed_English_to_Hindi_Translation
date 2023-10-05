from transformers import pipeline
import streamlit as st

# @st.cache_data(allow_output_mutation=True) 
@st.cache_data()
def load_translation_pipeline():
    return pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")

def main():
    st.title('Translation English-Hindi')
    english_sentence = st.text_area("English Sentence", height=100)

    pipe = load_translation_pipeline()

    if st.button('Translate'):
        translated_text = pipe(english_sentence, max_length=50)[0]['translation_text']

        st.write(translated_text)

if __name__ == "__main__":
    main()
