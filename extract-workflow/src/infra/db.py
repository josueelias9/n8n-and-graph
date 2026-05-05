import os
from typing import Optional

import psycopg2
from dotenv import load_dotenv

from src.application.ports import AppRepository

load_dotenv()

_conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)


def _row_to_json(table: str, row_id, id_column: str = "id") -> Optional[dict]:
    with _conn.cursor() as cur:
        cur.execute(
            f"SELECT row_to_json(t) FROM (SELECT * FROM {table} WHERE {id_column} = %s) t",
            (row_id,),
        )
        result = cur.fetchone()
        return result[0] if result else None


class PostgresRepository(AppRepository):
    def list_workflows(self) -> list:
        with _conn.cursor() as cur:
            cur.execute("SELECT id, name FROM workflow_entity ORDER BY name")
            return cur.fetchall()

    def get_workflow_json(self, workflow_id: str) -> Optional[dict]:
        return _row_to_json("workflow_entity", workflow_id)

    def list_credential_ids(self) -> list:
        with _conn.cursor() as cur:
            cur.execute("SELECT id FROM credentials_entity")
            return [row[0] for row in cur.fetchall()]

    def get_credential_json(self, cred_id: str) -> Optional[dict]:
        return _row_to_json("credentials_entity", cred_id)
