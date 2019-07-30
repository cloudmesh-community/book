# AWS in Julia

There are two Julia libraries that provide programmatic interface with AWS:
AWS.jl and AWSCore.jl. We will focus on AWSCore.jl, as it is under active
development and provides more infrastructure types and high-level packages.
We include a note about AWS.jl for completeness. The following information can
be found at <https://juliacloud.github.io/AWSCore.jl/build/index.html>

## AWSCore.jl

AWSCore.jl (hereinafter AWSCore) was only successfully tested on Julia 0.6.0. 
Note that multiple versions of Julia can be installed and run by linking the binary 
files to the shell session.  See "Installing Julia".  

### Credentials

Most AWSCore functions take an ```AWSConfig``` dictionary as an initial
argument, which passes in both credentials and region variables.  Credentials
can be gathered either from the default ```/.aws/credentials``` file or by
setting them as environment variables as discussed elsewhere in this chapter.  

AWSCore will attempt to read in credentials from (in order) Environment Variables, an
```~/.aws/credentials``` file, or EC2 Instance Credentials which can be set via the AWS CLI.  
Note that the third method is not recommended! 

Here, we use an AWS Credentials file located on Ubuntu at ```~/.aws/credentials```.  Ensure
that the user has appropriate permissions to create, delete, and modify AWS objects and services. 
We begin with a simple script that will allow creation of S3 containers.  
To set up a script that will create an S3 container and store a simple object, we 
initialize the Julia Dev environment.    First, create a new directory called "Julia App" and populate
with one ```.jl``` file:

```mkdir JuliaApp```
```cd JuliaApp```
```touch julia-app.jl```

Assuming Julia is properly installed, simply type the command for the executable created earlier.  
For instance, ```julia0.6```. This will start a Julia REPL inside the JuliaApp directory just created.  
Open a text/file editor to edit the julia-app.jl file:

```emacs julia-app.jl```

Julia is comparable to Python in its import statements in that to use a particular package or library, 
the user must specify that package prior to its use.  With the blank ```.jl``` open, import and 
initialize the following packages: 

```julia
> Pkg.add("AWSCore")
> Pkg.add("AWSS3")
> using AWSS3
> using AWSCore.Services
```
Now include in the script the AWS_Config() argument, which typically contains AWS Credentials and a 
Region parameter: 

```julia
> aws = AWSCore.aws_config()
```
Before proceeding, save the file and run the script in the opened Julia REPL.  Make sure that the working directory
is the same as where your script is located by issuing in Julia ```pwd()```.  To run the script, type in the Julia REPL: 

```julia
> import Pkg
> include("julia-app.jl")
```
Read AWS credentials into your environment session by adding the following command to your script: 

```julia
> aws = aws_config()
```

### S3 Containers

You should see some output indicating that the credentials have been created or read successfully. 
Now we can create a bucket and put an object in the bucket. Very basically, the syntax for creating a bucket 
using the low-level AWSCore services is: ```s3_create_bucket(credentials, bucketname```.  That's it!

Add the following to your script, ensuring that your name complies with AWS bucket naming conventions: 

```julia
s3_create_bucket(aws, "<bucket.name>")
s3_enable_versioning(aws, "<bucket.name>")
```

#### Listing buckets and Objects

Now we can run our script and verify that the bucket was created (see running Julia script above). We will further develop this script to include docopts to make managing S3 buckets and objects much easier. To expand on the previous example, add in the ```s3_list_buckets(credentials)``` or ```list_objects(credentials, bucket)``` functions. 

#### Adding objects to existing bucket

```julia
> s3_put(aws, "<bucket.name>", "key", "Hello!")
```

## AWS.jl

AWS.jl is no longer under active development.  The library repository can be found here:
<https://github.com/JuliaCloud/AWS.jl>
