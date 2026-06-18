import logging
import os
import shutil
import subprocess
import sys
from typing import Optional

import requests

logger = logging.getLogger(__name__)


def find_chrome_path() -> Optional[str]:
    if sys.platform == "win32":
        possible_paths = [
            os.path.join(os.environ.get("PROGRAMFILES", ""), "Google\\Chrome\\Application\\chrome.exe"),
            os.path.join(os.environ.get("PROGRAMFILES(X86)", ""), "Google\\Chrome\\Application\\chrome.exe"),
            os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google\\Chrome\\Application\\chrome.exe"),
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path

    elif sys.platform == "darwin":
        mac_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        if os.path.exists(mac_path):
            return mac_path

    else:
        for name in ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]:
            path = shutil.which(name)
            if path:
                return path

    return None


def launch_chrome(chrome_path: str, port: int, user_data_dir: str, url: str) -> subprocess.Popen:
    os.makedirs(user_data_dir, exist_ok=True)
    command = [
        chrome_path,
        f"--remote-debugging-port={port}",
        f"--user-data-dir={user_data_dir}",
        url,
    ]
    logger.info("Launching Chrome: %s", command)
    return subprocess.Popen(command)


def get_tabs(port: int) -> list[dict]:
    try:
        response = requests.get(f"http://localhost:{port}/json/list", timeout=5)
        return response.json()
    except requests.RequestException as e:
        logger.warning("Failed to fetch tabs: %s", e)
        return []


def find_pornhub_tab(tabs: list[dict]) -> Optional[str]:
    for tab in tabs:
        url = tab.get("url", "")
        if "www.pornhub.com" in url and "/view_video.php" in url:
            return url
    return None
