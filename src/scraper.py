import logging
from typing import Optional

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def get_video_info(tab_url: str) -> Optional[str]:
    try:
        response = requests.get(tab_url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logger.error("Failed to fetch video page: %s", e)
        return None


def parse_video_info(html: str) -> Optional[dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    og_tags = soup.find_all("meta", property=lambda x: x and x.startswith("og:"))
    og_data: dict[str, str] = {}
    for tag in og_tags:
        property_name = tag.get("property")
        content = tag.get("content")
        if property_name and content:
            og_data[property_name] = content
    if not og_data:
        logger.warning("No Open Graph tags found on page")
        return None
    return og_data


def get_url_and_description(html: str) -> Optional[dict[str, str]]:
    info = parse_video_info(html)
    if info is None:
        return None
    title = info.get("og:title")
    url = info.get("og:url")
    if not title or not url:
        logger.warning("Missing og:title or og:url in page metadata")
        return None
    return {"title": title, "url": url}
