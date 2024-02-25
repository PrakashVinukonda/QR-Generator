#imports
import streamlit as st
import streamlit.components.v1 as components
import snowflake.connector
from streamlit_option_menu import option_menu
import time
import streamlit.components.v1 as components
import smtplib
from email.mime.text import MIMEText
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import qrcode
from defnitions import*
import pandas as pd 
from PIL import Image
import io
from pathlib import Path
import os
import re
from defnitions import *


#setting page configuration
st.set_page_config(layout="wide", page_title='Kipi.bi Nexus',page_icon="🎉")


 


#sessionstatements
if 'select' not in st.session_state:
    st.session_state.select=False

if 'upload' not in st.session_state:
    st.session_state.upload=False

if 'frame1' not in st.session_state:
    st.session_state.frame1=False

if 'Email' not in st.session_state:
    st.session_state.Email=False

if 'Emllist' not in st.session_state:
    st.session_state.Emllist=False

if 'formatted_lines' not in st.session_state:
    st.session_state.formatted_lines=False

if 'sendmailbutton' not in st.session_state:
    st.session_state.sendmailbutton=False


if 'file_count' not in st.session_state:
    st.session_state.file_count=False

if 'QRcodegenerate' not in st.session_state:
    st.session_state.QRcodegenerate=False

if 'Eventdate' not in st.session_state:
    st.session_state.Eventdate=False


if 'QRCodepathholder' not in st.session_state:
    st.session_state.QRCodepathholder=False


if 'selected_folder' not in st.session_state:
    st.session_state.selected_folder=False

if 'kipiid' not in st.session_state:
    st.session_state.kipiid=False


with st.sidebar:
    tab = option_menu(
        menu_title =None,
        options=["Home","QR Gen","Gmail","Analysis"],
        icons=["house","qr-code","envelope-plus","bar-chart"]
    )



