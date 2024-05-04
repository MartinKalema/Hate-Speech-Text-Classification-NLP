from hateSpeechClassifier.logger import logging
from hateSpeechClassifier.exception import CustomException
import sys as system
from hateSpeechClassifier.configuration.gcloud_syncer import GoogleCloudSync
from dotenv import load_dotenv
import os

load_dotenv()

# try:
#     x = 4/"0"
# except Exception as e:
#     raise CustomException(e, system) from e

# gcp = GoogleCloudSync()
# gcp.sync_folder_from_gcloud(os.getenv('GCP_BUCKET_URI'), "artifacts")
