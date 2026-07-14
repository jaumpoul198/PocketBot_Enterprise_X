from abc import ABC, abstractmethod


class SecretProvider(ABC):
    """
    Enterprise abstraction for secret retrieval.

    Future implementations:
    - Environment variables
    - Docker secrets
    - Kubernetes secrets
    - Cloud secret managers
    """

    @abstractmethod
    def get_secret(self, key: str) -> str | None:
        """
        Retrieve a secret value.

        Args:
            key: Secret identifier.

        Returns:
            Secret value or None when unavailable.
        """
        raise NotImplementedError
