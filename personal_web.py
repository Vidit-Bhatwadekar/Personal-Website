from turtle import width
import streamlit as st
from PIL import Image
from bokeh.models.widgets import Div
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="🚀 Vidit's Porfolio Page 🚀",
    page_icon=":male-technologist:",
)

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


#####################
# Header 
st.write('''
# Vidit Bhatwadekar
''')



image = Image.open('images/circle.png')
st.image(image, width=150)



st.markdown('# Summary', unsafe_allow_html=True)
st.info('''
- UC Berkeley senior with experience in software engineering and data science. 
- Interested in back-end development, data engineering, machine learning, and data science.
- Strong communicator, fast learner, and proficient programmer as demonstrated by various projects, extracurriculars, and internships.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" target="_blank" id="top">Vidit Bhatwadekar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#vidit-bhatwadekar">Summary</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#extracurricular-activities">Extracurricular Activities</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#tech-stack">Tech Stack</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

##################### Education
st.markdown('''
# Education
''')

txt('**University of California, Berkeley**', 'Aug 2018 - Dec 2022')

txt('B.A. in Data Science *(Emphasis in Applied Mathematics and Modelling)*',
'')

st.markdown('''
- Relevant Courses: `Machine Learning`, `Data Engineering`, `Data Mining`, `Artificial Intelligence`, `Inference and Decision Theory`, `Data Structures`, `Structure of Computer Programs`, `Linear Algebra and Differential Equations`, `Multivariable Calculus`, `Non-linear and Discrete Optimization`, `Principles of Data Science`, `Economic Modelling`, `Probability`
- Activities and Societies: `DiversaTech Consulting`, `Student Association for Applied Statistics (SAAS)`, `DataGood`, `Intermural Soccer`, `Intermural Basketball`
''')


##################### Work Experience
st.markdown('''
# Work Experience
''')

txt('**Software Engineer Intern**, Privé Technologies | *Hong Kong S.A.R*',
'Jun 2021 - Aug 2021')
st.markdown('''
- Streamlined the process of client-data-parser testing by `30 mins` by assembling a library of wrapper functions to apply a legacy parser implementation to current client data
- Designed a metric to measure the similarity between parser outputs
- Expedited the process of building a new parser for the client-data-hub team by building a parser comparison tool which utilizes the above metric to compare client-data-parsers
- Aided in the building of future client-data-parsers by writing comprehensive unit tests to ensure the reliability of the parser comparison tool
- Used `Python`, `Git/Github`, `XML`, `Pandas`
''')

txt('**Software & Data Intern**, AtHum | *Remote (United States)*',
'Feb 2020 - Aug 2020')
st.markdown('''
- Assembled a highly accurate straight-line detector `(99% of clearly visible straight lines detected)` by applying the Hough Transform to images using the OpenCV library - this detector was used in the development of an augmented reality apartment designer web application
- Built a set of tools, using pandas, to clean and encode client survey data to be used in the building of a Natural Language Processing model
- Programmed a tool to calculate the thematic "Jaccard Similarity" between descriptions of rooms in survey data
- Assembled an preliminary 30-D Word2Vec model using Keras to use for mean-values in the subsequent building of a Gaussian Mixture Model for thematic room descriptors
- Used `Python`, `Pandas`, `OpenCV`, `ScikitLearn`, `Keras/Tensorflow`, `Docker`
''')

txt('**Software Engineer Intern**, OliveX | *Hong Kong S.A.R*',
'Jun 2019 - Aug 2019')
st.markdown('''
- Improved the performance of a pose-detection computer vision model by `8%` by adapting and upgrading an open-source image tagging software, written in Javascript, to add additional body tagging locations - including a "z-axis" indicator variable
- The above pose-detection computer vision model is used in the company’s proprietary KARA fitness mirror to detect exercise repetitions
- Streamlined the process of training the pose-detection computer vision model by `5 hours` by developing a JSON file parser which combined multiple COCO format JSON datasets
- Used `Javascript`, `Node.js`, `Python`, `Git/Github`
''')

    

##################### Projects

with st.container():
    st.write("---")
    st.markdown("# Projects")
    st.write("##")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("**okbr Meme and Quote Generator**")
        st.write("*A web app, deployed using Heroku, which displays a random meme and quotation from a major Reddit meme page. Used PRAW Reddit API to scrape image and text data from a meme reddit page.* *Used* `Python`, `pandas`, `streamlit`, `heroku`, `PRAW api`")
        if st.button('Enter App', key="ews_enter"):
            js = "window.open('https://okbr-memes.herokuapp.com/')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
        if st.button('Github', key="ews_github"):
            js = "window.open('https://github.com/Vidit-Bhatwadekar/RedditMemeWebApp')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col2:
        st.subheader("**Personal Resume and Portfolio Website (This site)**")
        st.write("*Personal resume and project portfolio website showcasing my projects, extracurriculars and work experience. Used* `Python`, `Streamlit`, `HTML`, `CSS`")
        if st.button('Enter App', key="gee_enter"):
            js = "window.open('')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
        if st.button('Github', key="gee_github"):
            js = "window.open('https://github.com/Vidit-Bhatwadekar/Personal-Website')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    # with col3:
    #     st.subheader("Crypto Currency Watchlist")
    #     st.write("Django web application that shows some basic data of your favourite crypto currencies.")
    #     if st.button('Enter App', key="ccw_enter"):
    #         js = "window.open('https://crypto-watchlist-rather-to.herokuapp.com/')"  # New tab or window
    #         html = '<img src onerror="{}">'.format(js)
    #         div = Div(text=html)
    #         st.write('Web Application opens in new browser tab')
    #         st.bokeh_chart(div)
    #     if st.button('Github', key="ccw_github"):
    #         st.write('Github opens in new browser tab')
    #         js = "window.open('https://github.com/ratherUsefulCode/')"  # New tab or window
    #         html = '<img src onerror="{}">'.format(js)
    #         div = Div(text=html)
    #         st.bokeh_chart(div)



with st.container():
    col4, col5 = st.columns(2)
    with col4:
        st.subheader("**Amazon Web Scraper**")
        st.write("*Built an Amazon Scraper for a start-up called CL1CK which scraped and cleaned over 2500 Amazon reviews and product descriptions and stored it neatly in CSV format. This data was analysed by company to make strategic decisions. Used* `Python`, `Selenium`, `Pandas`")
        if st.button('Github', key="qrc_github"):
            js = "window.open('https://github.com/Vidit-Bhatwadekar/AmazonWebScraper')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col5:
        st.subheader("**Portfolio Website made with Streamlit**")
        st.write("*Used OpenCV Cascade Classifier model to detect faces, eyes, and glasses on the webcam. Can also detect said images in jpg with an accuracy of above 90%. Used* `Python`, `OpenCV`")
        if st.button('Github', key="spw_github"):
            js = "window.open('https://github.com/Vidit-Bhatwadekar/FaceDetection')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    # with col6:
    #     st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
    #     st.subheader("Portfolio Website made with Bootstrap")
    #     st.write("Portfolio Website made with HTML/Bootstrap.")
    #     if st.button('Enter App'):
    #         js = "window.open('https://rather.to')"  # New tab or window
    #         html = '<img src onerror="{}">'.format(js)
    #         div = Div(text=html)
    #         st.bokeh_chart(div)
    #         st.write('Web Application opens in new browser tab')
    #     if st.button('Github', key="bpw_github"):
    #         js = "window.open('https://github.com/ratherUsefulCode/rather-to')"  # New tab or window
    #         html = '<img src onerror="{}">'.format(js)
    #         div = Div(text=html)
    #         st.bokeh_chart(div)

##################### ExtraCurriculars
st.markdown('''
# Extracurricular Activities
''')

txt('#### **DiversaTech Consulting**',
'')

txt('*Project Manager* | Client: Oracle','Spring 2021')
st.markdown(
  '''
  Project Manager for Oracle project involving go-to-market strategy for major product
  - Led a team of 7 consultants in devising a coherent go-to-market-strategy for our client
  - Worked as a liason between points of contact at Oracle and DiversaTech
  - Organised meetings and planned timelines for deliverables
  - Mentored young consultants and aided them in developing new skillsets for future projects
  '''
)

txt('*Consultant*','2019 - 2020')
st.markdown(
  '''
  Strategy consultant for UC Berkeley's premier tech consulting group
  - **Spring 19'** *(Microsoft)*: Conducted user research to aid in the planning of new marketing strategy for major suite of products. Designed and presented a slideshow of our ideas to client. 
  - **Fall 19'** *(Keysight Technologies)*: Tested and proposed UI/UX improvements for major B2B software product.
  - **Spring 20'** *(LinkedIn)*: Blueprinted a major feature launch for our client, LinkedIn - Prototyped ideas using Figma.
  - **Fall 20'** *(Qoakka Brew)*: Designed UI/UX of the iOS app for QuokkaBrew using Figma.
  '''
)

txt('#### **Student Association for Applied Statistics (SAAS)**',
'')
txt('*Data Science Consultant*','Fall 2021')
st.markdown(
  '''
  Data Science consultant for SAAS, working on building marketing mix model and data pipeline for major marketing agency, Media Matters Worldwide.
  - Created functions to clean and engineer features using pandas
  - Tested and evaluated various Machine Learning Models using cross-validation
  - Presented work to client, involving getting into technical details about Machine Learning
  - Built and demoed data pipeline to clients
  - Used `Python`, `pandas`, `scikitlearn`, `matplotlib`, `jupyter`
  - [Presentation](https://drive.google.com/file/d/1LLP7wWIhsKrbEsbJk3cRgQi9IRgR8cGW/view?usp=sharing)
  '''
)

txt('*Data Science Researcher*','Spring 2021')
st.markdown(
  '''
  Worked as Data Science Researcher representing SAAS for a economic/data science project
  - Conducted statistical analysis into the volatility and valuation of the US stock market during the pandemic and other Black Swan Events
  - Compiled research into a write-up and presented in at UC Berkeley's annual ML and Data research symposium
  - Used `Python`, `pandas`, `matplotlib/seaborn`, `R`, FRED Economic Data, Various financial APIs
  - [Write up](https://drive.google.com/file/d/1shzwlccTI4O84qt_cr65aFeRlhVUgSvP/view?usp=sharing) and [Presentation](https://drive.google.com/file/d/1-Asyw-Zfm1SrSJbn-LUhE-iM7pt_rDe5/view?usp=sharing)
  '''
)


#####################
# st.markdown('''
# ## Bioinformatics Tools
# ''')
# txt4('ABCpred', 'A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors', 'http://codes.bio/abcpred/')
# txt4('AutoWeka', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
# txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
# txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
# txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
# txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
# txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
# txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
# txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
# txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
# txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
# txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
# txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
# txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
# txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
# txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
# txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')


##################### Tech Stack
st.markdown('''
# Tech Stack
''')
txt3('Languages', '`Python`, `SQL`, `Java`, `Swift`, `Javascript`, `R`, `HTML`, `CSS`, `Bash`, `LATEX`')
txt3('Libraries & Frameworks', '`pandas`, `Flask`, `scikitlearn`, `matplotlib`, `streamlit`, `seaborn`, `OpenCV`, `Tensorflow/Keras`, `node.js`, `Selenium`, `ggplot2`')
txt3('Tools', '`Git/Github`, `Heroku`, `Docker`, `Postman`, `AWS`, `SQLite`, `Anaconda`')

#####################
st.markdown('''
# Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/vidit-bhatwadekar/')
txt2('GitHub', 'https://github.com/Vidit-Bhatwadekar')
txt2('Instagram', 'https://www.instagram.com/viditbhatwadekar/')



############# Contact

# with st.container():
#     st.write("---")
#     st.markdown("<h2 style='text-align: center;'>Contact</h2>", unsafe_allow_html=True)
#     st.write("##")

#     col1, col2, col3 = st.columns(3)
#     with col2:
#         contact_form = """
#         <form action="https://formsubmit.co/805cc992f02da35ae356f2451ece18be" method="POST">
#             <input type="hidden" name="_captcha" value="true">
#             <input type="text" name="name" placeholder="Your name" required>
#             <input type="email" name="email" placeholder="Your email" required>
#             <textarea name="message" placeholder="Your message" required></textarea>
#             <button type="submit">Send</button>
#         </form>
#         """
#         st.markdown(contact_form, unsafe_allow_html=True)


with st.container():
    for i in range(3):
        st.write("##")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write(
            """
            Feel free to copy this page 👍
            """
        )
    with col2:
        st.markdown("<p style='text-align: right;'>Made in 2022 with Python, Streamlit, HTML and CSS</p>", unsafe_allow_html=True)
    st.write("---")