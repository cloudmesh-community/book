# cmd Module

If you consider using this module, you may instead want to use cloudmesh cmd5 instead as it provides some very nice features that are not included in cmd. However to do the basics, cmd will do.

The Python cmd module is useful for any more involved command-line
application. It is used in the [Cloudmesh
Project](http://cloudmesh.github.io/), for example, and students have found it helpful in their projects to develop quickly high quality command line tools with documentation so that others can replicate and use the programs.  The Python
cmd module contains a public class, Cmd, designed to be used as a base class for command processors such as interactive shells and other
command interpreters.

Hello, World with cmd
---------------------

This example shows a very simple command interpreter that simply
responds to the greet command.

In order to demonstrate commands provided by cmd, let's save the
following program in a file called helloworld.py.

    from __future__ import print_function, division
    import cmd


    class HelloWorld(cmd.Cmd):
        '''Simple command processor example.'''

        def do_greet(self, line):
            if line is not None and len(line.strip()) > 0:
                print('Hello, %s!' % line.strip().title())
            else:
                print('Hello!')

        def do_EOF(self, line):
            print('bye, bye')
            return True


    if __name__ == '__main__':
        HelloWorld().cmdloop()

A session with this program might look like this:

    $ python helloworld.py

    (Cmd) help

    Documented commands (type help <topic>):
    ========================================
    help

    Undocumented commands:
    ======================
    EOF  greet

    (Cmd) greet
    Hello!
    (Cmd) greet albert
    Hello, Albert!
    <CTRL-D pressed>
    (Cmd) bye, bye

The Cmd class can be used to customize a subclass that becomes a
user-defined command prompt. After you have executed your program,
commands defined in your class can be used. Take note of the following
in this example:

* The methods of the class of the form do_xxx implement the shell
  commands, with xxx being the name of the command. For example, in
  the `HelloWorld` class, the function do_greet maps to the greet on
  the command line.

* The EOF command is a special command that is executed when you press CTRL-D on your keyboard.

* As soon as any command method returns True the shell application
    exits. Thus, in this example the shell is exited by pressing CTRL-D,
    since the do_EOF method is the only one that returns True.

* The shell application is started by calling the cmdloop method of
    the class.

A More Involved Example
-----------------------

Let's look at a little more involved example. Save the following code in
a file called calculator.py.

    from __future__ import print_function, division
    import cmd


    class Calculator(cmd.Cmd):
     prompt = 'calc >>> '
     intro = 'Simple calculator that can do addition, subtraction, multiplication and division.'

     def do_add(self, line):
         args = line.split()
         total = 0
         for arg in args:
             total += float(arg.strip())
         print(total)

     def do_subtract(self, line):
         args = line.split()
         total = 0
         if len(args) > 0:
             total = float(args[0])
         for arg in args[1:]:
             total -= float(arg.strip())
         print(total)

     def do_EOF(self, line):
         print('bye, bye')
         return True


    if __name__ == '__main__':
     Calculator().cmdloop()

A session with this program might look like this:

    $ python calculator.py
    Simple calculator that can do addition, subtraction, multiplication and division.
    calc >>> help

    Documented commands (type help <topic>):
    ========================================
    help

    Undocumented commands:
    ======================
    EOF  add  subtract

    calc >>> add
    0
    calc >>> add 4 5 6
    15.0
    calc >>> subtract
    0
    calc >>> subtract 10 2
    8.0
    calc >>> subtract 10 2 20
    -12.0
    calc >>> bye, bye

In this case we are using the prompt and intro class variables to
    define what the default prompt looks like and a welcome message when
    the command interpreter is invoked.

In the `add` and `subtract` commands we are using the strip and split
    methods to parse all arguments. If you want to get fancy, you can
    use Python modules like getopts or argparse for this, but this is
    not necessary in this simple example.

Help Messages
-------------

Notice that all commands presently show up as undocumented. To remedy
this, we can define help_ methods for each command:

    from __future__ import print_function, division
    import cmd


    class Calculator(cmd.Cmd):
      prompt = 'calc >>> '
      intro = 'Simple calculator that can do addition, subtraction, multiplication and division.'

      def do_add(self, line):
          args = line.split()
          total = 0
          for arg in args:
              total += float(arg.strip())
          print(total)

      def help_add(self):
          print('\n'.join([
              'add [number,]',
              'Add the arguments together and display the total.'
          ]))

      def do_subtract(self, line):
          args = line.split()
          total = 0
          if len(args) > 0:
              total = float(args[0])
          for arg in args[1:]:
              total -= float(arg.strip())
          print(total)

      def help_subtract(self):
          print('\n'.join([
              'subtract [number,]',
              'Subtract all following arguments from the first argument.'
          ]))

      def do_EOF(self, line):
          print('bye, bye')
          return True


    if __name__ == '__main__':
      Calculator().cmdloop()

Now, we can obtain help for the add and subtract commands:

    $ python calculator.py
    Simple calculator that can do addition, subtraction, multiplication and division.
    calc >>> help

    Documented commands (type help <topic>):
    ========================================
    add  help  subtract

    Undocumented commands:
    ======================
    EOF

    calc >>> help add
    add [number,]
    Add the arguments together and display the total.
    calc >>> help subtract
    subtract [number,]
    Subtract all following arguments from the first argument.
    calc >>> bye, bye

## Useful Links

* [cms Python 2 Docs](https://docs.python.org/2/library/cmd.html)
* [cmd Python 3 Docs](https://docs.python.org/3/library/cmd.html)

* [Python Module of the Week: cmd -- Create line-oriented command
    processors](https://pymotw.com/2/cmd/)
    
* [Python Module of the Week: cmd -- Create line-oriented command processors](https://pymotw.com/3/cmd/)

