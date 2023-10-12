from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    DataIngestion is a dataclass that holds the information needed to ingest data into the database.
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
