# WORK IN PROGRESS

# InterfaceLift

![Sample Image][image]

## Downloader

This is a script to mass download wallpapers from [interfacelift.com][interfacelift]

## My fork

Refactored the code using modern tools ([requests][requests], [BeautifulSoup][bs]), but kept the same logic as the [dmacpherson's original script][dmacpherson].

## Instructions

- `git clone`
- `pip install --requirement requirements.txt`
- `python download.py`
- PROFIT. Wallpapers will be downloaded to `wallpapers/` directory.

[image]: http://interfacelift.com/wallpaper/7yz4ma1/03489_fairfieldchurch_1280x720.jpg
[dmacpherson]: https://github.com/dmacpherson/py-interfacelift-downloader/
[interfacelift]: http://interfacelif.com
[requests]: http://docs.python-requests.org/en/latest/
[bs]: http://www.crummy.com/software/BeautifulSoup/
