# Chameleon Cloud Security Warning {#sec:chameleon-resources}

> ![Warning](images/warning.png) **Chameleon cloud promotes insecure
> use of ssh while suggesting passphrase less keys.** This is **very
> dangerous** and wrong due to the fact that someone could gain access
> to your computer and if a password less key is stolen easy access to
> other systems can be achieved. Instead you must use whenever
> possible passphrases and use ssh agent and ssh add! The same
> bets-practice security rules that you use on your laptop must apply
> on resources that you place in a cloud!

To show you this insecue practice, we quote from their
[Web page](https://www.chameleoncloud.org/about/frequently-asked-questions/#toc-ssh-issues):

> You will receive a message “Enter same passphrase again:” so just
> leave it blank and press enter.

This is clearly **WRONG** :warning:

Hence do not use their advise that is mentioned in their
documentation. Follow ours, and use a passphrase! If uncertain,
discuss with us.

Chameleon cloud also promotes the use of putty on the clients connecting
to windows which was for many years standard on Windows machines.
However, there are now much better ways of using keys from the Windows
command prompt as `ssh`, `ssh-keygen` and `ssh-add` are distributed with
Windows 10 and can now be activited. Please use them instead of putty as
they conform to best practices across all platforms and not just Windows
as putty does. However, you still can use putty on Windows if you like,
there is no security issue with putty as far as we know. Make sure you
use it properly.
