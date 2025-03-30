from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader=DirectoryLoader(path='pdfs', glob='*.pdf', loader_cls=PyPDFLoader)

# Egar Loading -----------------------------------
# docs = loader.load()
# print(docs)

# print('\n\n')

# print(docs[1].metadata)
# print(docs[1].page_content)


# Lazy Loading -----------------------------------
docs=loader.lazy_load()

for doc in docs:
    print('page_content: ',len(doc.page_content))
    print(doc.metadata)