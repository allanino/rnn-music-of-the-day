#!/usr/bin/env python
import argparse
import dropbox
import os
from time import gmtime, strftime
import datetime

ANCHOR_OPUS = 132
ANCHOR_DATE = datetime.datetime(2015,12,18,12,0,0)

def get_link(client, folder_path, opus_number):
    folder_metadata = client.metadata(folder_path)
    path = folder_metadata['contents'][opus_number-1]['path']
    url = client.share(path, short_url=False)['url']
    # For streaming to work
    url = url[:-1] + '1'
    return url

def add_post(client, blog_root, date, opus_number, mp3_path, svg_path):
    date = date.strftime('%Y-%m-%d') 
    mp3_url = get_link(client, mp3_path, opus_number)

    img = open(os.path.join(blog_root, 'img', '%d.svg' % opus_number), 'wb')
    with client.get_file(svg_path + '/%d.svg' % opus_number) as f:
        img.write(f.read())

    filename = date + '-opus-%d.md' % opus_number
    post_path = os.path.join(blog_root, '_posts', filename)
    with open(post_path, 'wb') as f:
        s = '---\nlayout: post\ntitle: Opus %d\nimg: %d.svg\nmp3: %s\n---\n'  % (opus_number, opus_number, mp3_url)
        s += '\n{% include post_content.html %}\n'
        f.write(s)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--access-token', '-a', help="Dropbox access token.")
    parser.add_argument('--mp3-path', '-m', help="Dropbox path to MP3 folder.")
    parser.add_argument('--svg-path', '-s', help="Dropbox path to SVG folder.")
    parser.add_argument('--opus-number', '-n', type=int, help="Opus number n. Used to get n.mp3 and n.svg and to set the blog date.")
    parser.add_argument('--blog-root', '-b', default='.', help="Directory to write the new post")
    args = parser.parse_args()

    date = ANCHOR_DATE + datetime.timedelta(days=args.opus_number-ANCHOR_OPUS)
    client = dropbox.client.DropboxClient(args.access_token)
    add_post(client, args.blog_root, date, args.opus_number, args.mp3_path, args.svg_path)
