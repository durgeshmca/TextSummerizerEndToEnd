from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    DataIngestion is a dataclass that holds the information needed to ingest data .
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    """
    DataValidationConfig is a dataclass that holds the information needed to validate data .
    """
    root_dir : Path
    STATUS_FILE : str
    REQUIRED_FILES : list