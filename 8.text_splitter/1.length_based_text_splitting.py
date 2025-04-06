from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

path = "../7.Document_Loaders/2.PyPDF_loader\BISWAJIT AICH RESUME.pdf"
loader = PyPDFLoader(path)
docs = loader.load()

splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0, separator="")
result = splitter.split_documents(documents=docs)

print(result)
print("\n\n")
for i, item in enumerate(result):
    print(f"[{i+1}]->", item.page_content)
    print("\n")
"""
[Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='BISWAJIT AICH \nAspiring Computer Science Engineer | AI/ML Enthusiast | Full-Stack Developer \nLocatio'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='n: Hooghly, West Bengal, India  Date of Birth: 22 September 2002 \nEmail: biswajitaichofficial@gmail.'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='com  Phone: +916290675574 \nPortfolio: http://biswajitaichportfolio.vercel.app GitHub: https://github'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='.com/BiswajitAich \n1. PROFESSIONAL SUMMARY \nComputer science engineering student with a love for the'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='field and over 2 years of hands-on experience in \nAI/ML and web development. Put more than 4 AI mod'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='els to work in real-world settings making backend \nAPIs run smoother and boosting user satisfaction.'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='Build using full stack. \n2. EDUCATION \nBachelor of Technology in Computer Science and Engineering'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='2022- Present  \nAcademy of Technology, MAKAUT University, Adisaptagram, West Bengal, India \nHigher S'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='econdary Education  2020-2022 \nVivekananda English Academy, WBBHSE, Rishra, West Bengal, India \nSeco'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='ndary Education  2018-2020 \nVivekananda English Academy, WBBSE, Rishra, West Bengal, India \n3. Techn'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='ical Skills \nProgramming Languages: Python, JavaScript, C++, TypeScript, HTML, CSS. \nFrameworks & To'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='ols: Next.js, React.js, Flask, TensorFlow, PyTorch, OpenCV, HTML, CSS, Node.js. \nAI/ML Skills: Natur'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='al Language Processing (NLP), Computer Vision, Deep Learning, Reinforcement Learning. \nAI/ML Tools:'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='TensorFlow, PyTorch, OpenCV, Scikit-learn \nDatabases: MongoDB, MySQL \nVersion Control: Git, GitHub'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='Other: REST APIs, Data Analysis, Software Testing \n4. Key Projects \nConversational Chatbot Using FLA'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='N-T5 \n❖ Built a chatbot using FLAN-T5 to engage in contextual conversations. \n❖ Focused on optimizin'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='g GPU/CPU resources during model training and inference. \n❖ Technologies: Python, TensorFlow, Google'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='Colab \nMultiplayer Rock-Paper-Scissors AI Game \n❖ Developed a YOLO-based (object detection) AI mode'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='l for playing rock-paper-scissors in real time. \n❖ Integrated the model into a live camera-based web'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='site using lightning.ai and NextJs. \n❖ Achieved 90% accuracy in gesture detection during testing. \nJ'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='ewellery Recommendation System \n❖ Built a recommendation engine using cosine similarity to display r'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='elevant jewellery products. \n❖ Deployed in a Next.js framework for a real-time user experience in e-'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='commerce website. \nSOFT SKILLS \nStrong Problem-Solving and Analytical Skills. Team Collaboration and'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='Leadership. Self-Motivation and Time \nManagement \nLANGUAGES \nEnglish: Professional Proficiency (C1)'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='.  Bengali: Native Speaker.  Hindi: Intermediate (B1) \nHOBBIES AND INTERESTS \nCreating art/painting.'), Document(metadata={'producer': 'PyPDF', 'creator': 'Microsoft Word', 'creationdate': '2025-01-27T18:01:27+00:00', 'author': 'Biswajit Aich', 'moddate': '2025-01-27T18:01:27+00:00', 'source': '../7.Document_Loaders/2.PyPDF_loader\\BISWAJIT AICH RESUME.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='Learning about cutting-edge technologies.  Sharing technical knowledge with peers')]



[1]-> BISWAJIT AICH
Aspiring Computer Science Engineer | AI/ML Enthusiast | Full-Stack Developer
Locatio


[2]-> n: Hooghly, West Bengal, India  Date of Birth: 22 September 2002
Email: biswajitaichofficial@gmail.


[3]-> com  Phone: +916290675574
Portfolio: http://biswajitaichportfolio.vercel.app GitHub: https://github


[4]-> .com/BiswajitAich
1. PROFESSIONAL SUMMARY
Computer science engineering student with a love for the


[5]-> field and over 2 years of hands-on experience in
AI/ML and web development. Put more than 4 AI mod


[6]-> els to work in real-world settings making backend
APIs run smoother and boosting user satisfaction.


[7]-> Build using full stack.
2. EDUCATION
Bachelor of Technology in Computer Science and Engineering


[8]-> 2022- Present
Academy of Technology, MAKAUT University, Adisaptagram, West Bengal, India
Higher S


[9]-> econdary Education  2020-2022
Vivekananda English Academy, WBBHSE, Rishra, West Bengal, India
Seco


[10]-> ndary Education  2018-2020
Vivekananda English Academy, WBBSE, Rishra, West Bengal, India
3. Techn


[11]-> ical Skills
Programming Languages: Python, JavaScript, C++, TypeScript, HTML, CSS.
Frameworks & To


[12]-> ols: Next.js, React.js, Flask, TensorFlow, PyTorch, OpenCV, HTML, CSS, Node.js.
AI/ML Skills: Natur


[13]-> al Language Processing (NLP), Computer Vision, Deep Learning, Reinforcement Learning.
AI/ML Tools:


[14]-> TensorFlow, PyTorch, OpenCV, Scikit-learn
Databases: MongoDB, MySQL
Version Control: Git, GitHub


[15]-> Other: REST APIs, Data Analysis, Software Testing
4. Key Projects
Conversational Chatbot Using FLA


[16]-> N-T5
❖ Built a chatbot using FLAN-T5 to engage in contextual conversations.
❖ Focused on optimizin


[17]-> g GPU/CPU resources during model training and inference.
❖ Technologies: Python, TensorFlow, Google


[18]-> Colab
Multiplayer Rock-Paper-Scissors AI Game
❖ Developed a YOLO-based (object detection) AI mode


[19]-> l for playing rock-paper-scissors in real time.
❖ Integrated the model into a live camera-based web


[20]-> site using lightning.ai and NextJs.
❖ Achieved 90% accuracy in gesture detection during testing.
J


[21]-> ewellery Recommendation System
❖ Built a recommendation engine using cosine similarity to display r


[22]-> elevant jewellery products.
❖ Deployed in a Next.js framework for a real-time user experience in e-


[23]-> commerce website.
SOFT SKILLS
Strong Problem-Solving and Analytical Skills. Team Collaboration and


[24]-> Leadership. Self-Motivation and Time
Management
LANGUAGES
English: Professional Proficiency (C1)


[25]-> .  Bengali: Native Speaker.  Hindi: Intermediate (B1)
HOBBIES AND INTERESTS
Creating art/painting.


[26]-> Learning about cutting-edge technologies.  Sharing technical knowledge with peers
"""
