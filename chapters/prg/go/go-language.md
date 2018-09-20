# Go Language :o: {#s-go-language}

:warning: This section is under development. It is contributed by Qianqian

Go is a computer language developed by Google with the goal 
to "build simple, 
reliable, and efficient software". 
The language is open source and the main Web page is


https://golang.org/

## Program Structure 

  A Go program basically consists of the following parts −

* Package Declaration
* Import Packages
* Functions
* Variables
* Statements and Expressions
* Comments

### Hello world

Firstly, look at a simple code that would print the words "Hello Tomorrow" 

```go 
package main

import "fmt"

func main() {
   /* This is a very easy program. */
	fmt.Println("Hello World!")
    }
```
    
Let us explain in detail about the meaning of different parts of the
above program.

* The first line of the program package main defines the package name
  in which this program should lie. It is a mandatory statement, as Go
  programs run in packages. The main package is the starting point to
  run the program. Each package has a path and name associated with
  it.
* The next line import "fmt" is a preprocessor command which tells the
  Go compiler to include the files lying in the package fmt.
* The next line func main() is the main function where the program
  execution begins.
* The next line /*...*/ is ignored by the compiler and it is there to
  add comments in the program. Comments are also represented using //
  similar to Java or C++ comments.
* The next line fmt.Println(...) is another function available in Go
  which causes the message "Hello, Tomorrow!" to be displayed on the
  screen. Here fmt package has exported Println method which is used
  to display the message on the screen.
* Notice the capital P of Println method. In Go language, a name is
  exported if it starts with capital letter. Exported means the
  function or variable/constant is accessible to the importer of the
  respective package.

### Executing a Go Program 

Let us discuss how to save the source code in a file, compile it, and
finally execute the program. Please follow the steps given below −

* Open a text editor and add the above-mentioned code.
* Save the file as hello.go
* Open the command prompt.
* Go to the directory where you saved the file.
* Type go run hello.go and press enter to run your code.
* If there are no errors in your code, then you will see "Hello
  Tomorrow!" printed on the screen.

 Make sure the Go compiler is in your path and that you are running it
 in the directory containing the source file hello.go.
 
## Basic Syntax
 
After we konw the program structure of Go, now we can learn more
about the building blocks of go programming language.

### Tokens in Go 
 
 A Go program consists of various tokens. A token is either a keyword,
 an identifier, a constant, a string literal, or a symbol. For
 example, the following Go statement consists of six tokens − ```go
 fmt.Println("Hello, Tomorrow!")  ``` the six individual tokens are as
 follow- ```go fmt .  Println ( "Hello, Tomorrow!"  ) ```
 

### Line separator in GO 

In a Go program, the line separator key is a statement
terminator. compared with C programming language, individual
statements in GO don't need a special separator like “;” . The Go
compiler internally places “;” as the statement terminator to indicate
the end of one logical entity.

For example, let us look at the following statements −

```go
fmt.Println("Hello, Tomorrow!")
fmt.Println("we have a better future!")
fmt.println("I am learning GO programming language!")
```

we can see that there is no special separator among individual
statements in GO.
 
### Identifiers 

A Go identifier is a name used to identify a variable, function, or
any other user-defined item. An identifier starts with a letter _A to
Z_ or _a to z_ or an underscore _ followed by zero or more letters,
underscores, and digits (0 to 9).

identifier = letter { letter | unicode_digit }.

Go does not allow punctuation characters such as **@, $, #, % and &** within identifiers. Go is a case-sensitive programming language. Thus, **Mahesh and mahesh are two different identifiers in Go**. Here are some examples of acceptable identifiers −
```go
mahesh      kumar   abc   move_name   a_123
myname50   _temp    j      a23b9      retVal
``` 

### Comments 

comments are helpful texts but are ingored by compilers, they start with /* and end with */ as follow:

```go
/* A new learner in GO */
```

### keywords

The following list shows the reserved words in Go. These reserved words may not be used as constant or variable or any other identifier names.

break   | default    | func   | interface | select 
case    | defer      | Go     | map       | Struct 
chan    | else       | Goto   | package   | Switch 
const	| fallthrough| range  |Type       | var    
continue| for	     | import | if        | return 
 
 
 
 
## References

* [Go toturial](https://www.tutorialspoint.com/go/)

 
