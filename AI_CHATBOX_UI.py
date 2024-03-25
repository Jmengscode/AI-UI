from zhipuai import ZhipuAI
import streamlit as st
# 
with st.sidebar:
	zhipu_api_key = st.text_input("ZhipuAI API Key", key="chatbot_api_key", type="password")
	submit_button = st.button("提交", key="submit_chatbot_api_key")

st.title("💬 Lamher AI")
st.caption("🚀 AI界面，有疑问请联系ljm")
if "messages" not in st.session_state:
	st.session_state["messages"] = [{"role": "assistant", "content": "请提出您的问题，我会尽力解答。"}]

for msg in st.session_state.messages:
	st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
	if not zhipu_api_key:
		st.info("请输入您的AI码以继续")
		st.stop()

	client = ZhipuAI(api_key=zhipu_api_key)
	st.session_state.messages.append({"role": "user", "content": prompt})
	st.chat_message("user").write(prompt)
	response = client.chat.completions.create(model="glm-4", messages=st.session_state.messages)
	response = client.chat.completions.create(
		model="glm-4",  # 填写需要调用的模型名称
		messages=st.session_state.messages
	)
	msg = response.choices[0].message.content
	st.session_state.messages.append({"role": "assistant", "content": msg})
	st.chat_message("assistant").write(msg)

def clear_cache_and_message():
    """Clear Streamlit's cache and session state message."""
    # Clear the cache
    st.session_state.cache = {}

if st.sidebar.button('清除缓存'):
    clear_cache_and_message()

if st.sidebar.button('清除聊天内容'):
    st.empty()
