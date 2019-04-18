# Docopts in Julia are similar to Python, Ruby, and other languages.

## Installation

Again, most of Julia's packages that are not in the base code are contained within git repositories. [@getting-started]. To get started with DocOpts in Julia,
issue the following command within the Julia REPL:

```julia
Pkg.add("DocOpt")
```

A list of the all approved packages is available at https://github.com/JuliaLang/METADATA.jl

Usage example is given as follows:

https://github.com/docopt/DocOpt.jl

```Julia
doc = """Naval Fate.
https://github.com/JuliaLang/METADATA.jl

Usage:
  naval_fate.jl ship new <name>...
  naval_fate.jl ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.jl ship shoot <x> <y>
  naval_fate.jl mine (set|remove) <x> <y> [--moored|--drifting]
  naval_fate.jl -h | --help
  naval_fate.jl --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""

using DocOpt  # import docopt function

args = docopt(doc, version=v"2.0.0")
```
