# Introduction to Go {#s-go-intro}

![Go Logo](https://upload.wikimedia.org/wikipedia/commons/2/23/Go_Logo_Aqua.svg)

Portions of this lesson have been adapted from the [official Go 
Documentation](https://golang.org/doc/).

Go is expressive, concise, clean, and efficient. It's concurrency
mechanisms make it easy to write programs that get the most out of
multicore and networked machines, while its novel type system enables
flexible and modular program construction. Go compiles quickly to
machine code yet has the convenience of garbage collection and the
power of run-time reflection. It's a fast, statically typed, compiled
language that feels like a dynamically typed, interpreted language.

Here is a good blog article discussing [Why should you learn Go?](https://medium.com/exploring-code/why-should-you-learn-go-f607681fad65).

Regarding the design philosophy behind the Go language, the following is [an excerpt from the designers](https://golang.org/doc/faq#principles):
> When Go was designed, Java and C++ were the most commonly used
> languages for writing servers, at least at Google. We felt that
> these languages required too much bookkeeping and repetition. Some
> programmers reacted by moving towards more dynamic, fluid languages
> like Python, at the cost of efficiency and type safety. We felt it
> should be possible to have the efficiency, the safety, and the
> fluidity in a single language.

> Go attempts to reduce the amount of typing in both senses of the
> word. Throughout its design, we have tried to reduce clutter and
> complexity. There are no forward declarations and no header files;
> everything is declared exactly once. Initialization is expressive,
> automatic, and easy to use. Syntax is clean and light on keywords.
> Stuttering (foo.Foo* myFoo = new(foo.Foo)) is reduced by simple type
> derivation using the := declare-and-initialize construct. And
> perhaps most radically, there is no type hierarchy: types just are,
> they don't have to announce their relationships. These
> simplifications allow Go to be expressive yet comprehensible without
> sacrificing, well, sophistication.

> Another important principle is to keep the concepts orthogonal.
> Methods can be implemented for any type; structures represent data
> while interfaces represent abstraction; and so on. Orthogonality
> makes it easier to understand what happens when things combine.

Go has lots of good features, the following are some examples.

- compiling language
- static typing
- powerful but simplistic concurrency support
- object oriented
- powerful standard libraries


Also, Go lang is gaining popularity among the industry and research
communities. Here you can find its increasing usage by
[companies globally distributed](https://github.com/golang/go/wiki/GoUsers).

The material collected here introduces the reader to the basic
concepts and features of the Go language and system. After you have
worked through the material you will be able to:

-   use Go
-   understand the basic syntax of go
-   write and run go programs stored in a file
-   have an overview of the standard library
-   install Go packages

This tutorial does not attempt to be comprehensive and cover every
single feature, or even every commonly used feature. Instead, it
introduces many of Go's most noteworthy features, and will give you a
good idea of the language's flavor and style. After reading it, you
will be able to read and write Go packages and programs, and you will
be ready to learn more about the various Go library modules.

In order to conduct this lesson you need

-   A computer with Go 1.10 or above
-   Familiarity with command line usage
-   A text editor such as [Atom](https://atom.io/packages/go-plus), [GoLand](https://www.jetbrains.com/go), 
   [vim](https://github.com/fatih/vim-go) or others. You should identity which works best for you
    and set it up.

References
----------

  * [golang.org](http://golang.org/doc/#learning)
  * [Go cheat sheet](https://github.com/a8m/go-lang-cheat-sheet)
  * [The Little Go Book](http://openmymind.net/The-Little-Go-Book/)
  * [Learn Go in an Hour - Video](https://www.youtube.com/watch?v=CF9S4QZuV30) _2015-02-15_
  * [Learning to Program in Go](https://www.youtube.com/playlist?list=PLei96ZX_m9sVSEXWwZi8uwd2vqCpEm4m6), a multi-part video training class.
  * [Go By Example](http://gobyexample.com/) provides a series of annotated code snippets.
  * [Learn Go in Y minutes](http://learnxinyminutes.com/docs/go/) is a top-to-bottom walk-through of the language.
  * [Workshop-Go](https://github.com/sendwithus/workshop-go) - Startup Slam Go Workshop - examples and slides.
  * [Go Fragments](http://www.gofragments.net/) - A collection of annotated Go code examples.
  * [50 Shades of Go: Traps, Gotchas, Common Mistakes for New Golang Devs](http://devs.cloudimmunity.com/gotchas-and-common-mistakes-in-go-golang/index.html)
  * [Free Go Language Workshop](https://www.frameworktraining.co.uk/go-language-free-training-workshop/) Framework Training is running regular free BYOD workshops in London, UK
  * [Golang Tutorials](http://golangtutorials.blogspot.com/2011/05/table-of-contents.html) - A free online class.
  * [The Go Bridge Foundry](https://github.com/gobridge) - A member of the [Bridge Foundry](http://bridgefoundry.org/) family, offering a complete set of free Go training materials with the goal of bringing Go to under-served communities.
* [Golangbot](https://golangbot.com/learn-golang-series/) - Tutorials to get started with programming in Go.
* [Algorithms to Go](http://yourbasic.org/) - Texts about algorithms and Go, with plenty of code examples.
* [Go Language Tutorials](https://www.cybrhome.com/topic/go-language-tutorials) - List of popular sites, blogs and tutorials for learning Go language.
* [Golang Development Video Course](https://www.youtube.com/playlist?list=PLzUGFf4GhXBL4GHXVcMMvzgtO8-WEJIoY) - A growing list of videos focused purely on Go development.

