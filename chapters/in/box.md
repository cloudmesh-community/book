# Box :o: :question:


Box is cloud service that allows users to store, access, collaborate, and share files. Box also has its own platform offering APIs in multiple languages and an SDK for the development of custom applications and integrations. Box offers free and paid versions for individual accounts and multiple types of business accounts that are charged on a per user basis. 

Limitations: 

- While Box offers unlimited storage, it's biggest business account has a 5GB file size limit with a 2GB limit on the smallest business plan and 250MB on the unpaid personal plan. Other services have no individual file size limit. 
- Using Box Sync grants the user full access to the data in the sync, including the ability to delete the data. Restoring data yourself only restores flat-folders and not nested ones, in order to fully restore everything Box must do the restoration. 
- Problems when two users edit the same file at the same time, unlike other collaboration tools
- While there is no official limit on the number of files uploaded at one time, Box itself recommends users not exceed 100,000 files at a time
- Deleting a user's account also deletes all the information they own, which can be problematic for users leaving a company

Link:

-   <http://opensource.box.com/box-python-sdk/tutorials/intro.html>

-   <https://github.com/box/box-python-sdk/tree/1.5/demo>

Install:

    pip install boxsdk

Creating an app:

Once you have created a Box account, go to the Developer Console and select Create New App. 
You will need to select what type of application you are building and an authentication method for your app and then enter an app name (you can change this later). Once the app is created you will receive a Developer Token that is valid for 60 minutes. You can implement authentication following the instructions in the Quickstart Guide https://developer.box.com/docs/quickstart-guides or use the Developer Token for temporary purposes. This token can be refreshed in the Configuration panel of the Developer Console. 

Create an app configuration file:
Find the Developer Token, Client ID, and Client Secret in the Configuration panel on the Developer Console @fig:box-config:

![Configuration Image](Box Configuration.png){#fig:box-config}

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
