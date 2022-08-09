import streamlit as st
from PIL import Image

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



image = Image.open('dp.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- UC Berkeley senior with experience in Software Engineering and Data Science. 
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
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
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

#####################
st.markdown('''
## Education
''')

txt('**University of California, Berkeley**', 'Aug 2018 - Dec 2022')

txt('B.A. in Data Science *(Emphasis in Applied Mathematics and Modelling)*',
'')

st.markdown('''
- Relevant Courses: `Machine Learning`, `Data Engineering`, `Data Mining`, `Artificial Intelligence`, `Inference and Decision Theory`, `Data Structures`, `Structure of Computer Programs`, `Linear Algebra and Differential Equations`, `Multivariable Calculus`, `Non-linear and Discrete Optimization`, `Principles of Data Science`, `Economic Modelling`, `Probability`
- Activities and Societies: `DiversaTech Consulting`, `Student Association for Applied Statistics (SAAS)`, `DataGood`, `Intermural Soccer`, `Intermural Basketball`
''')


#####################
st.markdown('''
## Work Experience
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

#####################
st.markdown('''
## Bioinformatics Tools
''')
txt4('ABCpred', 'A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors', 'http://codes.bio/abcpred/')
txt4('AutoWeka', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/chanin-nantasenamat')
txt2('Twitter', 'https://twitter.com/thedataprof')
txt2('GitHub', 'https://github.com/chaninn/')
txt2('', 'https://github.com/chaninlab/')
txt2('', 'https://github.com/dataprofessor')
txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
txt2('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
txt2('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
txt2('Publons', 'https://publons.com/a/303133/')