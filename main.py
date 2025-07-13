import streamlit as st
from app.rag_pipeline import load_and_chunk_pdf, embed_and_store, create_qa_chain
from app.utils import save_uploaded_file

st.set_page_config(page_title="Smart Doc QA Bot", layout="centered")
st.title("📄 Smart Document QA Bot")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file:
    file_path = save_uploaded_file(uploaded_file)
    with st.spinner("🔍 Processing document..."):
        chunks = load_and_chunk_pdf(file_path)
        vs = embed_and_store(chunks)
        qa = create_qa_chain(vs)
        st.success("✅ Document ready for QA")

    question = st.text_input("Ask a question about your document")
    if question:
        with st.spinner("🤖 Thinking..."):
            answer = qa.run(question)
            st.markdown("**💬 Answer:**")
            st.info(answer)
