# AWS in Julia

There are two Julia libraries that provide programmatic interface with AWS:
AWS.jl and AWSCore.jl. We will focus on AWSCore.jl, as it is under active
development and provides more infrastructure types and high-level packages.
We include a note about AWS.jl for completeness. The following information can
be found at <https://juliacloud.github.io/AWSCore.jl/build/index.html>

## AWSCore.jl
AWSCore.jl (hereinafter AWSCore)

### Credentials
Most AWSCore functions take an ```AWSConfig``` dictionary as an initial
argument, which passes in both credentials and region variables.  Credentials
can be gathered either from the default ```/.aws/credentials``` file or by
setting them as environment variables as discussed elsewhere in this chapter.  

## AWS.jl

Julia's AWS API (AWS.jl) is straightforward to configure and is similar to
Python. Using the Julia-AWS API carries the advantage of users not having to
switch between environments and languages. The API functionality in Julia is
currently limited, however, to EC2, S3, SQS, and Auto Scaling.
https://github.com/JuliaCloud/AWS.jl. Advanced APIs have not been tested yet.
Further development is in progress with the AWSSDK.jl package. 
