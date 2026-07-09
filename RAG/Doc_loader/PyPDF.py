from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)

# there are many pdf loader and PyPDF loader is one among them, it is to be used when the pdf has mostly text , it is not good to use for scanned pdf
# simple, clean -> PyPDFLoader
# PDFs with tables/columns -> PDFPlumber
# Scanned/image PDFs -> UnstructeredPDFLoader or AmazonTextextractPDFLoader
# need layout and image data -> PyMuPDFLoader
# want best structure extraction  ->  UnstructuredPDFLoader
 