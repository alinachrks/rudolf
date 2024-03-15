import streamlit as st
from streamlit_lottie import st_lottie
import json


def app():
    page_element="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://i.ibb.co.com/3yVykRQ/Minimal-Photography-1-fotor-20240315111216.png");
    background-size: cover;
    }
    [data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
    }
    [data-testid="stToolbar"]{
    right: 2rem;
    background-image: url("https://cdn.iconscout.com/icon/free/png-256/hamburger-menu-462145.png");
    background-size: cover;
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)

    # Заголовок страницы
    st.markdown("<h1 style='text-align: center; color: white; font-family: \"Old Standard TT\", serif; font-size: 32px;'>About the App </h1>", unsafe_allow_html=True)

    # Вставляем изображение после заголовка
    # st.image("img/about.png", use_column_width=True)

    # Описание приложения
    st.markdown("""
    <div style='font-family: "Old Standard TT", serif; padding: 18px; color: #525254; font-size: 18px; line-height: 1.2; margin-bottom: 5px;'>
    Древние тексты искаженных истин обрели форму в новом мире, где глаза человека встречают таинственные символы и непостижимые формы. В мрачном углу Интернета бродит молчаливый вестник измерений, неизведанных для умов смертных, - это веб-приложение, именуемое "Тень Алматы".    
    </div>

    <div style='font-family: "Old Standard TT", serif; padding: 18px; color: #525254; font-size: 18px; line-height: 1.2; margin-bottom: 5px;'>
    Написанное в коде и структурированное в тайне, оно раскрывает знания о местности, прежде скрытые от людей. Его алгоритмы проникают в тайные уголки города, предвещая перемены в ценах на землю и оценивая привлекательность районов.  
    </div>

    <div style='font-family: "Old Standard TT", serif; padding: 18px; color: #525254; font-size: 18px; line-height: 1.2; margin-bottom: 5px;'>
    Но внутри "Тени Алматы" скрываются иные тайны - они позволяют предугадывать преступность, раскрывают стратегии и раскрывают ужасные истины, простирающиеся за пределами понимания человечества.    
    </div>

    <div style='font-family: "Old Standard TT", serif; padding: 18px; color: #525254; font-size: 18px; line-height: 1.2; margin-bottom: 5px;'>
    Смелые искатели истины, взывающие к "Тени Алматы", должны быть осторожны, ибо её дары часто сопряжены с безумием и разрушением. Только те, кто готовы проникнуть в бездну неизвестного, могут постигнуть истину, замаскированную под код и данные, которые эта "Тень" предлагает.
    </div>
    """, unsafe_allow_html=True)

    with st.sidebar:
        with open("animation/car.json", "r", errors='ignore') as f:
            data = json.load(f)
        st_lottie(data)