from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader(file_path='BISWAJIT AICH RESUME.pdf')
docs=loader.load()
print(docs)

