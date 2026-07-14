"""
Downloads the raw pest detection dataset from Roboflow into data/raw/.
Run once: python src/download_dataset.py
"""
import os

from dotenv import load_dotenv
from roboflow import Roboflow

load_dotenv()

rf = Roboflow(api_key=os.environ["ROBOFLOW_API_KEY"])
project = rf.workspace("pest-2bk0e").project("detection-d0qov")
version = project.version(1)
dataset = version.download("yolov8", location="data/raw/pest-detection-v1")

print("Downloaded to:", dataset.location)
