import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from components import expert, gis, about
import json
# from components import business, land_prediction, strategy, estimation, methodology, about, crime, life_quality

# Apply theme from the config file
st.set_page_config(
    page_title="I kontakt",
    page_icon="📞",
    layout="centered",
    initial_sidebar_state="expanded"
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Create a sidebar option menu
        with st.sidebar:
            app = option_menu(
                menu_title='📞 I kontakt',
                options=['🗨️ Deskundige',  
                         '🗺️ Kaart', '📖 Over de applicatie'],
                icons=['house-garden','house-garden','house-garden'],
                menu_icon='house-garden',
                default_index=0,  # Change the default index to 0 for "🏠 Прогноз стоимости"
                styles={
                    "container": {"padding": "5!important", "width": "100%"},  # Adjust width here
                    # "icon": {"color": "white", "font-size": "0px"},
                    "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "orange"},
                    "nav-link-selected": {"background-color": "#44484d"},
                }

            )


        # Display selected app based on user choice
        if app == "🗨️ Deskundige":
            expert.app()
        elif app == '🗺️ Kaart':
            gis.app()
        elif app == '📖 Over de applicatie':
            about.app()
         


# Create an instance of MultiApp and add your apps
multi_app = MultiApp()

# Add your apps to the MultiApp instance
multi_app.add_app("🗨️ Deskundige", expert.app)
multi_app.add_app("🗺️ Kaart", gis.app)
multi_app.add_app("📖 Over de applicatie", about.app)

# Run the MultiApp
multi_app.run()