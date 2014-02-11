# InterfaceLift Downloader

This is a script to mass download wallpapers from [interfacelift.com][interfacelift]

### My fork

Refactored the code using modern tools ([requests][requests], [BeautifulSoup][bs]), but kept the same logic as the [dmacpherson's original script][dmacpherson]. The script now downloads wallpapers in a single session (instead of multiple ones), downloading wallpapers one after the other, without overloading interfacelift's website. My fork also addresses a bug where a wallpaper would be downloaded partially, causing a "pixelated" or non-viewable image.

### Instructions

- `git clone`
- `pip install --requirement requirements.txt`
- `python download.py`
- PROFIT. Wallpapers will be downloaded to `wallpapers/` directory.

[image]: http://interfacelift.com/wallpaper/7yz4ma1/03489_fairfieldchurch_1280x720.jpg
[dmacpherson]: https://github.com/dmacpherson/py-interfacelift-downloader/
[interfacelift]: http://interfacelift.com
[requests]: http://docs.python-requests.org/en/latest/
[bs]: http://www.crummy.com/software/BeautifulSoup/
