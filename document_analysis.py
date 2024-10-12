import openai
from config import OPENAI_API_KEY, OPENAI_API_BASE, OPENAI_API_VERSION

class DocumentAnalyzer:
    def __init__(self):
        openai.api_type = "azure"
        openai.api_key = OPENAI_API_KEY
        openai.api_base = OPENAI_API_BASE
        openai.api_version = OPENAI_API_VERSION

    def analyze_document(self, document_content):
        prompt = f"Analyze the following document and provide key insights:\n\n{document_content}"
        try:
            response = openai.chat.completions.create(
                        model="gpt-3.5-turbo",
                 messages=[
             {"role":"user","content":prompt}],
            max_tokens=150,
         n=1,
         stop=None,
         temperature=0.7,
            )
            analysis = response.choices[0].message.content.strip()
            print(f"Document Analysis: {analysis}")
            return analysis
        except Exception as e:
            print(f"Error in document analysis: {e}")
            return None
