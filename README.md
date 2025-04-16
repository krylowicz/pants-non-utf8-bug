Running:
```shell
pants package ::
```
works as intended.

Running:
```shell
pants --changed-since=18402b2aa42259cf7fa75c63505e7bce93249d10 package
```
Throws the following error:
```
12:07:12.46 [ERROR] 'utf-8' codec can't decode byte 0x90 in position 353: invalid start byte
```

Traceback:
```
pants --print-stacktrace -ldebug --changed-since=18402b2aa42259cf7fa75c63505e7bce93249d10 package
```
