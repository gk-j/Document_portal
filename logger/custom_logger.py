import os
import logging
from datetime import datetime
class customLogger:

    def __init__(self):
        # making sure logs directory exists
        self.log_dir=os.path.join(os.getcwd(),"logs")
        os.makedirs(self.log_dir,exist_ok=True)
        print("PATHhHHHHHH",os.getcwd())
        # creating timestamped files
        log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        log_file_path=os.path.join(self.log_dir,log_file)

        # configure logging
        logging.basicConfig(
            filename=log_file_path,
            format="[%(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
            level=logging.INFO
        )

    def get_logger(self,name=__file__):
        return logging.getLogger(os.path.basename(name))
    
if __name__=="__main__":
        logger=customLogger().get_logger(__file__)
        logger.info("Custom Logger initialized")
