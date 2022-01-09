import json
import re
import requests
import argparse
import time

var_re = re.compile('var (.+?) = (.+?);')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('file', help='address file; one address per line')
    ap.add_argument('--coin', required=True, help='e.g. XPM')
    ap.add_argument('--ignore-no-tx', action='store_true')
    args = ap.parse_args()
    for line in open(args.file):
        line_arr = line.split(' ')
        line = line_arr[0]
        line = line.strip()
        print(line)
        r = requests.get('https://www.bitgo.com/api/v1/address/%s' % (line))
        if r.status_code == 404:
            continue
        vs = {}
        print(r.text)
        time.sleep(1)
        #for m in var_re.finditer(r.text):
        #    key, value = m.groups()
        #    if key == 'startTime':
        #        continue
        #    try:
        #        value = json.loads(value.replace('\'', '"'))
        #    except json.JSONDecodeError:
        #        pass
        #    vs[key] = value
        #if args.ignore_no_tx and vs['total_tx'] == 0:
        #    continue

if __name__ == '__main__':
    main()
