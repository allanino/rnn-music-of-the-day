#!/usr/bin/env python
import argparse
import dropbox
import os
from time import gmtime, strftime

def get_link(client, folder_path, opus_number):
    folder_metadata = client.metadata(folder_path)
    path = folder_metadata['contents'][opus_number-1]['path']
    url = client.share(path, short_url=False)['url']
    # For streaming to work
    url = url[:-1] + '1'
    return url

def add_post(blog_root, date, opus_number, mp3_url):
    filename = date + '-opus-%d.md' % opus_number
    post_path = os.path.join(blog_root, '_posts', filename)
    with open(post_path, 'wb') as f:
        s = '---\nlayout: post\ntitle: Opus %d\nimg: %d.svg\nmp3: %s\n---\n'  % (opus_number, opus_number, mp3_url)
        s += '\n{% include post_content.html %}\n'
        f.write(s)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('access_token', help="Dropbox access token.")
    parser.add_argument('mp3_path', help="Dropbox path to MP3 folder.")
    parser.add_argument('svg_path', help="Dropbox path to SVG folder.")
    parser.add_argument('opus_number', type=int, help="Opus number n. Used to get n.mp3 and n.svg.")
    parser.add_argument('blog_root', help="Directory to write the new post")
    parser.add_argument('--date', help="Date to use on the blog post.")

    args = parser.parse_args()

    client = dropbox.client.DropboxClient(args.access_token)

    mp3_url = get_link(client, args.mp3_path, args.opus_number)

    img = open(os.path.join(args.blog_root, 'img', '%d.svg' % args.opus_number), 'wb')
    with client.get_file(args.svg_path + '/%d.svg' % args.opus_number) as f:
        img.write(f.read())

    if args.date:
        date = args.date
    else:
        date = strftime("%Y-%m-%d", gmtime())

    add_post(args.blog_root, date, args.opus_number, mp3_url)
