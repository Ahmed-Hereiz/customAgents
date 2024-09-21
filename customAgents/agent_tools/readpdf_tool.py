import PyPDF2
from customAgents.agent_tools import BaseTool


class PDFDocReaderTool(BaseTool):
    def __init__(
            self,
            description: str = "Tool used to read data in pdf",
            tool_name: str = None,
            ):
        
        super().__init__(description, tool_name)
    
    
    def execute_func(self, pdf_path) -> str:
        
        text = ""
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text 
    