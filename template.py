import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger((__name__))

project_name = "Project1"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils.common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/entity_config.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    dirname , filename = os.path.split(filepath)

    if dirname != "":
        os.makedirs(dirname, exist_ok=True)
        logger.info(f"Created directory {dirname}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:

            pass
            logging.info(f"Created file {filepath}")
    else:
        logging.info(f"File {filename} already exists")