import random
feetmile=5280
meterkilo=1000
def getfileext(filename):
    return filename[filename.index(".")+1:]
def rolldice(side):
    return random.randint(1,side)