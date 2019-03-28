# Scala for Cloud Computing

Scala is a multi-paradigm programming language aiming to integrate the features
of object oriented paradigm with that of functional programing. Scala is a statically typed 
language. Scala and Java are interoprable in the sense that libraries written
in either language can be used in Scala or Java.


## Language

### Install Scala

On macOS you can use Homebrew as follows:

```bash
brew update
brew install scala
```

For instructions on how to install Scala on other platforms please
vist the Scala website at https://www.scala-lang.org/download/.

### Hello World! in Scala

Open a terminal and run Scala:

```bash
scala
``` 

If Scala is installed on your machine you should get the following message:

```bash
Welcome to Scala 2.12.8 (Java HotSpot(TM) 64-Bit Server VM, Java 11.0.2).
Type in expressions for evaluation. Or try :help.

scala>

```
 
Now you can write and execute codes, for example:

```bash
println("hello world from scala!")
``` 

Now copy the line above into a teext file and name it helloworld.scala. Form the terminal 
run the following command:

```bash
scala helloworld.scala
```

The result of running this command is the same as executing the code in repl.

### Basics



To apply a method on a expression, Scala uses dot notation:

```python
"hello!".size
```

The code above applies the method `size` on the expression "hello!" and
returns the following (the output is an instance of Int named 'res0' with a value of 6):

```python
res0: Int = 6
```

As another example, consider the method `until` in the class `Int`:

```python
def until(end: Int): collection.immutable.Range
``` 

This method returns a range from the object that calles the method up to but not included 
the value of the `end` parameter. Here is how we can apply this method to a number, let's say 7:

```python
7.until(15)
```

Scala allows the infix syntax and hence you can also use the following syntax to achieve the same outcome:

```python
7 until 15
```

operators are methods which are usually used with the infix syntax:
the follwoing to codes are equivalent:

```python
4 + 5
```


```python
4.+(5)
```

Mehods are defined using the keyword `def`:

```python
def trapezoidArea (base1 : Double, base2 : Double, height : Double): Double = 
(base1 + base2)/ 2 * height

```

The defintion above defines a function with three input parametes of type Double and it returns a double value.

We could use a block to define the body of the method above:

```python
def trapezoidArea (base1 : Double, base2 : Double, height : Double) : Double = 
{(base1 + base2)/ 2 * height}

```

A block is defined by braces `{...}`. The last statement of a block determines its value. Anything you define inside 
a block is accessible only inside the block.

