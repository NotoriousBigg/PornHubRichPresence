import logging
import signal
import sys
import time

import chrome_utils
import scraper
from config import Config
from rpc_client import init_presence, update_presence, clear_presence

logger = logging.getLogger(__name__)
running = True


def signal_handler(signum: int, frame) -> None:
    global running
    logger.info("Received signal %s, shutting down...", signum)
    running = False


def main() -> None:
    global running
    config = Config.load()

    logging.basicConfig(
        level=getattr(logging, config.log_level.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    chrome_path = chrome_utils.find_chrome_path()
    if not chrome_path:
        logger.error("Could not find Chrome/Chromium installation")
        sys.exit(1)

    rpc = init_presence(config.client_id)

    chrome_process = chrome_utils.launch_chrome(
        chrome_path, config.chrome_port, config.resolved_user_data_dir, config.chrome_url
    )

    try:
        while running and chrome_process.poll() is None:
            tabs = chrome_utils.get_tabs(config.chrome_port)
            tab_url = chrome_utils.find_pornhub_tab(tabs)

            if tab_url and rpc:
                html = scraper.get_video_info(tab_url)
                if html:
                    video_info = scraper.get_url_and_description(html)
                    if video_info:
                        update_presence(rpc, video_info)
                    else:
                        clear_presence(rpc)
                else:
                    clear_presence(rpc)
            elif rpc:
                clear_presence(rpc)

            for _ in range(config.poll_interval):
                if not running:
                    break
                time.sleep(1)

    finally:
        logger.info("Cleaning up...")
        if rpc:
            clear_presence(rpc)
        chrome_process.terminate()
        chrome_process.wait(timeout=5)


if __name__ == "__main__":
    main()
