import os
import sys
from zipfile import ZipFile
from hateSpeechClassifier.logger import logging
from hateSpeechClassifier.exception import CustomException
from hateSpeechClassifier.configuration.gcloud_syncer import GoogleCloudSync
from hateSpeechClassifier.entity.config_entity import DataIngestionConfig
from hateSpeechClassifier.entity.artifact_entity import DataIngestionArtifacts



class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.gcloud = GoogleCloudSync()

    def get_data_from_gcloud(self) -> None:
        try:
            logging.info("Entered the get_data_from_gcloud method of Data Ingestion Class")
            self.gcloud.sync_folder_from_gcloud(self.data_ingestion_config.BUCKET_NAME, self.data_ingestion_config.ZIP_FILE_NAME, self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR)

            logging.info("Exited the get_data_from_gcloud method of the data ingestion class")
        except Exception as e:
            raise CustomException(e, sys) from e