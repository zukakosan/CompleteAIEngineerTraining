import streamlit as st

st.title("This is the title text")
# :blue[xxx] は中身を青色にする
# _xxx_ はイタリック体にする
# :speech_ballon: は吹き出しの絵文字
st.title('_This_is_ :blue[a_title]_ :speech_balloon:')

# LaTeX の形式も対応
st.title('$E = mc^2$')

st.header("This is the header text")
st.subheader("This is the subheader text")

st.text("This is the normal text")
st.markdown("""
            # Markdown Title
            ## aaa
            ### bbb
            - list1
            """)
st.write("This is the write text")

data = {'name': 'Alice', 'age': 24}
st.write(data)  # 辞書型も対応

# st.xxx でいろいろなコンポーネントを配置可能
# https://docs.streamlit.io/develop/api-reference/widgets/st.feedback
st.button("This is a button")
st.checkbox("This is a checkbox")
st.feedback("stars")