from abc import ABC, abstractmethod
from typing import Optional


class WorkflowRepository(ABC):
    @abstractmethod
    def list_all(self) -> list: ...

    @abstractmethod
    def get_json(self, workflow_id: str) -> Optional[dict]: ...


class CredentialRepository(ABC):
    @abstractmethod
    def list_all_ids(self) -> list: ...

    @abstractmethod
    def get_json(self, cred_id: str) -> Optional[dict]: ...
