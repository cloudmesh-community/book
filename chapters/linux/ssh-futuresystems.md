## SSH to FutureSystems Resources

---

![](images/learning.png) **Learning Objectives**

* Obtain a Future system account so you can use kubernetes or
  dockerswarm or other services offered by FutureSystems.

---

Next, you need to upload the key to the portal. You must be logged into
the portal to do so.

Step 1: Log into the portal <https://portal.futuresystems.org/>


Step 2: Click on the "MY ACCOUNT" link.

Step 3: Click on "EDIT"

Step 4: Paste your ssh key into the box marked Public SSH Key. Use a
text editor to open the `id_rsa.pub`. Copy the entire contents of this
file into the ssh key field as part of your profile information. Many
errors are introduced by users in this step as they do not paste and
copy correctly.

If you need to add keys, use the Add another item button

At this point, you have uploaded your key. However, you will still need
to wait till all accounts have been set up to use the key, or if you did
not have an account till it has been created by an administrator.
Please, check your email for further updates. You can also refresh this
page and see if the boxes in your account status information are all
green. Then you can continue.

### Testing your FutureSystems ssh key

If you have had no FutureSystem account before, you need to wait for up
to two business days so we can verify your identity and create the
account. So please wait. Otherwise, testing your new key is almost
instantaneous on india. For other clusters like it can take around 30
minutes to update the ssh keys.

To log into india simply type the usual ssh command such as:

```bash
$ ssh portalname@india.futuresystems.org
```

The first time you ssh into a machine you will see a message like this:

    The authenticity of host 'india.futuresystems.org (192.165.148.5)' cannot be established.
    RSA key fingerprint is 11:96:de:b7:21:eb:64:92:ab:de:e0:79:f3:fb:86:dd.
    Are you sure you want to continue connecting (yes/no)? yes

You have to type yes and press enter. Then you will be logging into
india. Other FutureSystem machines can be reached in the same fashion.
Just replace the name india, with the appropriate FutureSystems resource
name.


