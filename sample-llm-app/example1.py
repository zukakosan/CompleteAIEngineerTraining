import streamlit as st

st.title("Nested buttons")

if 'show_inner_button' not in st.session_state:
    # st.session_state.xxx に状態を保存
    st.session_state.show_inner_button = False

if st.button("Outer button"):
    st.session_state.show_inner_button = True

# 次のボタンの表示を上記の if から切り離すことで、状態を維持できる
if st.session_state.show_inner_button:    
    if st.button("Inner button 1"):
        st.write("Inner button 1 clicked")
    