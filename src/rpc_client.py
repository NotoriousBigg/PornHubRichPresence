import logging
from typing import Optional

from pypresence import Presence, ActivityType, StatusDisplayType
from pypresence.exceptions import PyPresenceException

logger = logging.getLogger(__name__)


def init_presence(client_id: str) -> Optional[Presence]:
    try:
        rpc = Presence(client_id)
        rpc.connect()
        logger.info("Connected to Discord Rich Presence")
        return rpc
    except PyPresenceException as e:
        logger.error("Failed to connect to Discord: %s", e)
        return None
    except ConnectionRefusedError as e:
        logger.error("Discord not running? Connection refused: %s", e)
        return None


def update_presence(rpc: Presence, video_info: dict[str, str]) -> None:
    try:
        rpc.update(
            state="Gooning",
            details=video_info["title"],
            large_image="phlogo",
            large_text="PornHub",
            buttons=[{"label": "Watch", "url": video_info["url"]}],
            activity_type=ActivityType.WATCHING,
            status_display_type=StatusDisplayType.STATE,
            name=video_info["title"],
        )
    except PyPresenceException as e:
        logger.error("Failed to update presence: %s", e)


def clear_presence(rpc: Presence) -> None:
    try:
        rpc.clear()
    except PyPresenceException as e:
        logger.error("Failed to clear presence: %s", e)
