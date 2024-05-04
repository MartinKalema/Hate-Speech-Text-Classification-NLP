from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "hateSpeechClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_pusher.py",
    f"src/{project_name}/components/prepare_base_model.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_prepare_base_model.py",
    f"src/{project_name}/pipeline/stage_03_model_training.py",
    f"src/{project_name}/pipeline/stage_04_model_evaluation.py",
    f"src/{project_name}/pipeline/stage_05_prediction.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/entity/artifact_entity.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/configuration/__init__.py",
    f"src/{project_name}/configuration/gcloud_syncer.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "demo.py",
    ".dockerignore",
    "Dockerfile",
    "research/01_data_ingestion.ipynb",
    "research/02_prepare_base_model.ipynb",
    "research/03_model_training.ipynb",
    "research/04_model_evaluation.ipynb",

]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir = filepath.parent
    filename = filepath.name

    if not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        with filepath.open('w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
