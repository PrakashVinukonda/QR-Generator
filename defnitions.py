import streamlit as st

def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
#@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
    
header_style = """
<style>
    div[data-baseweb="select"] > div:first-child {
        background-color: #B3D943;
        color: white;
    }
</style>
"""


def save_image_to_folder(image, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    file_path = os.path.join(folder, filename)
    image.save(file_path)
    return file_path

 
 

def PostFunction(placeholder):
     
            
    st.session_state.success_message = st.success(f'**{st.session_state.selected_entity}** Entry Successfull!.')
    audio_file=open('C:\\Users\\VinukondaBalaramPrak\\Desktop\\Nexusapp\\Audio\\gotitem.mp3', 'rb')
    audio_bytes = audio_file.read()
    audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
    st.session_state.success_audio=st.markdown(f'<audio src="data:audio/mp3;base64,{audio_base64}" autoplay="autoplay" controls="controls"></audio>', unsafe_allow_html=True)
    time.sleep(4) 

    st.session_state.success_message.empty()
    st.session_state.success_audio.empty()

    #st.session_state.selected_entity=False
    st.session_state.success_audio=False
    st.session_state.success_message=False



def is_valid_date_format(input_string):
    pattern = r"^\d{2}[A-Za-z]{3}\d{4}$"
    if re.match(pattern, input_string):
        return True
    else:
        return False





def load_lottieurl(url:str):
            r=requests.get(url)
            if r.status_code !=200:
                return None
            return r.json()
