import streamlit as st
from openai import AzureOpenAI
import os

st.set_page_config(page_title="Azure OpenAI with Streamlit", layout="wide", page_icon="🤖")
st.title("Azure OpenAI with Streamlit")

# 明示的にセットアップ状況の設定を行う
if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False

def complete_setup():
    # ここで必要なセットアップ処理を実行
    st.session_state.setup_complete = True
    
def reset_setup():
    st.session_state.setup_complete = False
    
# if not st.session_state.setup_complete:
st.subheader("ギャル語チャットボット", divider="rainbow")

# コンポーネントの配置だけでなく、その入力を変数として受け取れる
# if not "name" in st.session_state:
st.session_state.name = st.text_input(label="ギャルの名前", max_chars=20, placeholder="名前を付けてね", value="ミキティ")

# if not "level" in st.session_state:
st.session_state.level = st.slider(label="ギャルのレベル", min_value=0, max_value=100, value=25, step=1)

col1, col2 = st.columns(2)
with col1:
    # if not "gallevel" in st.session_state:
        st.session_state.gallevel = st.radio("ギャルのレベルを選択してね", options=[0, 25, 50, 75, 100], index=1, horizontal=True)
with col2:
    # if not "school" in st.session_state:
        st.session_state.school = st.selectbox("ギャルの学校を選択してね", options=["渋谷ギャル学園", "原宿ギャル学園", "新宿ギャル学園"], index=0)

st.button("保存", on_click=complete_setup)

# 応答がハングすることがあるのでそこは要調整
if st.session_state.setup_complete:            
    client = AzureOpenAI(
        api_version="2025-01-01-preview",
        api_key=st.secrets["AZURE_OPENAI_API_KEY"],
        azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"]
        )

    if "model" not in st.session_state:
        st.session_state.model = "gpt-4o"

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role":"system", 
                                    "content": f"""
                                    あなたはギャル語でこたえるアシスタントです。あなたのプロフィールはこちらです。
                                    - 名前:{st.session_state.name}
                                    - ギャル度合い:{st.session_state.gallevel}/100
                                    - 学校:{st.session_state.school}
                                    最初に必ず自己紹介をしてください。
                                    """}]

    for m in st.session_state.messages:
        # system prompt でなければ message をすべて表示
        if m["role"] != "system":
            with st.chat_message(m["role"]):
                st.markdown(m["content"])
# 返答が５回未満であれば、入力可能
    if "user_message_count" not in st.session_state:
        st.session_state.user_message_count = 0
        
    if st.session_state.user_message_count < 3:
        if prompt := st.chat_input("Aske me anything!"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            with st.chat_message("assistant"):
                stream = client.chat.completions.create(
                    model=st.session_state.model,
                    messages=st.session_state.messages,
                    stream=True
                )
                response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.user_message_count += 1
        
    if st.session_state.user_message_count >= 3:
        st.info("これ以上質問できません。")
        st.button("設定を変更する", on_click=reset_setup)