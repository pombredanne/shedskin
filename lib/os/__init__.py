import path

name = ''

linesep = ''
environ = {'':''}

curdir = ''
pardir = ''
extsep = ''
sep = ''
pathsep = ''
defpath = ''
altsep = ''
devnull = ''

class error(OSError): 
    pass

class __cstat:
    def __init__(self):
        self.st_mode = 1
        self.st_size = 1
        self.st_ino = 1
        self.st_dev = 1
        self.st_rdev = 1
        self.st_nlink = 1
        self.st_mtime = 1
        self.st_atime = 1
        self.st_ctime = 1
        self.st_uid = 1
        self.st_gid = 1

        self.st_blksize = 1
        self.st_blocks = 1

    def __len__(self):
        return 1
    def __getitem__(self, i):
        return 1
    def __slice__(self, x, l, u, s):     
        return (1,)

    def __repr__(self):
        return ''

class popen_pipe(file):
    pass

def listdir(path):
    return ['']

def getenv(name, alternative=''):
    return ''

def getcwd():
    return ''

def chdir(d):
    pass

def rename(a, b):
    pass

def remove(path):
    pass

def rmdir(a):
    pass

def removedirs(name):
    pass

def mkdir(a, mode=0777):
    pass

def makedirs(name, mode=0777):
    pass

def fork():
    return 1

def abort():
    pass

def chown(path, uid, gid):
    pass

def system(c):
    return 1

def strerror(i):
    return ''

def stat(path):
    return __cstat()

def lstat(path):
    return __cstat()

def fstat(file):
    return __cstat()

def readlink(path):
    return ''

def getuid():
    return 1

def getgid():
    return 1

def getgroups():
    return [1]

def getpgid(pid):
    return 1

def getpgrp():
    return 1

def stat_float_times(n=False): 
    return True

def getpid():
    return 1

def putenv(variable, value):
    pass

def umask(newmask):
    return 0

def chmod(path, val):
    return 0

def unsetenv(var):
    pass

def renames(old, new):
    pass

def popen(cmd, mode='r', bufsize=-1):
    return popen_pipe()

def popen2(cmd, mode='r', bufsize=-1):
    return ( file('/bin/sh'), file('/bin/sh') )

def popen3(cmd, mode='r', bufsize=-1):
    return ( file('/bin/sh'), file('/bin/sh'), file('/bin/sh') )

def popen4(cmd, mode='r', bufsize=-1):
    return ( file('/bin/sh'), file('/bin/sh') )

def close(fd):
    pass

def execv(file, args):
    pass

def execvp(file, args):
    pass

def fdopen(fd, mode='r', bufsize=-1):
    return file('/bin/sh')

def pipe():
    return (0,0)

def dup(f1):
    return 1

def dup2(f1,f2):
    pass

def fchdir(f1):
    pass

def fdatasync(f1):
    pass

def chroot(dir):
    pass

def ctermid():
    return ''

