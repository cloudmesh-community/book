# Go Language {#s-go-language}

Go is a computer language developed by Google with the goal
to "build simple,
reliable, and efficient software".
The language is open source and the main Web page is <https://golang.org/>

Go is specifically a systems-level programming language for large, distributed systems and highly-scalable network servers. It is meant to replace C++ and Java in terms of Google’s needs. Go was meant to alleviate some of the slowness and clumsiness of development of very large software systems.

* slow compilation and slow execution
* programmers that collaborate using different subsets of languages
* readability and documentation
* language consistency
* versioning issues
* multi-language builds
* dependencies being hard to maintain


The following program from the <https://golang.org/> web page shows
the customary Hello World example:

```go
package main

import "fmt"

func main() {
   /* This is a very easy program. */
	fmt.Println("Hello World!")
}
```

## Concurrency in Go

### GoRoutines (execution)

A GoRoutine in the Go programming language is a lightweight thread that is managed by Go runtime. If you just put ‘go’ before a function, it means that it will execute concurrently with the rest of the code.

### Channels (communication)

Channels are pipes that connect concurrent GoRoutines. You are able to send values and signals over Channels from GoRoutine to GoRoutine. This allows for synchronizing execution.

### Select (coordination)

The Select statement in Go lets you wait and watch multiple operations on a channel. Combining GoRoutines and channels will show off the true power of concurrency in Go.
