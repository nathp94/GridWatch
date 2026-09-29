from google.cloud import bigquery


PROJECT_ID = "gridwatch-510021"
BUCKET_NAME = "gridwatch-data"

GCS_URI = (
    "gs://gridwatch-data/"
    "raw/rte/eco2mix-regional-cons-def/"
    "backfill/eco2mix-regional-cons-def.csv"
)

TABLE_ID = f"{PROJECT_ID}.raw.eco2mix_regional_cons_def"


SCHEMA = [
    bigquery.SchemaField("code_insee_region", "STRING"),
    bigquery.SchemaField("region", "STRING"),
    bigquery.SchemaField("nature", "STRING"),
    bigquery.SchemaField("date", "STRING"),
    bigquery.SchemaField("heure", "STRING"),
    bigquery.SchemaField("date_heure", "STRING"),
    bigquery.SchemaField("consommation_mw", "STRING"),
    bigquery.SchemaField("thermique_mw", "STRING"),
    bigquery.SchemaField("nucleaire_mw", "STRING"),
    bigquery.SchemaField("eolien_mw", "STRING"),
    bigquery.SchemaField("solaire_mw", "STRING"),
    bigquery.SchemaField("hydraulique_mw", "STRING"),
    bigquery.SchemaField("pompage_mw", "STRING"),
    bigquery.SchemaField("bioenergies_mw", "STRING"),
    bigquery.SchemaField("ech_physiques_mw", "STRING"),
    bigquery.SchemaField("stockage_batterie", "STRING"),
    bigquery.SchemaField("destockage_batterie", "STRING"),
    bigquery.SchemaField("eolien_terrestre", "STRING"),
    bigquery.SchemaField("eolien_offshore", "STRING"),
    bigquery.SchemaField("tco_thermique_pct", "STRING"),
    bigquery.SchemaField("tch_thermique_pct", "STRING"),
    bigquery.SchemaField("tco_nucleaire_pct", "STRING"),
    bigquery.SchemaField("tch_nucleaire_pct", "STRING"),
    bigquery.SchemaField("tco_eolien_pct", "STRING"),
    bigquery.SchemaField("tch_eolien_pct", "STRING"),
    bigquery.SchemaField("tco_solaire_pct", "STRING"),
    bigquery.SchemaField("tch_solaire_pct", "STRING"),
    bigquery.SchemaField("tco_hydraulique_pct", "STRING"),
    bigquery.SchemaField("tch_hydraulique_pct", "STRING"),
    bigquery.SchemaField("tco_bioenergies_pct", "STRING"),
    bigquery.SchemaField("tch_bioenergies_pct", "STRING"),
    bigquery.SchemaField("column_30", "STRING"),
]


def main():
    client = bigquery.Client(project=PROJECT_ID)

    job_config = bigquery.LoadJobConfig(
        schema=SCHEMA,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        field_delimiter=";",
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )

    print(f"Chargement de {GCS_URI}")
    print(f"vers {TABLE_ID}...")

    load_job = client.load_table_from_uri(
        GCS_URI,
        TABLE_ID,
        job_config=job_config,
    )

    load_job.result()

    table = client.get_table(TABLE_ID)

    print("Chargement terminé.")
    print(f"Nombre de lignes : {table.num_rows}")
    print(f"Nombre de colonnes : {len(table.schema)}")


if __name__ == "__main__":
    main()