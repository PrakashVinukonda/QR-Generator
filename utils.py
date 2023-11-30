import streamlit as st
import base64
from streamlit.components.v1 import html
from PATHS import NAVBAR_PATHS, SETTINGS

def inject_custom_css():
    with open('assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def get_current_route():
    try:
        query_params = st.experimental_get_query_params()
        return query_params['nav'][0] if 'nav' in query_params else 'home'
    except:
        return 'home'

def navbar_component():
    # with open("assets/images/settings.png", "rb") as image_file:
    #     image_as_base64 = base64.b64encode(image_file.read())

    navbar_items = ''
    for key, value in NAVBAR_PATHS.items():
        if key == 'Kipi.bi':
            navbar_items += f'<a class="navitem" href="https://kipi.bi" target="blank" style="font-weight: normal;">{key}</a>'
        else:
            navbar_items += (f'<a class="navitem" href="/?nav={value}">{key}</a>')

    # settings_items = ''
    # for key, value in SETTINGS.items():
    #     settings_items += (
    #         f'<a href="/?nav={value}" class="settingsNav">{key}</a>')







    # component = rf'''
    #     <nav class="container navbar" id="navbar">
    #         <ul class="navlist">
    #             {navbar_items}
    #         </ul>
    #         <p class="navbar-text" style="margin-left: auto;">
    #             <a href="/?nav=kipibi" style="text-decoration: none; color: inherit;">Kipi.bi</a>
    #         </p>
    #     </nav>
    # '''
    # st.markdown(component, unsafe_allow_html=True)




    component = rf'''
            <nav class="container navbar" id="navbar">
                <ul class="navlist">
                {navbar_items}
                </ul>
                
            </nav>
            '''
    st.markdown(component, unsafe_allow_html=True)
    
    
    js = '''
    <script>
        // navbar elements
        var navigationTabs = window.parent.document.getElementsByClassName("navitem");
        var cleanNavbar = function(navigation_element) {
            navigation_element.removeAttribute('target')
        }
        
        for (var i = 0; i < navigationTabs.length; i++) {
            cleanNavbar(navigationTabs[i]);
        }
        
        // Dropdown hide / show
        var dropdown = window.parent.document.getElementById("settingsDropDown");
        dropdown.onclick = function() {
            var dropWindow = window.parent.document.getElementById("myDropdown");
            if (dropWindow.style.visibility == "hidden"){
                dropWindow.style.visibility = "visible";
            }else{
                dropWindow.style.visibility = "hidden";
            }
        };
        
        var settingsNavs = window.parent.document.getElementsByClassName("settingsNav");
        var cleanSettings = function(navigation_element) {
            navigation_element.removeAttribute('target')
        }
        
        for (var i = 0; i < settingsNavs.length; i++) {
            cleanSettings(settingsNavs[i]);
        }
    </script>
    '''
    html(js)

def main():
    # Inject custom CSS
    inject_custom_css()

    # Get the current route
    current_route = get_current_route()

    # Check if the current route is not specified or is "home"
    if current_route is None or current_route == 'home':
        # Set your default content for the "home" route
        st.title("Welcome to the Home Page")
        st.write("This is the default content for the home page.")
    else:
        # Handle other routes here
        pass

    # Render the navbar component
    navbar_component()

if __name__ == "__main__":
    main()




# import streamlit as st
# import base64
# from streamlit.components.v1 import html

# from PATHS import NAVBAR_PATHS, SETTINGS


# def inject_custom_css():
#     with open('assets/styles.css') as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# def get_current_route():
#     try:
#         return st.experimental_get_query_params()['nav'][0]
#     except:
#         return None


# def navbar_component():
#     with open("assets/images/settings.png", "rb") as image_file:
#         image_as_base64 = base64.b64encode(image_file.read())

#     navbar_items = ''
#     for key, value in NAVBAR_PATHS.items():
#         navbar_items += (f'<a class="navitem" href="/?nav={value}">{key}</a>')


 




#     settings_items = ''
#     for key, value in SETTINGS.items():
#         settings_items += (
#             f'<a href="/?nav={value}" class="settingsNav">{key}</a>')

#     component = rf'''
#             <nav class="container navbar" id="navbar">
#                 <ul class="navlist">
#                 {navbar_items}
#                 </ul>
#                 <div class="dropdown" id="settingsDropDown">
#                     <img class="dropbtn" src="data:image/png;base64, {image_as_base64.decode("utf-8")}"/>
#                     <div id="myDropdown" class="dropdown-content">
#                         {settings_items}
#                     </div>
#                 </div>
#             </nav>
#             '''
#     st.markdown(component, unsafe_allow_html=True)
#     js = '''
#     <script>
#         // navbar elements
#         var navigationTabs = window.parent.document.getElementsByClassName("navitem");
#         var cleanNavbar = function(navigation_element) {
#             navigation_element.removeAttribute('target')
#         }
        
#         for (var i = 0; i < navigationTabs.length; i++) {
#             cleanNavbar(navigationTabs[i]);
#         }
        
#         // Dropdown hide / show
#         var dropdown = window.parent.document.getElementById("settingsDropDown");
#         dropdown.onclick = function() {
#             var dropWindow = window.parent.document.getElementById("myDropdown");
#             if (dropWindow.style.visibility == "hidden"){
#                 dropWindow.style.visibility = "visible";
#             }else{
#                 dropWindow.style.visibility = "hidden";
#             }
#         };
        
#         var settingsNavs = window.parent.document.getElementsByClassName("settingsNav");
#         var cleanSettings = function(navigation_element) {
#             navigation_element.removeAttribute('target')
#         }
        
#         for (var i = 0; i < settingsNavs.length; i++) {
#             cleanSettings(settingsNavs[i]);
#         }
#     </script>
#     '''
#     html(js)
