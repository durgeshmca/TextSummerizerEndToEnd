import os
import urllib.request as request
import zipfile
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from TextSummarizer.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url= self.config.source_URL,
                filename= self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info:\n{headers})")
        else:
            logger.info(f"File already exists of size : {get_size(Path(self.config.local_data_file))}, skipping download")

    def extract_zip_file(self):
        """ 
        Extracts the zip file to the local directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted zip file to {unzip_path}")