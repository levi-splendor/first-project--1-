import streamlit as st

st.set_page_config(page_title="Chat with GePAI", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    .stApp { background-color: #0f0f0f; color: #e0e0e0; }
    section[data-testid="stSidebar"] { background-color: #1a1a1a; }
</style>
""", unsafe_allow_html=True)

# SIDEBAR 
with st.sidebar:
    st.markdown("### **GePAI**")
    st.markdown("#### Session Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Messages", len([m for m in st.session_state.get("messages", []) if m["role"] == "user"]))
    with col2:
        st.metric("Total", len(st.session_state.get("messages", [])))
    
    st.divider()
    st.markdown("#### Controls")
    agent = st.selectbox("Agents", ["Nurse=", "Doctor", "Therapist"], index=0)
    temperature = st.slider("Model temperature", 0.0, 2.0, 1.17, 0.01)
    top_p = st.slider("Top P", 0.0, 1.0, 0.90, 0.01)

# MAIN CHAT 
st.markdown("# Chat with GePAI")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm your GePAI assistant."}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🩺" if msg["role"] == "assistant" else None):
        st.markdown(msg["content"])

if prompt := st.chat_input("Message GePAI"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # TODO: Replace this with real LLM call (OpenAI, Grok, etc.)
    with st.chat_message("assistant", avatar="🩺"):
        response = f"Understood. As {agent} with temperature {temperature}, here's my response to: {prompt[:50]}..."
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})