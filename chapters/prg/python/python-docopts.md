# DocOpts {#s-python-docopts}

When we want to design commandline arguments for python programs we have
many options. However, as our approach is to create documentation
first, docopts provides also a good apprach for Python. The code for it is
located at

* <https://github.com/docopt/docopt>

It can be installed with

```bash
$ pip install docopt
```

A sample programs are located at 

* <https://github.com/docopt/docopt/blob/master/examples/options_example.py>

A sample program of using doc opts for our purposes loks as follows


```python
"""Cloudmesh VM management 

Usage:
  cm-go vm start NAME [--cloud=CLOUD]
  cm-go vm stop NAME [--cloud=CLOUD]
  cm-go set --cloud=CLOUD
  cm-go -h | --help
  cm-go --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --cloud=CLOUD  The name of the cloud.
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

ARGUMENTS:
  NAME     The name of the VM` 
"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.0rc2')
    print(arguments)
```

Another good feature of using docopts is that we can use the same
verbal description in other programming languages as showcased in this
book.
