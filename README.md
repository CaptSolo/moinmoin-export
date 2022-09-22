This project performs basic export of [moinmoin](http://moinmo.in/) pages to separate files or to an [org mode](https://orgmode.org) file.

# Usage

Optionally rename moinmoin pages directories to convert their unicode representation to regular utf-8:

```
python rename.py {moinmoin-pages-dir}
```

Extract the latest revisions of each page to a plain text file:

```
python export.py {moinmoin-pages-dir} -o {output-dir}
```

Or extract the latest revisions of each page to an org mode file:

```
python export.py {moinmoin-pages-dir} --org-file {org-output-file}
```

### Note

If `rename.py` fails with a Unicode error make sure you have correctly [set up UTF8 environment](https://perlgeek.de/en/article/set-up-a-clean-utf8-environment).
