# Excersises

E.OpenAPI.1:

> In Section
> [Step 1: Define Your REST Service](#step-1-define-your-rest-service), we introduced a
> schema.  The question relates to termsOfService: Investigate what
> the termOfService attribute is and suggest a better value. Discuss
> on piazza.

E.OpenAPI.2:

> In Section
> [Step 1: Define Your REST Service](#step-1-define-your-rest-service), we introduced a
> schema.  The question relates to model: What is the meaning of model
> under the definitions?

E.OpenAPI.3:

> In Section
> [Step 1: Define Your REST Service](#step-1-define-your-rest-service), we introduced a
> schema.  The question relates to \$ref: what is the meaning of the
> \$ref. Discuss on piazza, come up with a student answer in class.

E.OpenAPI.4:

> In Section
> [Step 1: Define Your REST Service](#step-1-define-your-rest-service), we introduced a
> schema.  What does the response 200 mean. Do you need other
> responses?

> After you have gone through the entire section and verified it works
> for you add create a more sophisticated schema and add more
> attributes exposing more information from your system.

> How can you for example develop a rest service that exposes portions
> of your file system serving large files, e.g. their filenames and
> their size? How would you download these files? Would you use a rest
> service, or would you register an alternative service such as ftp,
> DAV, or others? Please discuss in piazza. Note this will be a
> helping you to prepare a larger assignment. Think about this first
> before you implement.

> You can try expand the API definition with more resources and
> actions included. E.g., to include more detailed attributes in the
> CPU object and to have those information provided in the actual
> implementation as well. Or you could try defining totally different
> resources.

> The codegen tool provides a convenient way to have the code stubs
> ready, which frees the developers to focus more on the API
> definition and the real implementation of the business logic. Try
> with complex implementation on the back end server side code to
> interact with a database/datastore or a 3rd party REST service.

> For advanced python users, you can naturally use function
> assignments to replace the `cpu_get()` entirely even after loading
> the instantiation of the server. However, this is not needed. If you
> are an advanced python developer, please feel free to experiment and
> let us know how you suggest to integrate things easily.
