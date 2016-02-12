#!/usr/bin/env python
import os
import os.path
import requests
import re
import ctypes

from BeautifulSoup import BeautifulSoup
from itertools import count
from random import randint, seed
from time import sleep


SAVE_DIR          = 'wallpapers'
RESOLUTION        = '3840x2160'
RESOLUTION_PREFIX = 'wide_16:9'  # URL Prefix for filtering by resolution.
START_PAGE        = 1  # Page number to start downloading from. Keep this on '1' if you want to download everything at the current resolution.


SPI_SETDESKWALLPAPER = 20

def get_backgrounds():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    path = os.path.abspath(SAVE_DIR)

    pattern = re.compile(r'/wallpaper/.*jpg')

    # Sometimes interfacelift closes the connection, so we have to reconnect.
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=3)
    session.mount('http://', adapter)

    # Interfacelift blocks non-browser requests.
    session.headers = {'User-Agent':  'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)'}

    try:
        c = 0
        for page in count(START_PAGE):
            downloaded, carry_on = get_images_from_page(
                'http://interfacelift.com/wallpaper/downloads/random/%s/%s/index%s.html' % (
                    RESOLUTION_PREFIX, RESOLUTION, page),
                 session, pattern, path)
            c += downloaded
            if not carry_on:
                break;
    finally:
        session.close()

    return c


def get_images_from_page(url, session, pattern, path):
    soup = BeautifulSoup(session.get(url).text)
    wallpapers = soup.findAll('a', href=pattern)

    # Stop if no wallpapers on page.
    if not wallpapers:
        print 'Reached an empty page, stopping.'
        return 0, False
    else:
        c = 0
        for link in wallpapers:
            href = 'http://interfacelift.com%s' % link['href']
            wallpaper = href[href.rfind('/')+1:]
            save_to = '%s/%s' % (path, wallpaper)
            exists = os.path.isfile(save_to)

            if exists:
                print "%s already downloaded, stopping." % wallpaper
            elif not exists:
                response = session.get(href)
                with open(save_to, 'wb') as f:
                    f.write(response.content)
                c += 1
                print wallpaper


            cs = ctypes.c_buffer(save_to)
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, cs, 0)
            return 1, False

            # Random break between wallpapers.
            sleep(randint(2, 5))

    sleep(randint(2, 5))
    return c, True


if __name__ == '__main__':
    seed()
    c = get_backgrounds()

    # Summary
    print '\n%s' % (lambda c: 'Downloaded %d new wallpaper%s.' % (
        c, (lambda c: 's' if c>1 else '')(c))
        if c>0 else 'No new wallpapers were downloaded.')(c)
