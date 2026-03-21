import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GOOGLE_API_KEY"] = "AIzaSyCJtS-1MBEB_wxTZaF_QH5_Wo0sZmsAZ44"

# ✅ LEARNING PROMPT TEMPLATE
chat_template = ChatPromptTemplate.from_messages([
    ("system", """You are an expert {expertise} assistant. 
    Provide {style} responses with clear explanations. 
    Be helpful, accurate, and engaging for learning."""),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

# ✅ Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0.7
)

# ✅ Chain
chain = chat_template | llm

# Streamlit UI
st.title("🚀 LangChain Learning Chatbot")
st.caption("Powered by Gemini + Prompt Templates")

# Sidebar
expertise = st.sidebar.selectbox("Expertise", ["Python/ML", "Data Science", "Cricket", "General"])
style = st.sidebar.selectbox("Response Style", ["detailed", "concise", "step-by-step"])

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Format history for template
            chat_history = []
            for msg in st.session_state.messages[:-1]:  # Exclude current
                if msg["role"] == "user":
                    chat_history.append(HumanMessage(content=msg["content"]))
                else:
                    chat_history.append(AIMessage(content=msg["content"]))

            # Invoke chain
            response = chain.invoke({
                "expertise": expertise,
                "style": style,
                "question": prompt,
                "chat_history": chat_history
            })
            
            st.markdown(response.content)
            st.session_state.messages.append({"role": "assistant", "content": response.content})

# Sidebar info
st.sidebar.markdown("### 📚 Learning Features")
st.sidebar.markdown("""
- **Dynamic Prompt Template** with variables
- **Conversation History** maintained
- **Customizable** expertise/style
- **Gemini 2.5 Flash** backend
""")
