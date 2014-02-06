#!/usr/bin/env python
import os
import os.path
import requests
import re

from BeautifulSoup import BeautifulSoup as bs
from random import randint, seed
from time import sleep


SAVE_DIR       = 'wallpapers'
RESOLUTION     = '1920x1080'
STOP_IF_EXISTS = True  # Set to False to download all files even if the file exists and True to stop when it finds where it left off.


def get_backgrounds():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    base = 'http://interfacelift.com/wallpaper/downloads/date/widescreen/%s/index%s.html'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)'
    pattern = re.compile(r'/wallpaper/.*jpg')
    path = os.path.abspath(SAVE_DIR)

    c = 0
    for page in xrange(1, 99999):
        downloaded, carry_on = get_images_from_page(base % (RESOLUTION, page), user_agent, pattern, path)
        c += downloaded
        if not carry_on:
            break;

    return c

def get_images_from_page(url, user_agent, pattern, path):
    soup = bs(requests.get(url, headers={'User-Agent': user_agent}).text)
    wallpapers = soup.findAll('a', href=pattern)

    # Stop if we no wallpapers on page.
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

            if exists and STOP_IF_EXISTS:
                print "%s already downloaded, stopping." % wallpaper
                return c, False
            elif not exists:
                r = requests.get(href, headers={'User-Agent': user_agent})
                with open(save_to, 'wb') as f:
                    f.write(r.content)
                c += 1
                print wallpaper

            sleep(randint(5, 10))

    sleep(randint(5, 10))
    return c, True


if __name__ == '__main__':
    seed()
    c = get_backgrounds()
    print '\n%s' % (lambda c: 'Downloaded %d new wallpaper%s.' % (
        c, (lambda c: 's' if c>1 else '')(c))
        if c>0 else 'No new wallpapers were downloaded.')(c)
