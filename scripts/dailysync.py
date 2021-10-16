#!/usr/bin/env python
import subprocess
import os
import re
from multiprocessing import Pool

src = "/home/eric/gcert/multiprocessing/data/prod/"
dest = "/home/eric/gcert/multiprocessing/data/prod_backup/"

def runUpdate(srcDir):
        SPath = os.path.join(src, srcDir)
        DPath = os.path.join(dest, srcDir)

        if os.path.exists(DPath):
                print("updating: " + DPath)
                subprocess.call(["rsync", "-arq", SPath, DPath])
        else:
                print("copying: " + SPath + " to " + DPath)
                subprocess.call(["cp", "-r", SPath, DPath])


def generateSrcDir(source):
        print("Generating dirs in " + source)
        srcDir = []
        cat = os.walk(source, topdown=True)
        for root, dirs, files in cat:
                for name in dirs:
                        rootAfter = re.match(r".*(prod/)(.*)", root).groups()[1]
                        dir = os.path.join(rootAfter, name)
                        print(dir)
                        srcDir += [dir]
        return(srcDir)

if __name__ == "__main__":
        backupDirs = generateSrcDir(src)
        print(backupDirs)
        p = Pool(len(backupDirs))
        p.map(runUpdate, backupDirs)