For more on the basic features of Scala language refer to the following resources:
* [Scala Interactive Excercices](https://www.scala-exercises.org/scala_tutorial/terms_and_types)
* [Tour of Scala](https://docs.scala-lang.org/tour/tour-of-scala.html)


### Classes

Let us define a class callled person:



```python
class Person(var firstName : String, var lastName : String){

override def toString : String = s"$firstName $lastName"

}

val fred = new Person("Fred", "Fredian")
println(fred)
```

Save the above script in a file named LearnTheLanguage.scala and run
the code as the following:

 ```python
scala LearnTheLanguage.scala 
```

The class Person has two fields and one method. The primary construcor is 
in the class signature. A class has one primary constructor (this is the constructor that 
you define in the signature of the class) and any (including none) number of auxiliary constructors.
An auxiliary constructor is defined using the keyword `this`. All auxiliary constructors must start 
with a call to a preceding auxiliary constructor or the primary constructor.

In the class `Person` above, we override the method toString. The method toString is
a method in the class AnyRef. The class AnyRef is the supertype of any refrence type. AnyRef is the 
equivalent of java.lang.Object.

@fig:scala-type-hierarchy (taken from [@scala-type-hierarchy]) shows a subset of 
Scala type hierarchy:

![A subset of the type hierarchy](images/unified-types-diagram.svg){#fig:scala-type-hierarchy}



The top class `Any` has methods like `hashCode`, `isInstanceOf`, `asInstanceOf` , `toString` and the methods for 
equality (more on the class is availabe at https://www.scala-lang.org/api/2.12.1/scala/Any.html ). The class `AnyVal` does not add any methods. All value types
are derived from `AnyVal`. The class `AnyRef` adds some more methods: `wait`, `notify` and `synchronized` and `eq`. The method `eq` checks whether two refrences refer to the 
same object. If you want to compare two objects of a class by their values, you should override the `equals`. For example for the class `Person` defined 
above we should override `equals` as follows:

```python
final override def equals(other: Any) = {
val otherPerson = other.asInstanceOf[Person]
if (otherPerson == null) false
else firstName == otherPerson.firstName && lastName == otherPerson.lastName
}
```

Note that the method `equals` returns a boolean. In Scala, the type of the last statement in the body a method, is the 
return type of the method. Here we could make it implicit by declaring the return type as follows:

```python
final override def equals(other: Any) : Boolean = {
val otherPerson = other.asInstanceOf[Person]
if (otherPerson == null) false
else firstName == otherPerson.firstName && lastName == otherPerson.lastName
}
```

But Scala has type inference capability and can infer the types whereever there are enough information for it to infer types.

In addition to a top class `Any`, Scala has also a bottom class `Nothing`.
The class `Nothing` is a subtype of any other type. Scala also a `Null` type. The class `Null` 
has one and only instance called `null`. The class `Null` is a subtype of all reference types and 
therefore `null` is assignable to any reference type but not to value types. 

Members of a class are `public` by default. You can use the access modifier `private` to limit access 
to the members. A `private` member can be accessed only within the class. In the example above, the members
`firstName` and `lastName` are public because they have been defined using `var`. In the primary constructor, any parameter that 
is defined using either `var` or `val` is public. Otherwise it is `private`. `var` indicates that the 
thing to be difined is mutable while `val` indicates that the thing to be defined is immutable.  

In Java we have the concept of `intefaces` where an `interface` contains only the signature of some methods.
`Traits` in Scala are similar to interfaces in Java. However unlike intefaces in Java, a trait can contain attributes and code. Like Java, in Scala a class can have only one supertype. In case you want to define a class with more than
one supertype, you can use `trait`s.
Traits can not be instantiated but classes and objects (an `object` in Scala, which is defined by the kwyword `object` is just a singleton class) can extend traits.

Subtypying in Scala is simialr to that of Java. Let's modify our code and add the entity `Employee` as a subclass of `Person`:

```python
class Person(val firstName : String, val lastName : String){
override def toString : String = s"$firstName $lastName"
}

class Employee(firstName:String, lastName:String, val employeeId : String) extends Person(firstName, lastName){
var salary = 0.0
}

val fred = new Employee("Fred", "Fredian", "410")
println(fred)
```

Note that int the code above the primary constructor of `Employee` is calling the primary constructor of its supertype.
In Scala, only the primary constructor can call a superclass constructor.

Like Java, you can use the keyword `abstract` to define a class that cannot be instantiated.
In an abstract class, you can have methods or members that are not defined (that is, you can define a method without defining its body).

#### Pattern matching



 Pattern matching means that for a given data we have a sequence of patterns against which we 
 we match the data.  Java `switch` statements are examples of pattern matching. 
 
 Assume you have two different jobs: selling apples and software programming:
 
 ```python
sealed trait Profession
case class SellingApples (buy : Double, sell : Double, logistics : Double) extends Profession
case class Programming (hours : Double, perHourRate : Double, cost : Double) extends Profession
```

In this example we used the keyworkd `sealed`. This keyword can be used with a class or a trait. A 
`sealed class` cannot be inherited directly except when the inheriting class (or trait) is defined in the 
same source file. Similarly a `sealed trait` cannot be extended except in the same source file that 
contains the definition of the trait. One of the usages of `sealed traits` is when we want to have an alternative to 
Java's `enums`. 
 
The differences between `class` and `case class` are the followings:

* In order to instantiate an object of a class we need to use the keyword `new` whereas this is not needed for `case class`es.
* Two instances, `a` and `b`  of a `class` are not equal, that is a == b will return false. Whereas two instances `a` and 
`b` of a `case class` when they have the same values for their members are equal, that is `a == b` will return true.


Now we can use the pattern matching feature of Scala as the following:

```python
def calculateProfit(profession : Profession) : Double = 
    profession match {
        case SellingApples (buy, sell, logistics) => sell - (buy + logistics)
        case Programming (hours, perHourRate, cost) => (hours * perHourRate) - cost
    }
```

The match keyword, first checks whether the profession is SellingApples and if it is so, it
extracts the parameters and then evaluates the expression of the right hand side of the arrow, `=>`.
If the match is not successful it proceeds to the next case, if any.

The example above is an instance of an `algebraic data type`. An algebraic data type is a sealed trait together with several 
case classes that extend the sealed trait.  Whenever you have an `is-a` relationship between the concepts in the domain, it may be a good idea 
to model the domain using an algebraic data type.
 

### Scala as a functional language

Functions in Scala are first-class values and therfore you can pass them to other methods or a 
method can return another method as its return value. A function that one of its input or output 
parameters is itself a function, is called a `higher order function`.

Consider the following example:

```python
def cost(area : (Double , Double , Double) => Double, 
x : Double, y : Double, z : Double, costPerUnit : Double) : Double = 
area(x, y, z) * costPerUnit
```

Now we can call this method as the following:

```python
cost(trapezoidArea, 2, 3, 4, 10)
```  

Similarly we could pass an `anonymous function` to  `cost`:

```python
cost((x, y, z) => (x + y)/2 * z, 2, 3, 4, 10)
``` 

### Scala as a tool to create  Domain Specific Languages(DSL)

Scala was designed so that it would support creating DSLs ([refer to here for more](https://www.scala-lang.org/old/node/1403))
. Among the features and capabilities that are in particular helpful for creating DSLs are the followings[@artho2015domain]:

> ...  implicit function definitions, which allow
values of one type to be lifted to values of a different type, the ability to call
methods on objects without dots and parentheses, case classes, partial functions,
call-by-name, user-defined operators composed of symbols, operator overloading,
as well as other features such as higher-order functions and lambda expressions.


#### Cloud computing with Scala and GridGain

[GridGain](https://www.gridgain.com/) a company that provides Grid and Cloud computing
platforms and services, is using a DSL written in Scala that uses
GridGain's cloud computing development systems  to create cloud computing 
platforms. Here is a presentation which includes simple parctical 
programs using the DSL in Scala:

[Cloud Computing with Scala and GridGain](https://vimeo.com/28761608) 



## Parallel programming in Scala

### Parallel collections

Let us start with a simple example on how to run a simple operation in parallel. In this example we want to transform 
a list of strings to all-lowercase. Here is the sequential version of the code:

```python
scala> val x = List("Scala", "SPARK", "PAR", "ParelleL")
scala> x.map(_.toLowerCase)
```

The method map, applies the function that it receives as its argument to each member of the list.

Scala has a parallel counterpart to a number of its important sequential collections. For example `ParArray`,
`mutable.ParHashMap` and `immutable.ParHashMap`. Scala has a speical method `par` that when you call this method on a 
sequential collection, it will copy all the elements in that collection to an equivalent parallel collection. So to run the above example in parallel we only need to 
apply the function `par` as the following:

```python
scala> val x = List("Scala", "SPARK", "PAR", "ParelleL").par
scala> x.map(_.toLowerCase)
```

### Actor model

To do concurrent and parallel programming in Java, we usually use threads. Creating threads and 
managing their intercommunication is complex as you need to handle how they use shared resources, and how they 
communicate to each other. Especially you often need to use locks and monitors to prevent deadlocks. Another paradigm in 
concurrent programming is the `actor model`. In this model we have actors instead of threads. An actor is simply an object that can send and receive messages to other 
actors. Therefore it is an event-based mechanism. 

Scala had an [Actors](https://docs.scala-lang.org/overviews/core/actors.html) library but starting from 
Scala 2.11.0 that library is deprecated in favor of [Akka](https://akka.io). Akka is a toolkit written in Scala for devloping concurrent event-driven 
applications. 

Let us develope a simple concurrent program using Akka. We develope this program using [sbt](https://www.scala-sbt.org/index.html) build tool. We also use IntelliJ Community Edition as our IDE.
To install IntelliJ Community Edition and its Scala plugin please follow [this tutorial](https://docs.scala-lang.org/getting-started-intellij-track/getting-started-with-scala-in-intellij.html). When you have the IDE and the Scala plugin installed then 
follow the istructions in [the second turotial](https://docs.scala-lang.org/getting-started-intellij-track/building-a-scala-project-with-intellij-and-sbt.html) to build a sample project (call it scala_example) using the IDE and sbt build tool.

Now in your scala_example project replace the content of the file `build.sbt` with the following:

```python
name := "scala_example"

version := "0.1"

scalaVersion := "2.12.8"

libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-actor" % "2.5.21",
  "com.typesafe.akka" %% "akka-testkit" % "2.5.21" % Test
)
``` 

This file tells the sbt build tool that it needs to download the Akka related libraries for this project.

Next replace the content of the file `Main.scala` with the follwoing:

```python

package scala_example

import akka.actor.{Actor, ActorRef, ActorSystem, Props}

object Person {
  def props(name: String): Props = Props(new Person(name))

  case class MoneySent(amount: Double)

  case class MoneyRequested(amount: Double)

}

class Person(name: String) extends Actor {

  import Person._

  def receive = {

    case MoneySent(amount) => {
      println(name + " sent $" + amount)

    }
    case MoneyRequested(amount) => {
      println(name + " requested $" + amount)

    }
  }
}

object Main extends App {

  import Person._

  val system: ActorSystem = ActorSystem("helloAkka")
  val fred: ActorRef = system.actorOf(Person.props("fred"))
  val andi = system.actorOf(Person.props("andi"))
  fred ! new MoneyRequested(100)
  andi ! new MoneySent(100)

}
```

Now run the program using the run command of sbt. The output of the program will be 
either of the followings:

this:

```python
[info] Running scala_example.Main 
andi sent $100.0
fred requested $100.0
```

or this:

```python
[info] Running scala_example.Main 
fred requested $100.0
andi sent $100.0
```

In the example we defined a class named `Person` which extends the tarit `Actor`. 
This class overrides the `receive` method of the `Actor` trait to handle the messages that it receives. What happens when an actor receives a message, is the following:
* The actor maintains a queue for the messages that it receives. So when the actor receives a message, it adds the message to its queue.
* The actor executes the message that is in front of its queue.

Note that the internal state of an actor can be changed only through messages. Now an actor processes messages one at a time, so there will be no races regarding the internal stataes of the actors and therefore 
there is no need to have locks or monitors. Also senders are not locked and as soon as they sent a message they can continue doing other things. 



 
 
