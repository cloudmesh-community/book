# Editors Supporting Go :o:


# go editors
While an IDE may provide all the functionality you want for developing code, IDEs can often feel “heavy.” In other words, they can take a long time to start up, use a lot of memory, and sometimes feel unresponsive as you type code because they’re doing too much in the background. Code editors can sometimes be preferable, especially for short sessions, as long as you’re not bothered by having to switch to a separate command-line shell window for compiling.

Plugins can sometimes add IDE-like features to code editors. That’s usually good, as long as the periodic overhead of keeping the plugins up-to-date and the constant overhead of the plugins running processes in the background don’t slow down your editing.

Atom, Brackets, and Visual Studio Code are the three editors that stood out for me for working in the Go language. All are free and open source. Nevertheless, BBEdit, Emacs, Notepad++, Sublime Text, TextMate, and Vim all integrate with Go language plugins, and all have their proponents. Emacs, Notepad++, and Vim are free and open source. BBEdit is commercial, but its little brother TextWrangler is free.
The Atom editor from GitHub ships with the language-go package, which supports Go grammar and snippets. Additional packages for Go bring more functionality. For example, go-plus integrates with many standard Go tools (for autocompletion, formatting, linting, testing) to provide an IDE-like environment, and go-debug integrates with the delve debugger.

The Brackets editor from Adobe has several community extensions for Go support. These include Go-IDE, which uses gocode for autocompletion; Go-Syntax, which uses CodeMirror for syntax highlighting; and Improved Go Formatter, which uses gofmt to format code and goimports to manage imports.

Visual Studio Code supports Go syntax highlighting out of the box. Additional features are provided by the vscode-go plugin, which integrates with more than a dozen standard Go tools. If you don’t have your GOPATH set, the plugin will ask you to set it as soon as you try to edit a Go language file; you can set it for the project and/or the system environment. If you don’t have the Go tools installed, the plugin will ask to install them in the standard places as determined by your GOPATH.
