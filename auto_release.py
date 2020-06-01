#!/usr/bin/env python3
import json
import os
import sys

from urllib.parse import urlencode
from urllib.request import Request, urlopen

if __name__ == "__main__":
    owner = sys.argv[1]
    repo = sys.argv[2]
    tag = sys.argv[3]
    upload_file = sys.argv[4]

    token = os.environ['GITHUB_TOKEN']

    api_url_template = f'https://api.github.com/repos/{owner}/{repo}/releases'
    uploads_url_template = f'https://uploads.github.com/repos/{owner}/{repo}/releases'

    # Create.
    _json = json.loads(urlopen(Request(
        api_url_template,
        json.dumps({
            'tag_name': tag,
            'name': tag,
            'prerelease': True,
        }).encode(),
        headers={
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': 'token ' + token,
        },
    )).read().decode())
    release_id = _json['id']
    print(_json)

    # Upload.
    with open(upload_file, 'br') as myfile:
        content = myfile.read()
    _json = json.loads(urlopen(Request(
        uploads_url_template + '/' + str(release_id) + '/assets?'
        + urlencode({'name': os.path.split(upload_file)[1]}),
        content,
        headers={
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': 'token ' + token,
            'Content-Type': 'application/zip',
        },
    )).read().decode())
    print(_json)
