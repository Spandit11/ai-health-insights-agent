from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class VectorService:

    def __init__(self):

        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.index = None
        self.chunks = []

    def create_chunks(
        self,
        text,
        chunk_size=700,
        overlap=100
    ):

        chunks = []

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunks.append(
                text[start:end]
            )

            start += (
                chunk_size - overlap
            )

        return chunks

    def build_index(
        self,
        text
    ):

        self.chunks = self.create_chunks(
            text
        )

        embeddings = (
            self.embedding_model.encode(
                self.chunks
            )
        )

        embeddings = np.array(
            embeddings,
            dtype=np.float32
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            embeddings
        )

    def search(
        self,
        query,
        top_k=3
    ):

        query_embedding = (
            self.embedding_model.encode(
                [query]
            )
        )

        query_embedding = np.array(
            query_embedding,
            dtype=np.float32
        )

        distances, indices = (
            self.index.search(
                query_embedding,
                top_k
            )
        )

        results = []

        for idx in indices[0]:

            if idx < len(self.chunks):

                results.append(
                    {
                        "chunk_id": int(idx),
                        "content": self.chunks[idx]
                    }
                )

                return {
            "results": results,
            "score": float(
                distances[0][0]
            )
}