from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    Unzip_dir:Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model: Path
    update_base_model: Path
    Params_image_size: list
    Params_learning_rate: float
    Params_batch_size: int
    Params_includetop: bool
    Params_weights: str
    Params_class: int

@dataclass(frozen=True)
class CallBackConfig:
    root_dir:Path
    tensorboard_root_log_dir:Path
    checkpoint_model_filepath:Path