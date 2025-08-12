import sys
from pathlib import Path
import fitz
import uuid
from datetime import datetime, timezone
from logger.custom_logger import customLogger
from exception.custom_exception import DocumentPortalException 



class DocumentIngestion:
    """
    Handles saving, reading, and combining of PDFs for comparison with session-based versioning.
    """

    def __init__(self,base_dir="data/data_compare",session_id=None):
        self.logger = customLogger().get_logger(__name__)
        self.base_dir = Path(base_dir)
        self.session_id=session_id or f"session_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
        self.session_path = self.base_dir / self.session_id
        self.session_path.mkdir(parents=True, exist_ok=True)

        self.logger.info("DocumentComparator initialized", session_path=str(self.session_path))

    def save_uploaded_files(self, reference_file, actual_file):
        """
        Save reference and actual PDF files in the session directory.
        """
        try:
            ref_path = self.session_path / reference_file.name
            act_path = self.session_path / actual_file.name

            if not reference_file.name.lower().endswith(".pdf") or not actual_file.name.lower().endswith(".pdf"):
                raise ValueError("Only PDF files are allowed.")
            
            with open(ref_path, "wb") as f:
                f.write(reference_file.getbuffer())

            with open(act_path, "wb") as f:
                f.write(actual_file.getbuffer())

            self.logger.info("Files saved", reference=str(ref_path), actual=str(act_path), session=self.session_id)
            return ref_path, act_path
            
        except Exception as e:
            self.logger.error("Error saving PDF files", error=str(e),session=self.session_id)
            raise DocumentPortalException("Error saving files", sys)

    
    def read_pdf(self,pdf_path:str):
        """
            Reads a PDF file and extracts text from each page
        """
        try:
            with fitz.open(pdf_path) as doc:
                if doc.is_encrypted:
                    raise ValueError(f"PDF is encrypted: {pdf_path.name}")
                all_text=[]
                for page_num in range(doc.page_count):
                    page=doc.load_page(page_num)
                    text=page.get_text()
                    if text.strip():
                        all_text.append(f"\n -- Page {page_num+1} --- \n {text}")
                self.logger.info("PDF read Successfully",file=str(pdf_path),pages=len(all_text))
                return "\n".join(all_text)
        except Exception as e:
            self.log.error(f"Error Reading PDF",error=str(e),session=self.session_id)
            raise DocumentPortalException("Error Reading PDF",sys)
        
    
    def combine_documents(self)->str:
        try:
            content_dict = {}
            doc_parts = []

            for filename in sorted(self.base_dir.iterdir()):
                if filename.is_file() and filename.suffix == ".pdf":
                    content_dict[filename.name] = self.read_pdf(filename)

            for filename, content in content_dict.items():
                doc_parts.append(f"Document: {filename}\n{content}")

            combined_text = "\n\n".join(doc_parts)
            self.logger.info("Documents combined", count=len(doc_parts),session=self.session_id)
            return combined_text

        except Exception as e:
            self.logger.error("Error combining documents", error=str(e),session=self.session_id)
            raise DocumentPortalException("An error occurred while combining documents.", sys)
    

    def clean_old_sessions(self,keep_latest:3):

        """
        Optional method to delete older session folders, keeping only the latest N.
        """
        try:
            session_folders = sorted(
                [f for f in self.base_dir.iterdir() if f.is_dir()],
                reverse=True
            )
            for folder in session_folders[keep_latest:]:
                for file in folder.iterdir():
                    file.unlink()
                folder.rmdir()
                self.log.info("Old session folder deleted", path=str(folder),session=self.session_id)
        except Exception as e:
            self.log.error("Error cleaning old sessions", error=str(e),session=self.session_id)
            raise DocumentPortalException("Error cleaning old sessions", sys)