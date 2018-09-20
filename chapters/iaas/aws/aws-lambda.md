# AWS Lambda :o: {#s-aws-lambda}

---

**:mortar_board: Learning Objectives**

* Leran about AWS lambda
* Try out AWS Lambda practucally

---

AWS Lambda is an event-driven, serverless computing platform provided
by Amazon as a part of the Amazon Web Services. It is a computing
service that runs code in response to events, runs the code that has
been loaded into the system and automatically manages the computing
resources required by that code. According to the the Lambda product page

> “AWS Lambda lets you run code without provisioning or managing
> servers.” [:warning: ciite missing](cite missing) 

For example, one of the use-cases would be that everytime AWS Lambda
could resize the picture, after it is uploaded onto AWS S3 system and
rendered on different devices like phone, ipad or desktop. The event
that triggers the Lambda function is the file being uploaded to S3.
Lambda then executes the function of resizing the image. The Seattle
Times uses the AWS Lambda to automatically resize the images.

One key point to note here is that Amazon charges only when the
functions are executed. So, The Seattle Times is charged for this
service only when the images are been resized. Lambda can be used for
Analytics. So lets say, there has been a purchase of a house on
zillow, this data can be saved into a NoSQL database and this entry
into the database is an event which can trigger Lambda function to
load the order information into Amazon Redshift. Then we can run
Analytics on top of this data. We can also build serverless
applications composed of functions that are triggered by events and
automatically deploy them using AWS CodePipeline and AWS CodeBuild.
For more information, see Deploying Lambda-based Applications.

There are development groups or companies mainly startups, where they want to just focus on their application development without wanting to care about their infrastructure and they also want that they pay for what they use. Hence, AWS Lambda comes into play which satisfies all their needs.

Ironically, Lambda could be a threat to one of the Amazon's most
popular EC2. Developers can build apps that run entirely on Lambda
functions instead of spinning up EC2 VMs. Amazon may be out-innovating
itself with Lambda.

### Serverless Computing

In Serverless Computing, servers are still there, its just that we
dont need to manage them.

Another advantage of going serverless is that you no longer need to
keep a server running all the time. The *server* suddenly appears when
you need it, then disappears when you’re done with it. Now you can
think in terms of functions instead of servers, and all your business
logic can now live within these functions.

In AWS Lambda, we have triggers. Lambda Functions can be triggered in
different ways: an HTTP request, a new document upload to S3, a
scheduled Job, an AWS Kinesis data stream, or a notification from AWS
Simple Notification Service (SNS).

### How to run your first AWS Lambda function in the cloud - Example

Let us create our first Lambda function.

Step 1: The very first thing we need is an AWS account. (There is already a section on this, please go through that to understand how to create an AWS account - https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#creating-an-account )

Step 2: We will be writing a function that we call `isPalindrome`, which will check
if the string is palindrome or not.

:o: can syntax be improved so we can see the text

```
const isPalindrome = (string) => {
  const reverse = string.split('').reverse().join('');
  	const isPalindrome = (string === reverse);
      const result = isPalindrome ? `${string} is a Palindrome` :
       `${string} is not a Palindrome`;
              return result;
  };
```
  
This example we store in a file as javascript named `isPalindrome.js`

Step 3: Let’s see how to create an AWS Lambda function - isPalindrome. Firstly, go to AWS Console. (see +@fig:aws-lambda-console).

 
![AWS Console](images/aws_console.png){#fig:aws-lambda-console}
 
 
Step 4: Now we will select AWS Lambda from console and then click on <span style="background-color:blue;color:white">&nbsp;Get Started Now&nbsp;</span> (see +@fig:aws-lambda-lambda)
 
![AWS Lambda](images/aws_lambda.png){#fig:aws-lambda-lambda}

Step 5: For runtime, we will select Node.js 6.10 and then press “Blank Function.” (see +@fig:aws-lambda-blank).
 
![Blank Function](images/aws_lambda_1.png){#fig:aws-lambda-blank}

Step 6: We will skip this step and press <span style="background-color:blue;color:white">&nbsp;Next&nbsp;</span>. (see +@fig:aws-lambda-next)

![Next](images/aws_lambda_2.png){#fig:aws-lambda-next}
 
Step 7: Let’s give the Name as isPalindrome and put in a description of our new Lambda Function, or we can leave it blank. (see +@fig:aws-lambda-description)

![Description](images/aws_lambda_3.png){#fig:aws-lambda-desccription}

Lambda function is just a function, named as *handler* here and the
function takes three parameter - event, context and a callback
function. The callback will run when the Lambda function is done and
will return a response or an error message. For the Blank Lambda
blueprint, response is hard-coded as the string `Hello from Lambda`.

Step 8: Please scroll down for choosing the Role “Create new Role from template”, and for Role name we are going to use isPalindromeRole in our case.
For Policy templates, we will choose “Simple Microservice” permissions.
 (see +@fig:aws-lambda-policy)
 
![Policy](images/aws_lambda_4.png){#fig:aws-lambda-policy}

Step 9: For Memory, 128 megabytes is more than enough for our simple
function. As for the 3 second timeout, this means that — should the
function not return within 3 seconds — AWS will shut it down and
return an error. Three seconds is also more than enough. Leave the
rest of the advanced settings unchanged. (see +@fig:aws-lambda-settings)

![Advanced Settings](images/aws_lambda_5.png){#fig:aws-lambda-settings}

Step 10: Let’s click on the “Create function” button now to create our first Lambda function. (see +@fig:aws-lambda-create)

![Create](images/aws_lambda_6.png){#fig:aws-lambda-create}

Step 11: Now that we have created our first Lambda function, let's test it by clicking <span style="background-color:blue;color:white">&nbsp;Test&nbsp;</span> (see +@fig:aws-lambda-test)
 
![Test](images/aws_lambda_7.png){#fig:aws-lambda-test}

The output will be the hard-coded response of “Hello from Lambda.” from the created Lambda function. (see +@fig:aws-lambda-hello)
 
![Hello](images/aws_lambda_8.png){#fig:aws-lambda-hello}

Step 12: Now let us add our `isPalindrome.js` function code here to
Lambda function but instead of return result use `callback(null,
result)`. Then add a hard-coded string value of abcd on line 3 and
press `Test`. (see +@fig:aws-lambda-press)

![Press Test](images/aws_lambda_9.png){#fig:aws-lambda-press}

The output will be `abcd is not a Palindrome` (see +@fig:aws-lambda-output)

![Output](images/aws_lambda_10.png){#fig:aws-lambda-output}

Similarly, let us try with string `abcdcba` and in this case output
should return `abcdcba is a Palindrome`. Thus, our Lambda function is
behaving as expected.

