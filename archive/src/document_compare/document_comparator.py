import sys
from dotenv import load_dotenv
import pandas as pd
from logger.custom_logger import customLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from prompt.prompt_library import PROMPT_REGISTRY
from utils.model_loader import ModelLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

class DocumentComparator:
    def __init__(self):
        try:
            load_dotenv()
            self.logger = customLogger().get_logger(__name__)
            self.loader = ModelLoader()
            self.llm = self.loader.load_llm()
            self.parser = JsonOutputParser(pydantic_object=SummaryResponse)
            self.fixingparser = OutputFixingParser.from_llm(parser=self.parser,llm=self.llm)
            self.prompt = PROMPT_REGISTRY.get('document_comparision')
            self.chain = self.prompt | self.llm | self.fixingparser
            self.logger.info("DocumentComparator Initialized Successfully with model and parser")  
        except Exception as e:
            self.logger.error(f"DocumentComparator Initialization Failed: {e}")
            raise DocumentPortalException("DocumentComparator Initialization Failed",sys)

    def compare_documents(self,combined_docs:str)-> pd.DataFrame:
        """
          Compare two documents and returns a structured comparision
        """
        try:
            inputs = {
                "combined_docs": combined_docs,
                'format_instructions': self.parser.get_format_instructions()
            }
            self.logger.info("Invoking document comparison LLM chain")
            response = self.chain.invoke(inputs)
            self.logger.info("Chain invoked successfully", response_preview=str(response)[:200])
            return self._format_response(response)
        except Exception as e:
            self.logger.error(f"Error Comparing Documnets: {e}")
            raise DocumentPortalException("Error Comparing Documnets",sys)

    def _format_response(self,response_parsed: list[dict])->pd.DataFrame:
        """
          Formats the response from the llm into a structured format
        """
        try:
            df = pd.DataFrame(response_parsed)
            return df
        except Exception as e:
            self.logger.error(f"Error Formating response into DataFrame: {e}")
            raise DocumentPortalException("Error Formating response into DataFrame",sys)
