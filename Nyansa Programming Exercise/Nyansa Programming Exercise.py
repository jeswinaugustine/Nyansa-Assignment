import pytz
from datetime import datetime


def dailysummarizedreport(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    output = {}

    for line in lines:
        time, site = line.split('|')
        time = datetime.utcfromtimestamp(int(time)).strftime("%m/%d/%y")
        site = site.rstrip()
        if time in output:
            if site in output[time]:
                output[time][site] += 1
            else:
                output[time][site] = 1
        else:
            output[time] = {site: 1}

    gmt = pytz.timezone('GMT')

    for time in sorted(output):
        print(time, gmt)
        for site in output[time]:
            print(site, output[time][site])


dailysummarizedreport('input.txt')
