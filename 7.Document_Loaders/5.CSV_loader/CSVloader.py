from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='inventory.csv')
docs=loader.load()
print(docs[0])

print('\n\n')

for row in docs:
    print(row)
    print('\n\n')