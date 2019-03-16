# aiohttpServerForSphinx
a tiny web server for sphinx html builds

please copy this file to your sphinx html BUILDDIR and start using python3 ...

e.g. identify the sphinx BUILDDIR:

```shell
$ cat Makefile   # in your sphinx main dir 
...
SOURCEDIR     = sphinxSource
BUILDDIR      = sphinxBuild
```

```shell
$  python3 sphinxBuild/html/aiohttpServerForSphinx.py -p 8081
{'port': 8081}
======== Running on http://0.0.0.0:8081 ========
```
