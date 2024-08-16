__all__ = ["Container"]

from .model import BaseIOC


class Container(BaseIOC):
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
    def __init__(self) -> None:
        self._container = {}

    def attach(self, key: str, value) -> None:
        self._container[key] = value

    def get(self, key: str) -> any:
        if key not in self._container.keys():
            raise ValueError("invalid key, dependency not found.")

        return self._container[key]

    def __str__(self) -> str:
        return f"Container: {self._container}"
