from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from .rag import RAG
from .llm import ask_llm

class AskRequest(BaseModel):
    query: str

class Response(BaseModel):
    answer: str
    source: str

router = APIRouter()

rag_system = RAG(directory="./data")

@router.post("/ask", response_model=Response)
def ask(request: AskRequest):
    try:
        docs = rag_system.retrieve(request.query)

        if not docs:
            return Response(
                answer="I couldn't find relevant information in the documents.", 
                source="None"
            )
        
        context = "\n\n".join([doc.page_content for doc in docs])
        top_source_path = docs[0].metadata.get("source", "Unknown")
        top_source_name = os.path.basename(top_source_path)
    
        answer = ask_llm(query=request.query, context=context)
        
        return Response(answer=answer, source=top_source_name)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))