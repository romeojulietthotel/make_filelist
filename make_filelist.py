#!/usr/bin/python3

import os
import re
import sys
import time

from multiprocessing import Pool, cpu_count, popen_fork
from string import Template
from subprocess import check_output, PIPE, Popen, STDOUT


def unpakit(file):
    unpak = cmd.substitute(filename=file)
    upout = Popen(unpak, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    upstdout,upstderr=upout.communicate(input=None)
    if upstderr:
        # maybe log this output
        pass
    return (file,upstdout)


if __name__ == '__main__':
    files = os.listdir()
    pools = cpu_count()

    """ Test the commands as they will fail silently. """
    fileexts = {
                'tar.gz':Template('gunzip -c ${filename} | tar tf -'),
                'tar.xz':Template('xz -d -T0 -c ${filename} | tar tf -'),
                'tar.bz2':Template('bunzip2 -c ${filename} | tar tf -'),
                'tar':Template('tar tf ${filename}'),
                'zip':Template('unzip -l ${filename}')
               }

    contents = list()

    for ext in list(fileexts.keys()):
        rx = "{}{}{}".format('^\S+\.', ext, '$')
        frx = re.compile(rx)
        cmd = fileexts[ext]
        fileList = [ x for x in files if frx.match(x) ]
        if len(fileList) < 1:
            print("\n\nStart in a directory containing your tar files.\n\n")
            sys.exit(1)

        pool = None
        pool = Pool(processes=pools)
        result = pool.map(unpakit, fileList)

        # uncomment this to debug, comment pool above & below
        #for file in fileList:
        #   unpakit(file)

        if result[0] is False:
            print("Problem encountered, check external commands")
        contents.append(result)
        # close the pool and wait for the work to finish 
        pool.close()
        pool.join()

    for content in contents:
        for entry in content:
            for toc in entry[1:]:
                lines=(toc.decode().split("\n"))[:-1]
                for line in lines:
                    print("%s -> %s"%(entry[0],line))

