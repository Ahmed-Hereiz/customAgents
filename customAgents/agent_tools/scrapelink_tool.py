import time
import requests
from bs4 import BeautifulSoup # type: ignore
from typing import Any
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from customAgents.agent_tools import BaseTool
from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.document_loaders import AsyncHtmlLoader


class ScrapeLinkTool(BaseTool):
    def __init__(
            self,
            description: str,
            tool_name: str = None,
            max_num_chars: int = 5000
        ):

        self.max_num_chars = max_num_chars
        self.description = description
        self.tool_names = tool_name
        self.max_num_chars = max_num_chars
        self.headers = {
          "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
           }

        super().__init__(description, tool_name)


    def execute_func(self, url: str) -> str:
        try:
            urls = [url]
            loader = AsyncHtmlLoader(urls)
            docs = loader.load()
            html2text = Html2TextTransformer()
            docs_transformed = html2text.transform_documents(docs)
            text = docs_transformed[0].page_content
            text = ' '.join(text.split())
            return text[:self.max_num_chars]
        except Exception as e:
            return f"Error scraping URL: {str(e)}"
    

class ScrapeStaticLinkTool(ScrapeLinkTool):
    def __init__(self, description: str, tool_name: str = None, max_num_chars: int = 5000):
        super().__init__(description, tool_name, max_num_chars)

    def _scrape(self, docs) -> str:
        try:
            html2text = Html2TextTransformer()
            docs_transformed = html2text.transform_documents(docs)
            text = docs_transformed[0].page_content
            text = ' '.join(text.split())
            return text[:self.max_num_chars]
        except Exception as e:
            return f"Error processing content: {str(e)}"

    def execute_func(self, url: str) -> str:
        try:
            urls = [url]
            loader = AsyncHtmlLoader(urls)
            docs = loader.load()
            return self._scrape(docs)
        except Exception as e:
            return f"Error scraping static URL: {str(e)}"
    

# class ScrapeDynamicLinkTool(ScrapeStaticLinkTool):
#     def __init__(self, description: str, service: str="/usr/bin/chromedriver", tool_name: str = None, max_num_chars: int = 5000):
#         super().__init__(description, tool_name, max_num_chars)
#         self.service = service

#     def execute_func(self, url: str) -> str:
#         try:
#             service = Service(self.service)
#             driver = webdriver.Chrome(service=service)
#             # options.add_argument('--headless') 
#             # options.add_argument('--no-sandbox')
#             # options.add_argument('--disable-dev-shm-usage')
            
#             driver.get(url)
#             time.sleep(5)  
#             page_source = driver.page_source
#             driver.quit()

#             return self._scrape(page_source)
#         except Exception as e:
#             return f"Error scraping dynamic URL: {str(e)}"


class ScrapeDynamicLinkTool(ScrapeStaticLinkTool):
    def __init__(self, description: str, service: str="/usr/bin/chromedriver", tool_name: str = None, max_num_chars: int = 5000):
        self.service = service
        super().__init__(description, tool_name, max_num_chars)

    def execute_func(self, url: str) -> str:
        try:
            service = Service(self.service)
            driver = webdriver.Chrome(service=service)

            driver.get(url)
            time.sleep(5)  
            page_source = driver.page_source
            driver.quit()

            return self._scrape(page_source)
        
        except Exception as e:
            return f"Error scraping dynamic URL: {str(e)}"


if __name__ == "__main__":
    # Test static scraping
    # static_scraper = ScrapeLinkTool("Test static scraping")
    # static_url = "https://github.com/Ahmed-Hereiz"
    # print("\nTesting static scraping...")
    # print(f"URL: {static_url}")
    # print("Result:", static_scraper.execute_func(static_url))

    # Test dynamic scraping 
    dynamic_scraper = ScrapeDynamicLinkTool("Test dynamic scraping")
    dynamic_url = "https://github.com/Ahmed-Hereiz" # Replace with actual dynamic site
    print("\nTesting dynamic scraping...")
    print(f"URL: {dynamic_url}")
    print("Result:", dynamic_scraper.execute_func(dynamic_url))
