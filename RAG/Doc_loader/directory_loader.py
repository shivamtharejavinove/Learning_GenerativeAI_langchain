from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader('books', glob='*.pdf', loader_cls=PyPDFLoader)  # match actual folder name

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)