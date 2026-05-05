import streamlit as st

from src.infra.db import PostgresCredentialRepository, PostgresWorkflowRepository
from src.application.use_cases import export_all_credentials, export_workflow, list_workflows

workflow_repo = PostgresWorkflowRepository()
credential_repo = PostgresCredentialRepository()

st.title("Generate n8n Workflow JSON from PostgreSQL")

entities = list_workflows(workflow_repo)

if not entities:
    st.warning("No entities found.")
    st.stop()

name_to_id = {name: entity_id for entity_id, name in entities}
selected_name = st.selectbox("Selecciona un workflow:", list(name_to_id.keys()))

if selected_name:
    selected_id = name_to_id[selected_name]

    if st.button("Convertir y Guardar JSON"):
        saved_credentials = export_all_credentials(
            credential_repo, "/workspace/n8n/demo-data/credentials"
        )
        for path in saved_credentials:
            st.write(f"Saved credential: {path}")

        output_path = f"/workspace/n8n/demo-data/workflows/{selected_id}.json"
        success = export_workflow(selected_id, workflow_repo, output_path)

        if success:
            st.success(f"📁 File saved at: `{output_path}`")
        else:
            st.error("No register found.")
