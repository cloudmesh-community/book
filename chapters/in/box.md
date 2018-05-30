Box
===


what is box

Link:

-   <http://opensource.box.com/box-python-sdk/tutorials/intro.html>

-   <https://github.com/box/box-python-sdk/tree/1.5/demo>

Install:

    pip install boxsdk

app.cfg:

    * A Box client ID for a Box application
    * The corresponding Box client secret
    * A valid developer token for that application

code:

    # Import two classes from the boxsdk module - Client and OAuth2
    from boxsdk import Client, OAuth2

    # Define client ID, client secret, and developer token.
    CLIENT_ID = None
    CLIENT_SECRET = None
    ACCESS_TOKEN = None

    # Read app info from text file
    with open('app.cfg', 'r') as app_cfg:
      CLIENT_ID = app_cfg.readline()
      CLIENT_SECRET = app_cfg.readline()
      ACCESS_TOKEN = app_cfg.readline()

    # Create OAuth2 object. It's already authenticated, thanks to the developer token.
    oauth2 = OAuth2(CLIENT_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN)

    # Create the authenticated client
    client = Client(oauth2, LoggingNetwork())

    # Get information about the logged in user (that's whoever owns the developer token)
    my = client.user(user_id='me').get()
    print (my.name)
    print (my.login)
    print (my.avatar_url)

    root_folder = client.folder('0')
    root_folder_with_info = root_folder.get()

    print (root_folder_with_info)

Questions

-   how to list all file sin dir

-   how to recursively iterate

-   how to download each file when we iterate

boxpython
---------

* <https://github.com/wesleyfr/boxpython>

```python
    from boxpython import BoxAuthenticateFlow, BoxSession, BoxError

    flow = BoxAuthenticateFlow('\<client_id\>','\<client_secret\>')
    flow.get_authorization_url()
    '<https://www.box.com/api/oauth2/authorize?response_type=code&client_id>=\<client_id\>&state=authenticated'

    access_token, refresh_token =
    flow.get_access_tokens('\<auth_code\>')

    def tokens_changed(refresh_token, access_token): ...
        save_to_file(refresh_token, access_token) ... \>\>\> box =
        BoxSession('\<client_id\>', '\<client_secret\>', refresh_token,
        access_token, tokens_changed)

   box.get_folder_info(0)

   box.download_file(11006194629, '/tmp/test_dl.txt')
```

Pybox
-----

<https://github.com/hzheng/pybox>