st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"]{
            min-width: 210px;
            max-width: 210px;
        }
        """,
        unsafe_allow_html=True,
    )

if 'tab' not in st.session_state:
    st.session_state.tab=False


SNOWFLAKE_ACCOUNT = 'zk09026.ap-southeast-1' #https://fpb65609.us-east-1.snowflakecomputing.com
SNOWFLAKE_USER = 'Nexus4'
SNOWFLAKE_PASSWORD = 'Nexus$$4'
SNOWFLAKE_DATABASE = 'NEXUS'
SNOWFLAKE_SCHEMA = 'PUBLIC'
 
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA
)
cursor = conn.cursor()







#homepage
if tab == "Home":
    title_style = "color: white; text-align: left;"
  

    # title_html = """
    # <style>
    #     .scrolling-title {
    #         font-size: 2.5em;
    #         color: white;
    #         text-decoration: none;
    #         display: flex;
    #         flex-direction: row;
    #         align-items: center;
    #     }

    #     .static-part {
    #         color: #8fce00;
    #     }

    #     .scrolling-text {
    #         animation: scroll 12s linear infinite;
    #         white-space: nowrap; /* Prevent text from wrapping */
    #     }

    #     @keyframes scroll {
    #         0% {
    #             transform: translateX(100%); /* Start off-screen to the right */
    #         }
    #         100% {
    #             transform: translateX(calc(-100% - 100px)); /* Move to off-screen to the left */
    #         }
    #     }
    # </style>
    # <h1 class="scrolling-title">
    #     <span class="static-part"><a href="https://kipi.bi" style="color: #8fce00; text-decoration: none;">Kipi. bi</a> - Nexus, </span>
    #     <span class="scrolling-text">Hyderabad, Bangalore, Pune! 🥳</span>
    # </h1>
    # """

    title_html = """
    <style>
        .scrolling-title {
            font-size: 2.5em;
            color: white;
            text-decoration: none;
            display: flex;
            flex-direction: row;
            align-items: center;
        }

        .static-part {
            color: #8fce00;
        }

        .scrolling-text {
            animation: scroll 12s linear infinite;
            white-space: nowrap; /* Prevent text from wrapping */
        }

        @keyframes scroll {
            0% {
                transform: translateX(100%); /* Start off-screen to the right */
            }
            100% {
                transform: translateX(calc(-100% - 100px)); /* Move to off-screen to the left */
            }
        }
    </style>
    <h1 class="scrolling-title">
        <span class="static-part"><b><a href="https://kipi.bi" style="color: #8fce00; text-decoration: none;">Kipi. bi - Nexus</a></b>, </span>
        <span class="scrolling-text"><b>Hyderabad, Bangalore, Pune! 🥳</b></span>
    </h1>
    """






    # Kipi. bi - Nexus, Hyderabad, Bangalore, Pune!
    st.markdown(title_html, unsafe_allow_html=True)

    
  
 

    # Custom CSS for card styling and zigzag layout
    custom_css = """
    <style>
        .zigzag-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: flex-start;
            align-content: flex-start;
            gap: 10px;
        }

        .zigzag-card {
            width: 250px;
            height: 220px;
            background-color: #8fce00;
            border-radius: 15px;
            margin: 10px;
            display: flex;
            flex-direction: column;
            align-items: left;
            justify-content: left;
            transition: transform 0.2s ease-in-out;
            color: black; /* Black-colored text */;
            padding-left: 2rem;
             
        }

        .zigzag-card:hover {
            animation-name: shake;
            animation-duration: 0.2s;
            animation-timing-function: ease-in-out;
        }

        @keyframes shake {
            0% {
                transform: translateX(0);
            }
            25% {
                transform: translateX(-2px);
            }
            50% {
                transform: translateX(2px);
            }
            75% {
                transform: translateX(-2px);
            }
            100% {
                transform: translateX(2px);
            }

        h2 {
            color: black;
        }
    </style>
    """
   
   

 
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown('<div class="zigzag-container">', unsafe_allow_html=True)

    num_cards = 4
    for card_number in range(2, num_cards + 2):
        col1,col2=st.columns([2,2])
        with col1:
            col3,col4,col5=st.columns([2,1,2])
            with col3:
                if card_number==2:
                    st.markdown(
                                """
                                <div class="zigzag-card">
                                    <style>
                                        /* Reset margins and paddings for the entire HTML document */
                                        body, div, h3, p, ol, ul, li {
                                            margin: 0;
                                            padding: 1;
                                        }
                                    </style>
                                    <h3>Step 1</h3>
                                    <p><strong>Instructions:</strong></p>
                                    <ol>
                                        <li><strong>Click On QR Gen from nav.</strong></li>
                                        <li><strong>Upload to list file.</strong></li>
                                        <li><strong>Enter Event Date.</strong></li>
                                        <li><strong>Click on Generate QR's.</strong></li>
                                    </ol>
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )

                   
       
                elif card_number==3:
                    st.markdown(
                        """
                        <div class="zigzag-card">
                            <h3>Step 2</h3>
                            <p><strong>Instructions:</strong></p>
                            <ol>
                                <li><strong>Click On Gmail Tab.</strong></li>
                                <li><strong>Upload Collectors list file.</strong></li>
                                <li><strong>*To list file == Collectors <br>list file.</strong></li>
                                <li><strong>Choose Event Folder.</strong></li>
                            </ol>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )  


            with col5:
                if card_number==2:
                    st.markdown(
                                """
                                <div class="zigzag-card">
                                    <style>
                                        /* Reset margins and paddings for the entire HTML document */
                                        body, div, h3, p, ol, ul, li {
                                            margin: 0;
                                            padding: 1;
                                        }
                                    </style>
                                    <h3>Step 3</h3>
                                    <p><strong>Instructions:</strong></p>
                                    <ol>
                                        <li><strong>Check to "Preview" data.</strong></li>
                                        <li><strong>Input details in Mass <br> Mailing expander.</strong></li>
                                        <li><strong>Files auto-attach.</strong></li>
                                        <li><strong>Click on Send.</strong></li>
                                    </ol>
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )

                   
                    
                elif card_number == 3:
                    st.markdown(
                        """
                        <div class="zigzag-card">
                            <style>
                                /* Reset margins and paddings for the entire HTML document */
                                body, div, h3, p, ol, ul, li {
                                    margin: 0;
                                    padding: 1;
                                }
                            </style>
                            <h3>Step 4</h3>
                            <p><strong>Key points</strong></p>
                            <ol>
                                <li><strong>Upload a single CSV file <br>in both uploaders.</strong></li>
                                <li><strong>Choose Event Date properly.</strong></li>
                                <li><strong>Upload Collectors list file.</strong></li>
                            </ol>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

    # Close the container
    st.markdown("</div>", unsafe_allow_html=True)











if tab=="QR Gen":
   
    def generate_qr_code(data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        return img
    
    ""
    ""

    st.subheader("**QR Code Generator**")
    st.markdown("<div id='linkto_top'></div><style>div.block-container{padding-top:0rem;}</style>", unsafe_allow_html=True)

   
    col1,col2=st.columns([6,5.4])
    with col2:
        with st.expander("Upload the **To list**", expanded=True):
            
            st.session_state.upload = st.file_uploader("", type=["csv"])
            st.caption("Limit 200Mb only.")
            st.info('File should be Csv file & format -  ***gmail,Designation,Location***')

            st.session_state.Eventdate=st.text_input('Enter Event Date:',help='e.g., 16Sep2023',placeholder="16Sep2023")
            folder_name =  st.session_state.Eventdate 
            
            streamlit_folder = Path.cwd() / ".streamlit"
            folder_to_create = streamlit_folder / folder_name
            #st.write(folder_to_create)

            if not folder_to_create.exists():
                folder_to_create.mkdir()
                print(f"Folder '{folder_name}' created successfully in {streamlit_folder}.")
            else:
                print(f"Folder '{folder_name}' already exists in {streamlit_folder}.")



            hide_label = """
            <style>
                .css-9ycgxx {
                    display: none;
                }
            </style>
            """
            st.markdown(hide_label, unsafe_allow_html=True)
            
            hide_label1 = """
            <style>
                .css-61rn6a{
                    display: none;
                }
            </style>
            """
            st.markdown(hide_label1, unsafe_allow_html=True)
                
            hide_label2= """
            <style>
                .css-aoyl2m{
                    margin-top: 0rem;
                    margin-bottom: 0.12rem;
                }
            </style>
            """
            st.markdown(hide_label2, unsafe_allow_html=True)


            if st.session_state.upload is not None:
                df = pd.read_csv(st.session_state.upload)
                df.drop_duplicates(inplace=True)
                
                st.session_state.frame1 = pd.DataFrame(df)
                #st.write(st.session_state.frame1)




                res=[]
                for column in df.columns:               
                    li = st.session_state.frame1[column].tolist()
                    res.append(li)
                
                
                num_sublists = len(res)            
                st.session_state.formatted_lines = []
                for i in range(len(res[0])):
                    line = " - ".join(res[j][i].strip() for j in range(num_sublists))
                    st.session_state.formatted_lines.append(line)
                    
            

                df=pd.DataFrame(st.session_state.frame1)
                df.insert(0, "S.No", range(1, len(df) + 1))
                df.set_index("S.No", inplace=True)
                css = """
                        <style>
                            @keyframes blink {
                                0%, 100% {
                                    opacity: 1;
                                }
                                50% {
                                    opacity: 0;
                                }
                            }
                            .blink {
                                animation: blink 2s 5; /* Blink 5 times */
                                display: inline-block;
                            }
                        </style>
                """
                st.markdown(css, unsafe_allow_html=True)
                st.markdown('<h3 style="color: #8fce00;">Preview <span class="blink">👁️</span></h3>', unsafe_allow_html=True)
                st.dataframe(df) 
                st.info(f'Total Records: {len(df)}')
                
                colblink1,colblink2=st.columns([6,15])
                with colblink1:
                    st.write('<style>.column-padding { padding-top: 0; }</style>', unsafe_allow_html=True)
                    st.session_state.QRcodegenerate=st.button("Generate QR's",type='primary',key='Generate QR Codes')
                with colblink2:
                    st.markdown(
                                    """
                                    <style>
                                    @keyframes color-change {
                                        0% { color: #111111; }
                                        50% { color: #8fce00; }
                                        100% { color: #111111; }
                                    }
                                    .text-animation {
                                        animation: color-change 2s infinite alternate;
                                    }
                                    </style>
                                    """,
                                    unsafe_allow_html=True)
                
                if st.session_state.QRcodegenerate==False:   
                    st.write('<p class="text-animation"><b>Click ⬆️ button to Generate!</p>', unsafe_allow_html=True)

                            
            elif st.session_state.upload==None:
                with col1:
                    st.info("Please upload file to Generate QR's")





    with col1:
 
        if st.session_state.upload!=None:
            if len(st.session_state.Eventdate) == 9 and st.session_state.Eventdate[:2].isdigit() and st.session_state.Eventdate[2:5].isalpha() and st.session_state.Eventdate[5:].isdigit():            
                
                if st.session_state.QRcodegenerate==True:
                    target_folder = str(folder_to_create)
                    for filename in os.listdir(target_folder):
                        file_path = os.path.join(target_folder, filename)
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                    
                    with st.expander("QR Code",expanded=True):
                        for value in st.session_state.formatted_lines:
                            qr_img = generate_qr_code(value)
                            qr_bytes = io.BytesIO()
                            qr_img.save(qr_bytes, format='PNG')  # Save image as bytes
                            
                            st.image(qr_bytes, caption=value, use_column_width=False)
                            
                                
                            vsplit=value.split('-')
                            vsplit = vsplit[3]+"_"+vsplit[0]
                            
                            file_path = save_image_to_folder(qr_img, folder_to_create, f"{vsplit}.png")
                         
                            qr_img.save(file_path)
                            
                            st.write(f"QR code saved in: {file_path}")
                            st.write("---")
                        st.info(f"Generated {len(st.session_state.formatted_lines)} Qr Codes")
            else:
                st.info("Enter Valid Event Date [ddMMMyyyy]")  

            st.markdown("<a href='#linkto_top' style='color: #8fce00; text-decoration: none; font-weight: bold;'>Back to top</a>", unsafe_allow_html=True)
    
  
    























elif tab == "Gmail":

    st.markdown('''
        <style>
            @keyframes moveRocket {
                0% {
                    transform: translateY(0);
                }
                50% {
                    transform: translateY(-7px);
                }
                100% {
                    transform: translateY(0);
                }
            }

            .rocket-emoji {
                display: inline-block;
                animation: moveRocket 2s infinite;
            }
        </style>
        <h3 style="color: #8fce00;">
            <b>Email Sender with QR Code Attachment</b> <span class="rocket-emoji">🚀</span>
        </h3>
    ''', unsafe_allow_html=True)

 


    #columns
    col1,col2,col3,col4=st.columns([11,0.01,4,0.1])

    with col3:
        with st.expander("Upload **collectors list**",expanded=True):
            st.session_state.upload = st.file_uploader("", type=["csv"])
            st.caption('''Please Upload .csv file.''')
            st.info('Details should be in this format --  ***gmail,Designation,Location***')
            st.write("<hr style='margin: 0 -1%;'>", unsafe_allow_html=True)



            st.markdown(
                            """
                            <style>
                            @keyframes color-change {
                                0% { color: #111111; }
                                50% { color: #8fce00; }
                                100% { color: #111111; }
                            }
                            .text-animation {
                                animation: color-change 2s infinite alternate;
                            }
                            </style>
                            """,
                            unsafe_allow_html=True)
        
   
                
    

            
            streamlit_folder = Path.cwd() / ".streamlit"
            st.session_state.QRCodepathholder = []
            if streamlit_folder.is_dir():
                items = [item.name for item in streamlit_folder.iterdir() if item.is_dir()]
                st.write('<p class="text-animation"><b>Please Select Event Date Carefully!</p>', unsafe_allow_html=True)
                items.insert(0, "None")

                if items:
                    st.session_state.selected_folder = st.selectbox("Choose Event Date:", items)
                    if st.session_state.selected_folder != "None":
                        selected_folder_path = streamlit_folder / st.session_state.selected_folder
                        files = [str(file) for file in selected_folder_path.iterdir() if file.is_file()]
                        st.session_state.file_count = len(files)
                        st.success(f"Choosen: {st.session_state.selected_folder}")
                        for file in files:
                            qr=st.session_state.QRCodepathholder.append(file)


                    else:
                        st.warning("No folder selected.")
                else:
                    st.error("The .streamlit folder is empty (no subdirectories).")
            else:
                st.error(".streamlit folder does not exist.")

            
           








            # streamlit_folder = Path.cwd() / ".streamlit"
            # if streamlit_folder.is_dir():
                
            #     items = [item.name for item in streamlit_folder.iterdir() if item.is_dir()]
            #     st.write('<p class="text-animation"><b>Please Select Event Date Carefully!</p>', unsafe_allow_html=True)
            #     if items:
            #         selected_folder = st.selectbox("Select a folder:", items)
            #         selected_folder_path = streamlit_folder / selected_folder
            #         files = [str(file) for file in selected_folder_path.iterdir() if file.is_file()]
            #         st.write(f"Files in the selected folder '{selected_folder}':")
            #         for file in files:
            #             st.write(file)
            #     else:
            #         st.error("The .streamlit folder is empty (no subdirectories).")
            # else:
            #     st.error(".streamlit folder does not exist.")



 




            hide_label = """
            <style>
                .css-9ycgxx {
                    display: none;
                }
            </style>
            """
            st.markdown(hide_label, unsafe_allow_html=True)
            
            hide_label1 = """
            <style>
                .css-61rn6a{
                    display: none;
                }
            </style>
            """
            st.markdown(hide_label1, unsafe_allow_html=True)
                
            hide_label2= """
            <style>
                .css-aoyl2m{
                    margin-top: 0rem;
                    margin-bottom: 0.12rem;
                }
            </style>
            """
            st.markdown(hide_label2, unsafe_allow_html=True)
    
 




    with col1:
        with st.expander("**Mass Mailing**",expanded=False):
            col1,col2=st.columns(2)
            with col1:
                email_sender = st.text_input("Your Email:")
            with col2:
                password = st.text_input("Your Password:", type="password")
            subject = st.text_area("Subject:",height=100)
            body = st.text_area("Body:",height=400)
            st.caption('''Note: Before sending, please generate QR codes from the 'QR Gen' tab.''')
            col1,col2,col3=st.columns([5,11,3])
            with col3:
                st.session_state.sendmailbutton=st.button('Send',use_container_width=True)


        if st.session_state.upload is not None:
            df = pd.read_csv(st.session_state.upload)
            df.drop_duplicates(inplace=True)
            cols = df.columns.tolist()         
            
            st.session_state.frame1 = pd.DataFrame(df)
             
            res=[]
            for column in df.columns:               
                li = st.session_state.frame1[column].tolist()
                res.append(li)
            
            
      
      
            num_sublists = len(res)  
            formatted_lines = []
            max_sublist_length = max(len(sublist) for sublist in res)  

            for i in range(max_sublist_length):
                line = " - ".join(sublist[i].strip() if i < len(sublist) else "" for sublist in res)
                formatted_lines.append(line)
          
         
    
        
            st.session_state.Email    =[]
            st.session_state.Emllist  =[]
            st.session_state.kipiid = []
            
    
            for i in range(len(formatted_lines)):
                st.session_state.Email.append(res[0][i])
                st.session_state.Emllist.append(res[0][i])
                
                st.session_state.kipiid.append(res[3][i])
            
            st.session_state.Email = ', '.join(st.session_state.Email)

            df.insert(0, "S.No", range(1, len(df) + 1))
            df.set_index("S.No", inplace=True)

 

            # if st.session_state.selected_folder != 'None':
            #     st.session_state.frame1 = df

            #     # Function to list image files from a directory
            #     def list_image_files(directory):
            #         image_files = []
            #         for filename in os.listdir(directory):
            #             if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            #                 image_files.append(os.path.join(directory, filename))
            #         return image_files

            #     st.session_state.Emllist.sort()

            #     directory_without_filename = os.path.dirname(st.session_state.QRCodepathholder[0])
            #     image_files = list_image_files(directory_without_filename)
            #     image_files.sort()

            #     # Ensure all lists have the same length
            #     min_length = min(len(st.session_state.Emllist), len(image_files), len(st.session_state.frame1))

            #     # Create a dictionary to map email to image and ID
            #     email_and_image = {}
            #     emailbox = []

            #     # Iterate over the minimum length
            #     for idx in range(min_length):
            #         # Extract email from Emllist
            #         email = st.session_state.Emllist[idx]

            #         # Extract image file from image_files
            #         image_file = image_files[idx]

            #         # Extract ID from the DataFrame
            #         id_value = st.session_state.frame1.iloc[idx]['ID'] if 'ID' in st.session_state.frame1.columns else None

            #         # Store email and corresponding image file along with ID
            #         email_and_image[email] = {'image_file': image_file, 'ID': id_value}
            #         emailbox.append(email)

            #     st.write(emailbox)



            
            

            # check=st.checkbox("Preview")

            if st.session_state.selected_folder!='None':
            #     st.write("collectors list")

                st.session_state.frame1=df
                
                cols=st.session_state.frame1.columns
                # Function to list image files from a directory
                def list_image_files(directory):
                    image_files = []
                    for filename in os.listdir(directory):
                         
                       
                        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                             
                            image_files.append(os.path.join(directory, filename))
                    return image_files

                st.session_state.Emllist.sort()
 

                directory_without_filename = os.path.dirname(st.session_state.QRCodepathholder[0])
                 

                image_files = list_image_files(directory_without_filename)
                    
                image_files.sort()
               
                st.session_state.kipiid.sort()
                 
                # Ensure both lists have the same number of elements
                min_length = min(len(st.session_state.Emllist), len(image_files),len(st.session_state.kipiid))
                Emllist = st.session_state.Emllist[:min_length]
                image_files = image_files[:min_length]
                kipiid = st.session_state.kipiid[:min_length]

                # Create a dictionary to map email to image
                email_and_image = {}
                
                emailbox=[]
                
                for idx, image_file in enumerate(image_files):
                    email = Emllist[idx]
                    email_and_image[email] = image_file
                    
                    emailbox.append(Emllist[idx])
                    
           
                # st.write(email_and_kipiid)
                # st.write(emailbox)
                
                
                data = []
                
                for email, image_path in email_and_image.items():
                    data.append({"EmailId": email, "Image attached path": image_path})

                df = pd.DataFrame(data)
                
                merged_df = pd.merge(st.session_state.frame1, df, on="EmailId", how="outer")
                
                merged_df.insert(0, "S.No", range(1, len(df) + 1))
                merged_df.set_index("S.No", inplace=True)
                
                unique_merged_df = merged_df.drop_duplicates(subset="EmailId")
            
            
            check=st.checkbox("Preview")
            if check==True and st.session_state.selected_folder!='None':
                st.write("collectors list")
                st.write(unique_merged_df)

                st.info(f"Total QR codes in the directory: {st.session_state.file_count}")
            
            elif check==True and st.session_state.selected_folder==None:
                st.warning('Please Choose a Folder')
            
            
            if st.session_state.sendmailbutton==True:
                with st.spinner("Sending..."):
                    try:
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email_sender, password)


                        for recipient_email,  image_file in email_and_image.items():
                            
                            # kipiid = email_and_kipiid.get(recipient_email)
                            # st.write(kipiid)
                    
                            msg = MIMEMultipart()
                            msg['From'] = email_sender
                            msg['Subject'] = subject
                           
                            
                            msg.attach(MIMEText(body, 'plain'))
                            
                            msg['To'] = recipient_email

                            with open(image_file, "rb") as img_file:
                                image_data = img_file.read()
                            image_filename = os.path.basename(image_file)
                            image = MIMEImage(image_data, name=image_filename)
                            msg.attach(image)

                            server.sendmail(email_sender, [recipient_email], msg.as_string())
                            

                        st.success('Email with attached image sent successfully to all recipients! 🚀')
                        st.session_state.sendmailbutton=False
                            

                        server.quit()
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
                




                # failed_emails = []  # Create an empty list to store failed emails
                # with st.spinner("Sending..."):
                #     try:
                #         server = smtplib.SMTP('smtp.gmail.com', 587)
                #         server.starttls()
                #         server.login(email_sender, password)

                #         for recipient_email, image_file in email_and_image.items():
                #             msg = MIMEMultipart()
                #             msg['From'] = email_sender
                #             msg['Subject'] = subject
                #             msg.attach(MIMEText(body, 'plain'))

                #             msg['To'] = recipient_email

                #             with open(image_file, "rb") as img_file:
                #                 image_data = img_file.read()
                #             image_filename = os.path.basename(image_file)
                #             image = MIMEImage(image_data, name=image_filename)
                #             msg.attach(image)

                #             try:
                #                 server.sendmail(email_sender, [recipient_email], msg.as_string())
                #             except Exception as e:
                #                 st.error(f"Failed to send email to {recipient_email}: {e}")
                #                 failed_emails.append(recipient_email)

                #         server.quit()

                #         if not failed_emails:
                #             st.success('Emails with attached images sent successfully to all recipients! 🚀')
                #             st.session_state.sendmailbutton = False
                #         else:
                #             st.warning('Some emails failed to send. Please check the list of failed recipients.')

                #     except Exception as e:
                #         st.error(f"An error occurred: {e}")

                
                # if failed_emails:
                #     st.write("List of failed email recipients:")
                #     for email in failed_emails:
                #         st.write(email)

                   
                #     df = pd.DataFrame({'Failed Emails': failed_emails})
                #     csv_data = df.to_csv(index=False)

                   
                #     st.markdown(f'<a href="data:file/csv;base64,{base64.b64encode(csv_data.encode()).decode()}" download="failed_emails.csv">Download CSV File</a>', unsafe_allow_html=True)







elif tab=="Analysis":  
    st.markdown("<h1 style='text-align: center; margin-top: 0; margin-bottom: 0;'>Total Attendees</h1>", unsafe_allow_html=True)


    try:
        cursor.execute('USE DATABASE NEXUS')
        cursor.execute('USE SCHEMA RAW')
        cursor.execute('USE WAREHOUSE COMPUTE_WH')
        data=cursor.execute('SELECT * FROM NEXUS.RAW.QR_ENTRY;')
        
        headers=['Gmail','Designation','Location',"Eventplace",'Entrytime']
        df_A=pd.DataFrame(data,columns=headers)
        df_A.insert(0, "S.No", range(1, len(df_A) + 1))
        df_A.set_index("S.No", inplace=True)

 
    

        formatted_headers = [f'<b>{col}</b>' for col in df_A.columns]

        
        all_option = "All"
        location_options = df_A['Location'].unique().tolist()
        location_options.append(all_option)
        
        selected_location = st.selectbox("Select Location", location_options)

        
        if selected_location == all_option:
            filtered_df = df_A   
        else:
            filtered_df = df_A[df_A['Location'] == selected_location]

        st.write(filtered_df)

        count_attendees = len(filtered_df)
        st.markdown(f"<span style='color: #8fce00; font-size: 25px;'>Total Attendees from {selected_location}: <span style='color: white; background-color: transparent; padding: 0 3px; font-size: 25px;'>{count_attendees}</span></span>", unsafe_allow_html=True)

    

    except Exception as E:
        st.error(f"Encountered wtih {E}")
                    
  
   
