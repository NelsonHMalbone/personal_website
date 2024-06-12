import streamlit as st

# centering the header
col1, col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    st.header('About Me')
    st.subheader('Who I Am?')
    st.write('')
with col3:
    st.write('')

# who i am section
col_1, col_2 = st.columns(2)
with col_1:
    st.image('images/photo.png', width=275)

with col_2:
    content = """
        Hi, my name is Nelson. Reliable Warehouse Worker with extensive experience
    """
    content1 = """
    A person that is eager to learn new things a team player with an eye for detail and safety
    """
    content2 = """
     Self learning how to code using python and along with photography 
    """
    st.info(content)
    st.info(content1)
    st.info(content2)
    st.write('')
col1, col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    data = "on the dl"
    st.download_button('Download Resume', data)
    st.write('')
with col3:
    st.write('')

# personal note
st.subheader('On a personal Note: ')
content3 = """
Im a father to a beautiful little girl also
I have been an volunteer firefighter for over 15 + years love to help and support the commmunity
when im not working or working on my code/photography
"""
st.info(content3)
st.write('')

# top 3 code section
col1, col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    st.subheader('Top 3 Code Projects')
with col3:
    st.write('')

col1, col2, col3 = st.columns(3)
with col1:
    st.write('img')
with col2:
    st.write('img2')
with col3:
    st.write('img3')
    st.write('')


# top 3 photos taken
col1, col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    st.subheader('Top 3 Photos Projects')
with col3:
    st.write('')

col1, col2, col3 = st.columns(3)
with col1:
    st.image('images/photos/Canal_oil_tanker 06-2024-9.jpg')
with col2:
    st.image('images/photos/Navy_boat_May-2024-5.jpg')
with col3:
    st.image('images/photos/Flowers-3.jpg')
