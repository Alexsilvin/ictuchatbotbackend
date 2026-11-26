from app.services.ictukb import search_knowledge_base
from app.services.ollama import generate_response

SYSTEM_PROMPT = """
You are the official AI assistant of The ICT University.

Your responssibility is to answer questions about The ICT University.

STRICT RULES:
1. Answer using ONLY the university information provided in the retrieved context.
2. Never invent university polocies, tuition fees, deadlines, admission requirements, or any other information and facts.
3. If the context does not conatin the answer, clearly say that you do not have enough verified information to answer the question.
4. Do not use your general training knowledge to fill gaps in unverified information.
5. Be polite, professional, helpful, and concise in your responses.
6. Preserve important figures, dates, and percentages.
7. When appropriate, cite the document titles used to construct your answer.
8. If a document is marked as outdated, warn the user that the information may no longer be current and advise them to verify with the university's official sources.
"""

async def answer_question(question: str):
    
    # Step 1: We retrieve relevant context from the ICT University knowledge base
    retrieval = await search_knowledge_base(question)
    
    confidence = retrieval.get("confidence", "none")
    results = retrieval.get("results", [])
    
    # Step 2: I check retrieval confidence
    if confidence != "high" or not results:
        
        return {
            "answer": (
                "I could not find sufficiently reliable "
                "information to answer your question. "
                "Please consult the official ICT University office for accurate information."
            ),
            "confidence": confidence,
            "sources": []
        }
        
    # Step 3: prepare retrieved university information
    context_parts = []
    sources = []
    
    for item in results:
        
        document = item.get("document", {})
        
        title = document.get("title", "Unknown Document")
        text = item.get("text", "")
        source_url = document.get("source_url")
        last_verified = document.get("last_verified")
        stale = document.get("stale", False)
        
        context_parts.append(
            f"""Documenst: {title}
            Last Verified: {last_verified}
            Potentially Outdated: {stale}
            
            Content: 
            {text}
            """
        )
        
        sources.append({
            "title": title,
            "source_url": source_url,
            "last_verified": last_verified,
            "stale": stale
        })
        
    context = "\n\n".join(context_parts)
    
    # Step 4: prepare the user's(MY) prompt
    user_prompts = f"""
    UNIVERSITY KNOWLEDGE BASE CONTEXT:
    
    {context}
    
    STUDENT QUESTION:
    
    {question}
    
    Answer the student's question using onlu the information provided in the context.
    """
    
    #step 5: generate the final answer using the gemma 
    answer = await generate_response(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompts
    )
    
    #STEP 6: Return the answer and its sources
    return {
        "answer": answer,
        "confidence": confidence,
        "sources": sources
    }