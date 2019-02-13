# Go Language {#sec:go-language}

Go is a computer language developed by Google with the goal to "build
simple, reliable, and efficient software".  The language is open
source and the main Web page is <https://golang.org/>

Go is specifically a systems-level programming language for large,
distributed systems and highly-scalable network servers. It is meant
to replace C++ and Java in terms of Google’s needs. Go was meant to
alleviate some of the slowness and clumsiness of development of very
large software systems.

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

Making a program to be able to run multiple tasks simultaneously is known as concurrency. Go language supports concurrency with `GoRoutines`, `Channels`, and `select` statements.

### GoRoutines (execution)

A GoRoutine in the Go programming language is a lightweight thread
that is managed by Go runtime. If you just put ‘go’ before a function,
it means that it will execute concurrently with the rest of the code.

To create a goroutine we use the keyword go followed by a function invocation:

```go
package main

import "fmt"

func f(n int) {
  for i := 0; i < 10; i++ {
    fmt.Println(n, ":", i)
  }
}

func main() {
  go f(0)
  var input string
  fmt.Scanln(&input)
}
```

This program consists of two `goroutines`. The first `goroutine` is implicit and is the main function itself. The second goroutine is created when we call `go f(0)`. Normally when we invoke a function our program will execute all the statements in a function and then return to the next line following the invocation. With a `goroutine` we return immediately to the next line and don't wait for the function to complete.

Goroutines are lightweight and we can easily create thousands of them. We can modify our program to run 10 goroutines by doing this:

```go
func main() {
  for i := 0; i < 10; i++ {
    go f(i)
  }
  var input string
  fmt.Scanln(&input)
}
```

### Channels (communication)

Channels are pipes that connect concurrent GoRoutines. You are able to
send values and signals over Channels from GoRoutine to
GoRoutine. This allows for synchronizing execution.

Here is an example program using channels:

```go
package main

import (
  "fmt"
  "time"
)

func pinger(c chan string) {
  for i := 0; ; i++ {
    c <- "ping"
  }
}

func printer(c chan string) {
  for {
    msg := <- c
    fmt.Println(msg)
    time.Sleep(time.Second * 1)
  }
}

func main() {
  var c chan string = make(chan string)

  go pinger(c)
  go printer(c)

  var input string
  fmt.Scanln(&input)
}
```

This program will print “ping” forever (hit enter to stop it). A channel type is represented with the keyword `chan` followed by the type of the things that are passed on the channel (in this case we are passing strings). The `<-` (left arrow) operator is used to send and receive messages on the channel. `c <- "ping"` means send "ping". `msg := <- c` means receive a message and store it in msg.


### Select (coordination)

The Select statement in Go lets you wait and watch multiple operations
on a channel. Combining GoRoutines and channels will show off the true
power of concurrency in Go.

Take the following code as an example:

```go
func main() {
  c1 := make(chan string)
  c2 := make(chan string)

  go func() {
    for {
      c1 <- "from 1"
      time.Sleep(time.Second * 2)
    }
  }()

  go func() {
    for {
      c2 <- "from 2"
      time.Sleep(time.Second * 3)
    }
  }()

  go func() {
    for {
      select {
      case msg1 := <- c1:
        fmt.Println(msg1)
      case msg2 := <- c2:
        fmt.Println(msg2)
      }
    }
  }()

  var input string
  fmt.Scanln(&input)
}
```

`select` picks the first channel that is ready and receives from it (or sends to it). If more than one of the channels are ready then it randomly picks which one to receive from. If none of the channels are ready, the statement blocks until one becomes available.
