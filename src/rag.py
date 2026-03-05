from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

class RAG:
    def __init__(self, directory):
        self.embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
        self.directory = directory   
        self.vector_store = None
        self.PERSIST = './rag_db'

        self._vector_store()

    def _load_docs(self, path):
        loader = DirectoryLoader(
            path,
            glob="**/*.txt",
            loader_cls=TextLoader
        )
        return loader.load()
    
    def _extract_chunks(self):
        docs = self._load_docs(self.directory)
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(docs)
        return chunks
    
    def _vector_store(self):
        chunks = self._extract_chunks()
        self.vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.PERSIST
        )
        return self.vector_store
    
    def retrieve(self, query, top_k=3):
        results = self.vector_store.similarity_search(
            query,
            k=top_k
        )
        return results

        