import streamlit as st 

st.set_page_config(page_title="My Webpage",page_icon=":tata:",layout="wide")







st.subheader("Hi I'm Prathiba:wave:")
st.title("A Data Analyst from Chennai")
st.write("I'm passionate about finding ways to use python & powerbi to be more efficient and effective in business")
st.write("<learn more>")
with st.container():
    st.write("---")
    left_column,right_column= st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("#")
        st.write("""
        I Am proficient data analyst with experience in excel,power bi,tableau ,R language
        - also eagerly engaged in making dynamic models of predictions and so on.
        if this sounds interesting to you , consider to reach me out.
         """
        )
        with right_column:
            st.image("analyst.webp")




def home():
    st.title("Welcome to My Portfolio")
    st.write("This is the home section of the portfolio ")
     
def about():
    st.title("About Me")
    st.write("""
    Hello! I'm a prathiba, and this is a showcase of my work.
    I specialized in [python,powerbi,tableau,streamlit,excel,sql and so on].
    """)

def projects():
    st.title("Projects")
    st.write("""
    ### Project 1: [AI ACCOUNTING software with AI]
    - Description: [From this project you can be able to find out where can a specified acounting items would appear.
    And also it works As search bar to find the posting of an accounting item.]
    
    ### Project 2: [RISK MANAGEMENT DATA THROUGH POWERBI ]
    - Description: [From this project you can be able to find out the visualisation of risk management for specified
    And also it works As search bar to find the posting of an accounting item.]
    """)
    


def contact():
    st.title("Contact Me")
    st.write("You can reach me at prathiba.tmuthu@gmail.com.")
def image():
    st.title("project1")
    st.image("Screenshot70.png")

    st.title("project2")
    st.image("screenshot1.png")
    
    st.image("Screenshot52.png")

    st.image("Screenshot53.png")

    st.image("Screenshot54.png")

    st.image("Screenshot55.png")

    st.image("Screenshot56.png")
    



# Set up the navigation bar
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ("Home", "About", "Projects", "Contact","image"))

# Route to the corresponding section based on the user selection
if options == "Home":
    home()
elif options == "About":
    about()
elif options == "Projects":
    projects()
elif options == "Contact":
    contact()
elif options == "image":
    image()