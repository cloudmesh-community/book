# Security Warning

:warning: **Chameleon cloud promotes insecure use of ssh while
suggesting passphrase less keys.** This is **very dangerous** due to
the fact that someone could gain access to your computer and if a
password less key is stolen easy access to other systems can be
achieved. Instead you must use whenever possible passphrases and use
ssh agent and ssh add!

To show you tis insecue practice, we quote from their
[Web page](https://chameleoncloud.readthedocs.io/en/latest/getting-started/faq.html?highlight=ssh#faq-ssh):

> You will receive a message “Enter same passphrase again:” so just
> leave it blank and press enter.

Hence do not use their advise that is mentioned multiple times in their
documentation. Follow ours, and use a passphrase!

# Resources

YOu can also visit the Chameleon Web page as there is also more
information about other topics that we may not need to worry about
. Furthermore we do not use Advanced Appliances, but use mostly
ansible instead as it is independent from OpenStack and can be used
with other frameworks.

If you prefer you can also go to the Chameleon Web site using the
following links. However we have improved some of the documentation
found in this document. We would like to get your feedback in case you
find errors or like to contribute tho this documentation.


The links to Chameleons online resources are:

- [Web page](https://www.chameleoncloud.org/)
- [Documentation ](https://chameleoncloud.readthedocs.io/en/latest/)
- [News](https://www.chameleoncloud.org/news/)
- [About](https://www.chameleoncloud.org/about/chameleon/)
- [Log in](https://www.chameleoncloud.org/login/)
- [Dashborad](https://www.chameleoncloud.org/user/dashboard/)

## Outages

Any computer system may undergo maintenance. Before filing tickets with
Chameleon cloud, make sure that the cloud is operational. Outages are
posted at

<https://www.chameleoncloud.org/user/outages/>

To be notified by mail, you can subscribe to them at

<https://www.chameleoncloud.org/user/profile/subscriptions/>

## Account Creation

The fist step to get access Chameleon cloud is to create a user account
if you do not already have one. You can skip to the next section if you
have a chameleon cloud account.

The register web page is available at:

<https://www.chameleoncloud.org/user/register/>

For more details, please als consult the chameleon chapter in the
handbook.

## Join a Project

An active project is required to access compute resources. Each class
has a particular project number that you will need to write down as you
will use it to interact with the system. The information is given out by
the instructor.

For the Fall-18 classes please use the
following project number:

* [CH-819337](https://www.chameleoncloud.org/user/projects/37347/)

However, before you can access it the instructor (in our class Dr. von
Laszewski) needs to authorize you to use the project. For this you have
filled out an account survey in piazza. The most common errors we see
are that students provide us with the wrong user name or have not
applied for a chameleon account. Once the instructor has added you, you
will be able to use VM's on Chameleon cloud.

## Usage Restriction

As using VM's in a shared environment cost resources, you are
**REQUIRED** to shut down your resources after you are not using them
anymore. Furthermore, before the class is over and we assign grades you
must terminate your instances and free all ip addresses. Remember that
any running VM is just like you were running a real computer. I am sure
you close the lid of your laptop when not in use. Shutting down the VM
is similar and avoids that you unnecessarily use resources that others
could use in a shared environment.
