import json
from typing import Optional
from src.application.ports import AppRepository


def list_workflows(repo: AppRepository) -> list:
    return repo.list_workflows()


def export_workflow(workflow_id: str, repo: AppRepository, output_path: str) -> bool:
    data = repo.get_workflow_json(workflow_id)
    if not data:
        return False
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return True


def export_all_credentials(repo: AppRepository, output_dir: str) -> list[str]:
    saved = []
    for cred_id in repo.list_credential_ids():
        data = repo.get_credential_json(cred_id)
        if data:
            path = f"{output_dir}/{cred_id}.json"
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            saved.append(path)
    return saved
