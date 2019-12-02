ZSH
===

Z shell (zsh) is an alternative to bash. It is used as an interactive
shell or command interpreter. Zsh has been chosen by apple as a
replacement for bash. A large number of plugins for zsh is avalable at
the Web site [Oh My Zsh](https://ohmyz.sh/).

Features of zsh include:

* commandline completion
* global history that can be shared in shells
* build in file globing
* multiline commands
* spell correction
* compatibillity modes to impersonate other shells
* themes for prompts
* in addition to which a wher ecommand
* shortcut to names directories with ~

In principal it does not matter much whcih shell you use as long as you
use to set up your envireonment properly. While bash zupporst
`.bash_profile` and .bashrc, zsh supports `~/.zprofile` and `~/.zshrc`

A good overview of the loading process is documented at

* <https://medium.com/@rajsek/zsh-bash-startup-files-loading-order-bashrc-zshrc-etc-e30045652f2e>

Setting up zsh on an older OSX is relatively simple.

```bash
$ brew install zsh
```

To add Oh My Zsh you can do:

```bash
$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

To chnge the default shell to zsh you can than execute

```bash
$ chsh -s $(which zsh)
```

To activate the shell you can as usal do 

```bash
$ source ~/.zshrc
```

However if you start a new terminal, you do not have to do this as it is
added automatically.

To use a number of useful plugins, you can activate them with 

```bash
$ plugins=(osx git colored-man colorize pip python brew zsh-syntax-highlighting zsh-autosuggestions)
```

If you like to change the theme you can find a large number at

* <https://github.com/ohmyzsh/ohmyzsh/wiki/Themes>

## Other operating systems

For other operationg systems see

* <https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH>

## zsh on Windows 10

To install zsh on Windows 10, please look at

* <https://www.howtogeek.com/258518/how-to-use-zsh-or-another-shell-in-windows-10/>

