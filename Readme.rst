Run multiple os commands in parallel
====================================

How to use:

.. code-block:: perl

        cd /home/myhome/Downloads
        python3 ./make_filelist.py >filelist.txt


Features:
---------

* Uses all available cpus to decompress and untar files for faster
  completion of the chore.

* Looks at tar.gz tar.xz tar.bz2 .tar .zip

Portability:
------------

* Runs fine on linux, should run fine on macosx.


TODO:
-----

- Possibly there are ways to improve the speed of the decompression tools
  but I haven't looked yet.

- Add other extensions for other naming schemes and other compression algorithms. i.e. .tgz and lz

- I thought I observed some odd behavior where not all cpus were utilized.
  I might have been wrong but a thorough test would be a good addition.
  But it may only point to a python problem so maybe someone else will
  discover this issue.
