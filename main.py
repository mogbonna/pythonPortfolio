import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)
with col1:
    st.image('images/photo.png')

with col2:
    st.title('Moses Ogbonna')
    content = """
        Hi, I am Moses! I am a Python programmer, teacher, and Mechatronics engineer. I graduated in 2015 with a Bachelor of Engineering in Chemical Engineering from the Nnamdi Azikiwe University, Awka in Anambra State, Nigeria with a focus on using Python for remote sensing.
    I have worked with companies from various countries, such as the Center for Conservation Geography, to map and understand Australian ecosystems, image processing with the Swiss in-Terra, and performing data mining to gain business insights with the Australian Rapid Intelligence.
        """
    st.info(content)

content2 = """Below you can find some of the apps I have built in python. Fell free to contact me!
"""
st.write(content2)