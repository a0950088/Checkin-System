def CheckinLog(msg):
    path = 'log.txt'
    with open(path, 'a') as f:
        f.write(msg)