from typing import Any

class ArticleLogger:
    FORMAT: str = ...
    LOG_FNAME: str = ...
    file_handler: Any = ...
    stream_handler: Any = ...
    logger: Any = ...
    def __init__(self, NAME: str) -> None: ...
    def debug(self, MSG: str) -> None: ...
    def warning(self, MSG: str) -> None: ...
    def critical(self, MSG: str) -> None: ...
    def error(self, MSG: str) -> None: ...
