Python Click
------------

Click allows developers to create composable command line interfaces. It
aims to simplify the the process of writing command line tools.
Highlights include:

-   arbitrary nesting of commands
-   automatic help page generation
-   supports of lazy loading of subcommands at runtime

The following example take from the clik Web page at

-   <http://click.pocoo.org/>

illustrates the use of click

    import click

    @click.command()
    @click.option('--count', 
                  default=1, 
                  help='Number of greetings.')
    @click.option('--name', 
                  prompt='Your name',
                  help='The person to greet.')
    def hello(count, name):
        """Simple program that greets NAME for a total of COUNT times."""
        for x in range(count):
        click.echo('Hello %s!' % name)

    if __name__ == '__main__':
        hello()

A sample invocation looks like this:

    $ python hello.py --count=3
    Your name: Gregor
    Hello Gregor!
    Hello Gregor!
    Hello Gregor!

To obtain the man page you can say:

    $ python hello.py --help
    Usage: hello.py [OPTIONS]

        Simple program that greets NAME for a total of COUNT times.

        Options:
            --count INTEGER  Number of greetings.
            --name TEXT      The person to greet.
            --help           Show this message and exit.

### Install

    pip install click
    pip install click-shell

### Click Shell

click-shell is an extension allowing to run click commands in a shell

    from click_shell import shell

    @shell(prompt='my-shell > ', intro='Starting the shell ...')
    def my_shell():
        pass

    @my_shell.command()
    def the_command():
        print ('the shell is running')

    ...

### Links

-   <http://click.pocoo.org>
-   <https://github.com/clarkperkins/click-shell>
