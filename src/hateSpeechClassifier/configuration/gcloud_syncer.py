import os

class GoogleCloudSync:
    def __init__(self) -> None:
        pass

    def sync_folder_to_gcloud(self, gcp_bucket_uri, filepath):
        command = f"gsutil cp {filepath} gs://{gcp_bucket_uri}"
        os.system(command)

    def sync_folder_from_gcloud(self, gcp_bucket_uri, filepath):
        command = f"gsutil cp gs://{gcp_bucket_uri} {filepath}"
        os.makedirs('artifacts', exist_ok=True)
        os.system(command)