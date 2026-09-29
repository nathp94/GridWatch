from pathlib import Path

from google.cloud import storage


PROJECT_ID = "gridwatch-510021"
BUCKET_NAME = "gridwatch-data"

CSV_PATH = Path("data/eco2mix-regional-cons-def.csv")

GCS_OBJECT_NAME = (
    "raw/rte/eco2mix-regional-cons-def/"
    "backfill/"
    "eco2mix-regional-cons-def.csv"
)


def main():
    if not CSV_PATH.exists():
        raise FileNotFoundError(
            f"Fichier introuvable : {CSV_PATH}"
        )

    client = storage.Client(project=PROJECT_ID)

    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(GCS_OBJECT_NAME)

    print("Upload du CSV vers GCS...")

    blob.upload_from_filename(CSV_PATH)

    print("Upload terminé.")
    print(
        f"gs://{BUCKET_NAME}/{GCS_OBJECT_NAME}"
    )


if __name__ == "__main__":
    main()