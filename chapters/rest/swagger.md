Rest Services with Swagger
==========================

Swagger <https://swagger.io/> is a tool for developing API
specifications based on the OpenAPI Specification (OAS). It allows not
only the specification, but the generation of code based on the
specification in a variety of languages.

Swagger itself has a number of tools which together build a framework
for developing REST services for a variety of languages.

Swagger Tools
=============

The major Swagger tools of interest are:

Swagger Core

:   includes libraries for working with Swagger specifications
    <https://github.com/swagger-api/swagger-core>.

Swagger Codegen

:   allows to generate code from the specifications to develop Client
    SDKs, servers, and documentation.
    <https://github.com/swagger-api/swagger-codegen>

Swagger UI

:   is an HTML5 based UI for exploring and interacting with the
    specified APIs <https://github.com/swagger-api/swagger-ui>

Swagger Editor

:   is a Web-browser based editor for composing specifications using
    YAML <https://github.com/swagger-api/swagger-editor>

The developed APIs can be hosted and further developed on an online
repository named SwaggerHub <https://app.swaggerhub.com/home> The
convenient online editor is available which also can be installed
locally on a variety of operating systems including OSX, Linux, and
Windows.

Swagger Community Tools
=======================

notify us about other tools that you find and would like us to mention
here.

Swagger Toolbox
---------------

Swagger toolbox is a utility that can convert json to swagger compatible
yaml models. It is hosted online at

* <https://swagger-toolbox.firebaseapp.com/>

The source code to this tool is available on github at

.

It is important to make sure that the json model is properly configured.
As such each datatype must be wrapped in "quotes" and the last element
must not have a `,` behind it.

In case you have large models, we recommend that you gradually add more
and more features so that it is easier to debug in case of an error.
This tool is not designed to provide back a full featured OpenAPI, but
help you getting started deriving one.

Let us look at a small example. Let us assume we want to create a REST
service to execute a command on the remote service. We know this may not
be a good idea if it is not properly secured, so be extra careful. A good
way to simulate this is to just use a return string instead of executing
the command.

Let us assume the json schema looks like:

    {
       "host": "string",
       "command": "string"
    }

The output the swagger toolbox creates is

    ---
      required: 
        - "host"
        - "command"
      properties: 
        host: 
          type: "string"
        command: 
          type: "string"

As you can see it is far from complete, but it could be used to get you
started.

Based on this tool develop a rest service to which you send a schema in
JSON format from which you get back the YAML model.
