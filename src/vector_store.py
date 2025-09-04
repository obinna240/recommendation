from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

class VectorStoreBuilder:

    # This constructor takes the csv path of the newly created csv
    # the persist directory for the vector store - Chroma
    # and an embedding algorithm from Hugging face
    def __init__(self, csv_path:str, persist_dir:str="chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2") #similar to a final var in Java

    # Here we create the vector store
    def build_and_save_vectorstore(self):
        #load the csv
        loader = CSVLoader(
            file_path = self.csv_path,
            encoding = 'utf-8',
            metadata_columns = []
        )

        #load the csv
        data = loader.load()

        #split the text into chunks 
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = splitter.split_documents(data)

        #convert to embeddings using the embeddings model from hugging face that 
        # is passed in the constuctor
        db = Chroma.from_documents(texts, 
                                   self.embedding, 
                                   persist_directory=self.persist_dir)
        #persist the embeddings
        db.persist()

    # Load the vector store afterwards
    def load_vector_store(self):
        return Chroma(persist_directory=self.persist_dir, embedding_functions=self.embedding)
