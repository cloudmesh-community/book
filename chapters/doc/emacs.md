Emacs
-----

One of the most useful short manuals for emacs is the following reference
card. It takes some time to use this card efficiently, but the most
important commands are written on it. Generations of students have
literally been just presented with this card and they learned emacs
from it.

-   <https://www.gnu.org/software/emacs/refcards/pdf/refcard.pdf>

There is naturally also additional material available and a great
manual. You could also look at

-   <https://www.gnu.org/software/emacs/tour/>

From the last page we have summarized the most useful and **simple**
features. And present them here. One of the hidden gems of emacs is the
ability to recreate replay able macros which we include here also. You
ought to try it and you will find that for data science and the cleanup
of data emacs (applied to smaller datasets) is a gem.

Notation

  Key   Description
  ----- ----------------------
  C     Control
  M     Esc (meta character)

Here are some other ways on what to do if you have accidentally pressed
a wrong key:

-   `C-g` If you pressed a prefix key (e.g. `C-x`) or you invoked a
    command which is now prompting you for input (e.g. Find file: ...),
    type `C-g`, repeatedly if necessary, to cancel. `C-g` also cancels a
    long-running operation if it appears that Emacs has frozen.

-   `C-/` If you executed a command and Emacs has modified your buffer,
    use `C-/` to undo that change.

  Key         Description
  ----------- -----------------------------------------
  ---         **Saving and Exiting**
  `C-x C-w`   Write the buffer to file
  `C-x C-s`   Write the buffer to file and quit Emacs
  ---         **Cursor** *use the cursor keys or ...*
  `C-f`       Forward one character
  `C-n`       Next line
  `C-b`       Back one character
  `C-p`       Previous line
  ---         **Cursor context move**
  `C-a`       Beginning of line
  `M-f`       Forward one word
  `M-a`       Previous sentence
  `M-v`       Previous screen
  `M-<`       Beginning of buffer
  `C-e`       End of line
  `M-b`       Back one word
  `M-e`       Next sentence
  `C-v`       Next screen
  `M->`       End of buffer
  ---         **Cursor jump**
  `M-g` g     Jump to specified line number
  ---         **Search**
  `C-s`       Incremental search forward
  `C-r`       Incremental search backward
  ---         **Replace**
  `M-`%       Query replace
  ---         **Killing ("cutting") text**
  `C-k`       Kill line
  `C-y`       Yanks last killed text
  ---         **Macros**
  `M-x (`     Start recording macro
  `M-x )`     Stop recording macro
  `M-x e`     Play back macro once
  `M-5 C-x-e` Play back macro 5 times

Modes

"Every buffer has an associated major mode, which alters certain
behaviors, key bindings, and text display in that buffer. The idea is to
customize the appearance and features available based on the contents of
the buffer." modes are typically activated by ending such as `.py`,
`.java`, `.rst`, ...

  Key                    Description
  ---------------------- -------------------------------------------------------------------------
  `M-x python-mode`      Mode for editing Python files
  `M-x auto-fill-mode`   Wraps your lines automatically when they get longer than 70 characters.
  `M-x flyspell-mode`    Highlights misspelled words as you type.

### Org Mode

Emacs has some very advanced features that you can activate via a mode.
One such feature is to organize a TODO list via org-mode.

Instead of us designing our own video, we point to a community tutorial
such as

\video{Cloud}{18:04}{Emacs org-mode}{https://www.youtube.com/watch?v=Kde5YVUwDTQ}{Youtube}
### Programming Python with Emacs

Emacs comes by default with syntax highlighting for python when you
edit a `.py` file. This is really all you need. It also comes with a
python ide that you can use and customize.

Python auto-completion for Emacs:

-   <https://github.com/tkf/emacs-jedi>

Some more information is available at

-   <https://realpython.com/blog/python/emacs-the-best-python-editor/>

-   <https://www.emacswiki.org/emacs/PythonProgrammingInEmacs>

### Emacs Keys in a Terminal

One of the real great features of knowing emacs is that you can set all
your editors to emacs shortcuts. This includes pyCharm, but also bash.
In bash you simply say

    set -o emacs

in your bash prompt. Additionally, if you do not have a window systems
configured, you can run emacs directly in the terminal with

    emacs -nw

This you can log in to a remote computer and if it has emacs installed.
Use it in the terminal. This would replace editors such as vi, vim,
nano, pico or others that work in a terminal.

### LaTeX and Emacs

LaTeX is directly supported by emacs and nothing has to be changed.
However, a collection of information about additional LaTeX features for
emacs is available at

-   <https://www.emacswiki.org/emacs/LaTeX>

Of interest are for example also

* `M-x flyspell-mode`: allowing to do spell checking in the window
* predictive mode: https://www.emacswiki.org/emacs/PredictiveMode
* preview latex
* whizzy tex

However instead of previews and whizzy tex we recommend to use

-   <https://www.emacswiki.org/emacs/LatexMk>

which comes pre-installed and allows you to do editing in one terminal,
while previewing the update on change in another window.

LatexMk is all integrated in our report Makefiles and the Book format,
so you will be able to use this immediately. This is similar to share
latex, but much faster and without collaborators editing the same file.
