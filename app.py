import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

load_dotenv()

st.title("LLM機能を搭載したWebアプリ")

st.write("##### 動作モード1: Aの領域の専門家")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで選択したAの領域の回答が得られます。")
st.write("##### 動作モード1: Bの領域の専門家")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで選択したBの領域の回答が得られます。")

selected_item = st.radio(
    "質問する専門家を選択してください。",
    ["Aの領域の専門家", "Bの領域の専門家"]
)

st.divider()

input_message = st.text_input(label="質問を入力してください。")

if st.button("実行"):
    st.divider()

    if input_message:
        st.error("テキストを入力してから「実行」ボタンを押してください。")
        exit
    
    if selected_item == "Aの領域の専門家":
        content="あなはたはAの領域の専門家です。"
    else:
        content="あなはたはBの領域の専門家です。"

    messages = [
        SystemMessage(content=content),
        HumanMessage(content=input_message),
    ]

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    result = llm(messages)

    st.write(f"回答: **{result.content}**")