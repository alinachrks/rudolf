import streamlit as st
import streamlit.components.v1 as components
from openai import OpenAI
from streamlit_lottie import st_lottie
import json
from components.config_dialog import *

# Create an instance of the API client

# Access the OpenAI API key from Streamlit secrets
# api_key = st.secrets["OPENAI_API_KEY"]

def app():
    st.title("Карта Алматы")

    # HTML-код для встраивания карты и стилизованной кнопки полноэкранного режима
    mapbox_iframe_html = """
    <iframe id="mapboxIframe" width='100%' height='400px' src="https://api.mapbox.com/styles/v1/alinach/clrn3kwk7004501pl7mddfpzb.html?title=false&access_token=pk.eyJ1IjoiYWxpbmFjaCIsImEiOiJjbGlpcnZpaTgwMTZ4M2twaGo1NjRsNHhhIn0.9jw_R_D1i1nqOtaolld-dQ&zoomwheel=false#17/43.23546/76.903217/47.5/74" title="one" style="border:none;"></iframe>
    <button onclick="toggleFullscreen()" style="padding: 10px 20px; font-size: 16px; cursor: pointer; border: none; border-radius: 5px; background-color: #ACACAD; color: #ECEBE5;">Полноэкранный режим</button>
    <script>
        function toggleFullscreen() {
            var iframe = document.getElementById('mapboxIframe');
            if (!document.fullscreenElement) {
                iframe.requestFullscreen().catch(err => {
                    alert(`Ошибка при переходе в полноэкранный режим: ${err.message}`);
                });
            } else {
                document.exitFullscreen();
            }
        }
    </script>
    """

    # Встраивание HTML-кода карты в приложение Streamlit
    components.html(mapbox_iframe_html, height=450)

    
    # st.subheader("Хомяк-аналитик на связи")

    # # Sidebar with OpenAI API key input
    # with st.sidebar:
    #     openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    #     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    #     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    #     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"
    #     with open("animation/dino.json", "r", errors='ignore') as f:
    #         data = json.load(f)
    #     st_lottie(data)


    # if "messages" not in st.session_state:
    #     st.session_state["messages"] = [{"role": "assistant", "content": INITIAL_PROMPT}]

    # for msg in st.session_state.messages:
    #     st.chat_message(msg["role"]).write(msg["content"])

    # if prompt := st.chat_input():
    #     # Добавляем контекст о городе Алматы к сообщению пользователя
    #     st.session_state.messages.append({"role": "user", "content": prompt + " в стиле доброго и милого " + NLP_MODEL_NAME})
    #     st.chat_message("user").write(prompt)

    #     try:
    #         client = OpenAI(api_key=openai_api_key)
    #         # Создаем запрос с контекстом о городе Алматы
    #         response = client.chat.completions.create(model=NLP_MODEL_NAME, messages=st.session_state.messages)
    #         msg = response.choices[0].message.content
    #         st.session_state.messages.append({"role": "assistant", "content": msg})
    #         st.chat_message("assistant").write(msg)
    #     except Exception as e:
    #         st.error(f"OpenAI Error: {e}")
    with st.sidebar:
        with open("animation/bird_music.json", "r", errors='ignore') as f:
            data = json.load(f)
        st_lottie(data)