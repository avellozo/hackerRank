#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import json

#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

url_address_team1 = 'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}'
url_address_team2 = 'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}'


def getGoalsTeamUrl(team, year, url):
    total_page = 1
    page = 1
    ret = 0
    while page <= total_page:
        url_request = url.format(year=year, team=team, page=page)
        response = requests.get(url_request).json()
        data = response['data']
        for item in data:
            if item['team1'] == team:
                ret += int(item['team1goals'])
            elif item['team2'] == team:
                ret += int(item['team2goals'])
        page += 1
        total_page = response['total_pages']
    return ret


def getTotalGoals(team, year):
    # total_page = 1
    # page = 1
    # ret = 0
    # url_request = 'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}'
    # while page <= total_page:
    #     url = url_request.format(year=year, team=team, page=page)
    #     response = requests.get(url).json()
    #     data = response['data']
    #     for item in data:
    #         ret += int(item['team1goals'])
    #     page += 1
    #     total_page = response['total_pages']
    #
    # total_page = 1
    # page = 1
    # url_request = 'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}'
    # while page <= total_page:
    #     url = url_request.format(year=year, team=team, page=page)
    #     response = requests.get(url).json()
    #     data = response['data']
    #     for item in data:
    #         ret += int(item['team2goals'])
    #     page += 1
    #     total_page = response['total_pages']
    #
    # return ret
    return getGoalsTeamUrl(team, year, url_address_team1) + getGoalsTeamUrl(team, year, url_address_team2)


# Write your code here


if __name__ == '__main__':
    #    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #    team = input()
    #    year = int(input().strip())
    team = 'monaco'
    year = 2013

    result = getTotalGoals(team, year)
    print(result)
#    fptr.write(str(result) + '\n')
#    fptr.close()
