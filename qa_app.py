import streamlit as st
from transformers import pipeline

# ===== Load the model =====
# Change this path to your fine-tuned model folder
MODEL_PATH = "./distilbert-qa-model"

# Load QA pipeline
qa_pipeline = pipeline("question-answering", model=MODEL_PATH, tokenizer=MODEL_PATH, framework="pt")

# ===== Streamlit App =====
st.set_page_config(page_title="Question Answering App", layout="centered")

st.title("🤖 Question Answering with Transformers")

st.markdown("""
This is a simple demo app for **extractive Question Answering**.
Provide a passage (context) and a question, and the model will return the most likely answer.
""")

# Input fields
context = st.text_area("📄 Enter context passage:", height=200, placeholder="Paste your paragraph here...")
question = st.text_input("❓ Enter your question:", placeholder="Type your question here...")

# Run inference
if st.button("Get Answer"):
    if context.strip() and question.strip():
        with st.spinner("Thinking..."):
            result = qa_pipeline(question=question, context=context)
        st.success("✅ Answer found!")
        st.write(f"**Answer:** {result['answer']}")
        st.write(f"**Confidence Score:** {result['score']:.4f}")
        st.write(f"**Answer Start:** {result['start']} | **End:** {result['end']}")
    else:
        st.warning("Please provide both a context passage and a question.")

# Footer
st.markdown("---")
st.markdown("Built with [Streamlit](https://streamlit.io) and [Hugging Face Transformers](https://huggingface.co/).")
