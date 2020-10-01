#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import re
import requests
import sys


def callAPI(url):
    host = "https://blacklight.api.themarkup.org/"
    payload = '{ "inUrl" : "' + url + '"}'
    headers = {'content-type': 'text/plain;charset=UTF-8'}
    response = requests.request("POST", host, data=payload, headers=headers)
    responseJson = json.loads(response.text)
    if 'error_message' in responseJson.keys():
        print('\033[91m\033[1m[ERROR]\033[0m\033[0m '
              + responseJson['nicer_error_message'])
        exit()
    return responseJson


def printInspectionResult(data):
    for group in data['groups']:
        if 'Blacklight Inspection Result' in group['title']:
            print('> \033[1mInspection result:\033[0m')
            for card in group['cards']:
                if 'bigNumber' in card.keys():
                    print('  \033[93m' + str(card['bigNumber'])
                          + '\033[0m '
                          + card['title'])
                else:
                    mark = '0'
                    if card['testEventsFound']:
                        mark = '!'
                    print('  \033[93m' + mark + '\033[0m ' + card['title'])


def printAdCompany(data):
    for group in data['groups']:
        if 'Some of the ad-tech companies' in group['title']:
            print('> \033[1mAd-tech companies:\033[0m')
            for card in group['cards']:
                print('  \033[93m' + card['title'] + '\033[0m: '
                      + re.sub(r'</?\w+>',
                               '',
                               ', '.join(card['domains_found'])))


def main():
    if len(sys.argv) != 2:
        print('\033[91m\033[1m[ERROR]\033[0m\033[0m Wrong input! '
              + '\nUsage: ./blacklight.py "<url>"')
        exit()

    if sys.argv[1].startswith('http'):
        url = sys.argv[1]
    else:
        url = 'https://' + sys.argv[1]

    data = callAPI(url)
    printInspectionResult(data)
    print()
    printAdCompany(data)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
