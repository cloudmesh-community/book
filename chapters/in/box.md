# Box :o: :question:

## About 

Box is cloud storage service that allows users to store, access, collaborate, and share files, similar to DropBox. However, while DropBox started out as a service for storing personal files, Box is geared more towards business applications. Box also has its own platform offering APIs in multiple languages and an SDK for the development of custom applications and integrations, as well as many pre-built apps for integrating Box into various other tools and platforms. It has some limited project management tools in addition to its storage capabilities, including task and workflow management. Box offers free and paid versions for individual accounts and multiple types of business accounts that are charged on a per user basis. Finally, Box has just released Box Skills, a machine learning tool for automatically processing files uploaded to Box. 

## Limitations: 

- While Box offers unlimited storage, it's biggest business account has a 5GB file size limit with a 2GB limit on the smallest business plan and 250MB on the unpaid personal plan. Other services have no individual file size limit. 
- Using Box Sync grants the user full access to the data in the sync, including the ability to delete the data. Restoring data yourself only restores flat-folders and not nested ones, in order to fully restore everything Box must do the restoration. 
- Problems can occur when two users edit the same file at the same time, unlike other collaboration tools
- While there is no official limit on the number of files uploaded at one time, Box itself recommends users not exceed 100,000 files at a time
- Deleting a user's account also deletes all the information they own, which can be problematic for users leaving a company
- While Box has a collections feature, the only collection supported is the 'Favorites' collection, users are not able to make their own

REST:

https://developer.box.com/reference

Installation:

    pip install boxsdk
    
If you will be using JWT authentication for you app, you'll want to install its dependencies:

    pip install "boxsdk[JWT]"

## Creating an app:

Once you have created a Box account, go to the Developer Console and select 'Create New App'. 
You will need to select what type of application you are building and an authentication method for your app and then enter an app name (you can change this later). Once your app has been created, click View App. 

### Authentication with JWT:

In the Configuration panel of the Developer Console, scroll down to the section titled 'Add and Manage Public Keys' and click 'Generate a Public/Private Keypair':

![Box Add Key](box_add_key.png)

Once you have generated a keypair, a config.json file will automatically download. Save this file in a secure location as you will need it for authentication purposes. Finally, you will need to read in this config file into your app:

    from boxsdk import JWAuth
    from boxsdk import Client
    
    sdk = JWTAuth.from_settings_file(<path to config.json>)
    client = Client(sdk)

### Authentication with OAuth2:



## Box Methods

The Python SDK has several methods for creating objects and endpoints which you can then perform operations on, including: 
- client.user(user_id)
- client.folder(folder_id)
- client.file(file_id)
- client.search()
- client.events()

### Get information about a Box object

    # Get information about the logged in user (that's whoever owns the developer token):
    user = client.user().get()
    print(user.name)
    print(user.login)
    print(user.avatar_url)
    
    # Get information about the root folder (referenced by id '0'):
    folder = client.folder('0').get()
    print(folder.name)
    print(folder.item_status)

    # Get specific fields in one call:
    folder = client.folder(<folder id>).get(fields = ['created_at', 'size'])
    print(folder)

### Folders

    # Create a new folder:
    subfolder = client.folder(<folder id>).create_subfolder(<subfolder name>)
    
     # Delete a folder:
     client.folder(<folder id>).delete()
     
     # Copy a folder: 
     folder = client.folder(folder_id=<folder id>)
     destination = client.folder(<destination folder id>)
     copy_of_folder = folder.copy(destination)
     
     # Update a folder:
     folder = client.folder(folder_id=<folder id>).update_info({'name':'Updated name', 'description':'This has now been updated."})
     
     # Get all items in a folder:
     items = client.folder(folder_id=<folder id>).get_items()
     for entry in items.entries:
        print(entry.name)

### Uploading files
    
    # Upload a file to a Box folder:
    test_file = client.folder(folder_id=<folder id>).upload(<path to file>, <file name>)
    print(test_file.name)
    
    # Upload a stream to a Box folder:
    from io import StringIO
    stream = StringIO()
    stream.write("Test stream")
    stream.seek(0)
    stream_file = client.folder('0').upload_stream(stream, 'Stream File')
    print(stream_file.name)
    print(stream_file.content())
    
    # Upload a new version of a file:
    client.file(<file id>).update_contents(<path to file>)
    
### File upload errors
A file upload will fail if there is already a file in the folder with the same name, if the file is too big, or if there is not enough storage. To avoid errors, Box has an exception API that will check if a file will be accepted before sending it to Box: 
    
    # Enable preflight checks:
    file = 'test.txt'
    try:
        test_file = client.folder('0').upload('test.txt', 'Test File', preflight_check=True)
        print(test_file.name)
        print(test_file.content())
    except BoxAPIException:
        pass
        
Which will return the following:

    "OPTIONS https://api.box.com/2.0/files/content" 409 466
    {'Date': 'Thu, 24 Jan 2019 16:30:46 GMT', 'Content-Type': 'application/json', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Strict-Transport-Security': 'max-age=31536000', 'Cache-Control': 'no-cache, no-store', 'Content-Encoding': 'gzip', 'Vary': 'Accept-Encoding', 'BOX-REQUEST-ID': '0rgjouev2logn8gqcn1fauco84o', 'Age': '0'}
    {'code': '---_use',
     'context_info': {'conflicts': {'etag': '0',
                                    'file_version': {'id': '411411432162',
                                                     'sha1': '02d92c580d4ede6c80a878bdd9f3142d8f757be8',
                                                     'type': 'file_version'},
                                    'id': '389113382562',
                                    'name': 'Test File',
                                    'sequence_id': '0',
                                    'sha1': '02d92c580d4ede6c80a878bdd9f3142d8f757be8',
                                    'type': 'file'}},
     'help_url': 'http://developers.box.com/docs/#errors',
     'message': 'Item with the same name already exists',
     'request_id': 'slj5jkfzi55kba81',
     'status': 409,
     'type': 'error'}
        
 ### Deleting, copying, and downloading files
 
    # Delete a file:
    client.file(file_id=<file id>).delete()
    
    # Copy a file: 
    file = client.file(file_id=<file id>)
    destination = client.folder(folder_id=<folder id>)
    copy_of_file = file.copy(destination)
    
    # Download a file:
    file_to_download = client.file(file_id=<file id>).get()
    output = open(file_to_download.name, 'wb')
    file_to_download.download_to(output)
    
### Searching
The query string used in a search can include object names, description, text content, or other object data. 

    items = client.search().query(<query string>, file_extensions = ['png', 'txt'], fields = ['name', 'description'])
    for entry in items.entries:
        print(entry.id)
        
### Shared links
Shared links give read-only access to a file through a URL. Specifying the access level of a shared link determines whether users will need to authenticate with Box in order to view the file. 

    # Creating a shared link:
    url = client.file(file_id=<file id>).get_shared_link()
    
    # Retrieving a shared link that has already been created:
    url = client.file(file_id=<file id>).shared_link['url']
    

Pybox
-----
Pybox provides an way to work with Box files from the command line. Documentation on how to set up and use pybox can be found at <https://github.com/hzheng/pybox>
