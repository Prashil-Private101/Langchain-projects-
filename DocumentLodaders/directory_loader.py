from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='path/books',
    glob='*/.pdf',
    loader_cls= PyPDFLoader
)

docs = loader.load() #loader.lazy_loader

print(docs[0].page_content)
print(docs[0].metadata)