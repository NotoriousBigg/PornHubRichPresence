import json
import os
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Config:
    client_id: str = "1478206867451805826"
    chrome_port: int = 6000
    poll_interval: int = 15
    chrome_url: str = "https://pornhub.com/"
    chrome_user_data_dir: Optional[str] = None
    log_level: str = "INFO"

    @classmethod
    def load(cls, path: Optional[str] = None) -> "Config":
        if path is None:
            path = os.path.join(os.path.dirname(__file__), "config.json")
        if os.path.exists(path):
            with open(path) as f:
                data = json.load(f)
            return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})
        return cls()

    @property
    def resolved_user_data_dir(self) -> str:
        if self.chrome_user_data_dir:
            return self.chrome_user_data_dir
        if os.name == "nt":
            return r"C:\chrome-debug"
        return os.path.expanduser("~/chrome-debug")
