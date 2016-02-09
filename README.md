# InterfaceLift Downloader

This is a script to rotate my windows desktop background randomly selected from [interfacelift.com][interfacelift]
I use a cronjob to run this daily and enjoy a new desktop each day

### My fork

Refactored using [oryband's forked script][oryband]. The script now downloads a random wallpaper and sets it to the desktop.

### Instructions

- `git clone`
- `pip install --requirement requirements.txt`
- `python download.py`
- Enjoy. Wallpapers will be cached to `wallpapers/` directory.

[image]: http://interfacelift.com/wallpaper/7yz4ma1/03489_fairfieldchurch_1280x720.jpg
[dmacpherson]: https://github.com/dmacpherson/py-interfacelift-downloader/
[interfacelift]: http://interfacelift.com
[requests]: http://docs.python-requests.org/en/latest/
[bs]: http://www.crummy.com/software/BeautifulSoup/
