#!/usr/bin/python
import json
import sys
from subprocess import call

if len(sys.argv) != 2:
    print 'Usage: ', str(sys.argv[0]), 'YYMMDD'
else:
    date = sys.argv[1]

    print "Downloading for ", date
    status_list = date + ".txt"
    call(["wget", "-O", status_list, "--load-cookie=/share/cookies.txt", "--post-data", "'Kid=0&pdt="+date+"&fmt=Long&_ts_:0'", "https://www.dailyconnect.com/CmdListW?cmd=StatusList"])

    with open(status_list) as data_file:    
        data = json.load(data_file)

    for d in data['list']:
        if 'Photo' in d:
            photo_id = str(d['Photo'])
            date = str(d['Pdt'])
            time = str(d['Utm'])
            if len(time) == 3:
                time = "0"+time
            # yyyy:mm:dd-hh:mm:ss
            timestamp = "20"+date[0:2]+":"+date[2:4]+":"+date[4:6]+"-"+time[0:2]+":"+time[2:4]+":00"

            print ""
            print "===================="
            print "Photo ID: " + photo_id
            print "TIMESTAMP: " + timestamp

            call(["wget", "--load-cookie=cookies.txt", "-O", photo_id+".jpg", "https://www.dailyconnect.com/GetCmd?cmd=PhotoGet&id="+photo_id+"&thumb=0"])
            call(["jhead", "-mkexif", photo_id+".jpg"])
            call("jhead -ts"+timestamp+" "+photo_id+".jpg", shell=True)
            call("jhead -n%Y%m%d_%H%M%S "+photo_id+".jpg", shell=True)
            print "===================="
