from abc import ABC, abstractmethod
from typing import Optional


class AppRepository(ABC):
    @abstractmethod
    def list_workflows(self) -> list: ...

    @abstractmethod
    def get_workflow_json(self, workflow_id: str) -> Optional[dict]: ...

    @abstractmethod
    def list_credential_ids(self) -> list: ...

    @abstractmethod
    def get_credential_json(self, cred_id: str) -> Optional[dict]: ...
