
#### PornHubRichPresence - A Discord Rich Presence Client
![Rich Presence Example](https://i.imgur.com/U9ys13R.png)

## System Requirements
 - [Google Chrome](https://www.google.com/chrome/index.html)
 - [Python 3](https://www.python.org/downloads/) (Manual installation only)
 - [Discord Desktop](https://discord.com/download) (Web will not work)

## Quick Start
**Automatic (Linux/macOS)**
 - Download and unzip this repository
 - Run `./run.sh`

**Manual**
 - Download and unzip this repository
 - Navigate to `/src` in your terminal / command prompt
 - Install requirements with `pip install -r requirements.txt`
 - Run the program `python main.py`

**Automatic (Windows)**
 - [Download](https://github.com/TPD94/PornHubRichPresence/releases/download/win-x64/PHRichPresence.exe) the windows release
 - Run and watch!

## Configuration
Optional: create `src/config.json` to override defaults:
```json
{
  "client_id": "1478206867451805826",
  "poll_interval": 15,
  "chrome_port": 6000
}
```

### Begin watching!
A chrome debug window will open automatically to PornHub, just begin watching and your rich presence should now update with whatever video you choose to watch! Now your friends can get some inspiration too! When (your) finished browsing and watching simply close the window or press Ctrl+C and your rich presence will be cleared and the script will stop.

<!-- **KNOWN LIMITATIONS** -->

<!--  `- Can't detect active tab if more than one video is open in your browser` -->
<!--  This is fixed, it now updates the active tab to your discord activity tab(Tested)-->

 **Made for**
![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white)
