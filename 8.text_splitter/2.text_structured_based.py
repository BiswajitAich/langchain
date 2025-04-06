from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
Deep Learning:
Uses artificial neural network architecture to learn hidden patterns and relationships in the dataset.
Requires a larger volume of data compared to machine learning.
Better for complex tasks like image processing, natural language processing, etc.
Takes more time to train the model.
Relevant features are automatically extracted from images, making it an end-to-end learning process.
More complex and works like a black box, making interpretations of results less straightforward.
Requires a high-performance computer with GPU.
Machine Learning:
Applies statistical algorithms to learn hidden patterns and relationships in the dataset.
Can work on a smaller amount of data.
Better for low-label tasks.
Takes less time to train the model.
Relevant features are manually extracted from images to detect an object.
Less complex and easier to interpret the results.
Can work on a CPU or requires less computing power compared to deep learning.
"""

splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=0)

chunks = splitter.split_text(text=text)
print(chunks)
print("\n\n")
for i, item in enumerate(chunks):
    print(f"[{i}]->", item)
    print("\n")

"""
['Deep Learning:\nUses artificial neural network architecture to learn hidden patterns and relationships in the dataset.', 'Requires a larger volume of data compared to machine learning.\nBetter for complex tasks like image processing, natural language processing, etc.', 'Takes more time to train the model.\nRelevant features are automatically extracted from images, making it an end-to-end learning process.', 'More complex and works like a black box, making interpretations of results less straightforward.\nRequires a high-performance computer with GPU.', 'Machine Learning:\nApplies statistical algorithms to learn hidden patterns and relationships in the dataset.\nCan work on a smaller amount of data.', 'Better for low-label tasks.\nTakes less time to train the model.\nRelevant features are manually extracted from images to detect an object.', 'Less complex and easier to interpret the results.\nCan work on a CPU or requires less computing power compared to deep learning.']



[0]-> Deep Learning:
Uses artificial neural network architecture to learn hidden patterns and relationships in the dataset.


[1]-> Requires a larger volume of data compared to machine learning.
Better for complex tasks like image processing, natural language processing, etc.


[2]-> Takes more time to train the model.
Relevant features are automatically extracted from images, making it an end-to-end learning process.


[3]-> More complex and works like a black box, making interpretations of results less straightforward.
Requires a high-performance computer with GPU.


[4]-> Machine Learning:
Applies statistical algorithms to learn hidden patterns and relationships in the dataset.
Can work on a smaller amount of data.


[5]-> Better for low-label tasks.
Takes less time to train the model.
Relevant features are manually extracted from images to detect an object.


[6]-> Less complex and easier to interpret the results.
Can work on a CPU or requires less computing power compared to deep learning.
"""
