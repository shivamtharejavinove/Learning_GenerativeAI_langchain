from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.apple.com/in/shop/buy-mac/macbook-air/13-inch-midnight-m5-chip-10-core-cpu-8-core-gpu-16gb-memory-512gb-storage'
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)