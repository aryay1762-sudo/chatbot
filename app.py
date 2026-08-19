import streamlit as st

st.set_page_config(page_title="Emotional AI Chatbot", page_icon="🤖")

st.title("🤖 Emotional Support Chatbot")
st.write("Aap kaisa feel kar rahe hain? Yahan share karein.")

# Simple Keyword-Based Emotion Engine
def get_response(text):
    text = text.lower()
    if any(word in text for word in ["sad", "dukh", "upset", "crying", "lonely"]):
        return "Mujhe afsos hai ki aap aisa feel kar rahe hain. Main aapki baat sunne ke liye yahan hoon. Kya hua?"
    elif any(word in text for word in ["happy", "khush", "excited", "great", "awesome"]):
        return "Yeh toh bohot acchi baat hai! Aapki khushi dekh kar mujhe bhi accha laga. 🎉"
    elif any(word in text for word in ["angry", "gussa", "frustrated", "annoyed"]):
        return "Gussa aana swabhavik hai. Thoda lambi saans lein. Kya aap batana chahenge kis wajah se aisa hua?"
    elif any(word in text for word in ["stress", "tension", "worried", "anxious"]):
        return "Tension mat lijiye, sab theek ho jayega. Ek-ek karke cheezon ko handle karte hain."
    else:
        return "Main samajh raha hoon. Kripya mujhe aur vistar se batayein."

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Apna message yahan likhein..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
