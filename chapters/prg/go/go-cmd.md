# Go CMD {#s-go-cmd}

## CMD

In pthon we have the CMD5 package that allows us to create command
shells with plugins. In Go we find a community developed package called
`gosh` (or Go shell). It uses the Go plugin system to
create  interactive console-based shell programs.
A shell created with `gosh` contains a collection of Go plugins, each
of which which implement one
or more commands. Upon start `gosh` starts, searches the directory
`./plugins` and loads them so they become available within `gosh`.

* <https://github.com/vladimirvivien/gosh>

## DocOpts

When we want to design commandline arguments for go programs we have
many options. However, as our approach is to create documentation
first, docopts provides also a good apprach for Go. The code for it is
located at

* <https://github.com/docopt/docopt.go>

It can be installed with

```bash
$ go get github.com/docopt/docopt-go
```

A sample programs are located at 

* <https://github.com/docopt/docopt.go/blob/master/examples/options/>

A sample program of using doc opts for our purposes loks as follows.

```go
package main

import (
	"fmt"
	"github.com/docopt/docopt-go"
)

func main() {
	  usage := `cm-go.

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

	  arguments, _ := docopt.ParseDoc(usage)
	  fmt.Println(arguments)
}
```
