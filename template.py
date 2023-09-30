import os
from pathlib import Path #windows path for folder/file
import logging


logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

package_name= "CNNClassifier"

# write code for create folder structure
list_of_files=[
   ".github/workflows/.gitkeep", # github is a folder name
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/components/__init__.py", 
   f"src/{package_name}/utils/__init__.py", 
   f"src/{package_name}/config/__init__.py", 
   f"src/{package_name}/pipeline/__init__.py", 
   f"src/{package_name}/entity/__init__.py", 
   f"src/{package_name}/constants/__init__.py",
   "tests/__init__.py", # tests is folder name
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "configs/config.yaml",
   "params.yaml",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt", # its development envronment
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "research/trials.ipynb", 
                ]
# write code for create all above folder 
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    #creating filedir,filename
    if filedir !="": # file dir is not empty
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")
    # it will created all folders like src, tests,github,etc   