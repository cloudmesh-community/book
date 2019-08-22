# Perl One liners

Perl is a programming language that used to be very popular with system
administrators. It predates Python. It has some very powerful regular
expression abilities allowing you to easily do things on the commandline
that woul otherwise thake many hours. Here ar some useful perl one line
commands

Strip trailing whitespace from a file:

```perl
perl -lpe 's/\s*$//' FILENAME
```

Replace wrong quote

```perl
perl -i -p -e "s/’/'/g;"  *.md
```

Remove `^M` from file

```
perl -p -i -e 's/\r\n$/\n/g'
```
