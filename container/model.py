from abc import ABC, abstractmethod


class BaseIOC(ABC):
    """
    ### IoC Container
    Store dependencies by key-value principe

    @example

    Store dependencie
    ``` python
    container.attach("notificator", notificator)
    ```

    Get from container
    ``` python
    notificator = container.get("notificator")
    ```
    """
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def attach(self, key: str, value) -> None:
        """Attach dependency to container"""
        pass

    @abstractmethod
    def get(self, key: str) -> any:
        """Get dependency in container"""
        pass
