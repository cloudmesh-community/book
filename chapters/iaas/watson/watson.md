# What is IBM Watson and why is it important?

In years past we traditionally typed our questions into a query based search engine and it would return relevant content.  As we start interacting with our devices more in conversation through natural language processing, we need an answer to a question - not a list of relevant information.  We need the power of question answering (QA) technology.  

IBM's Watson's is well known for its ability to play and successfully win the popular gameshow, jeopardy!  IBM startled the world in 2011 when Watson beat Jeopardy! pros Ken Jennings and Brad Rutter over several rounds.  Watson completed the formidable task by combining 15 terabytes of human knowledge with a variety of computer disciplines including automated reasoning, natural language processing, knowledge representation, information retrieval and machine learning.

IBM's goal of having computers understand the questions humans ask while providing answers in a similar fashion is not unique to them.  In recent years, products like Amazon's Alexa and Google Home have brought the awareness of this capability mainstream for millions of households.  In short, it has become a race to serve up relevant content with the least amount of effort in the most consumable format.

## How can we use Watson?

IBM's Watson has a rich set of Developer Services (https://www.ibm.com/watson/developer/) that allow users to stand on the shoulders of the IBM developers using their AI framework to "bolt on" new or improved applications that sit on top.

There are a breadth of services available.  Watson Discovery is used to mine through data to find trends and surface patterns.  Watson Visual Recognition is used to classify content using machine learning.  Watson Assistant provides a framework for chatbots and virtual agents.

While The next section walks through how to create a free account,  let's continue with an example of leveraging a foundation and building on-top with Watson Assistant Basic.  

Instead of starting with a blank page IBM steps are put in place and working examples can be customized.  

[](images/1WatsonAssistentBasic.PNG)
[](images/2WatsonAssistentBasicCode.PNG)
[](images/3WatsonAssistent3steps.PNG)
[](images/4Watsoneditsample.PNG)
[](images/5Watsonaddingexample.PNG)
[](images/6Watsoncustomizesettings.PNG)

In the case above when I was trying the Watson Assistant It was not personal when I asked the Assistant's name so it can be modified to "digress!"

In addition to using these modules to help build there is also a variety of APIs and services that can be used:

The list of APIs and services include:
* Watson Assistant
* Watson Discovery
* Natural Language Understanding
* Discovery News
* Knowledge Studio
* Language Translator
* Natural Language Classifier
* Personality Insights
* Tone Analyzer
* Visual Recognition
* Speech to Text
* Text to Speech

## Creating an account

This section will guide through the processes of creating an IBM Watson
account and explain the free tier details so that you can leverage the
tools and products available in AWS for your work and research.

* A valid email address

First you need to visit the
[IBM Watson home page](https://www.ibm.com/watson/index.html) and
click in the "Get Started Free" link on the top right corner. You will
then be asked to provide some basic details including your email
address as shown in the image below

![](images/ibmwatson_signup.png)

Once you have submitted the signup form an confirmation email will be
sent to your email account, check your inbox and click on the confirm
account link in the email you receive. This will activate your IBM
Watson account. Once you have accepted the terms and conditions you
will be taken to the product and service catalog of IBM Watson as
shown in the image below.

![](images/catalog_ibm_watson.png)

## Understanding the free tier

IBM watson provides a set of services for free with their Lite
account. Since you did not provide any credit/debit card information
when creating the account, by default you will have a Lite account.
The lite plan does apply usage caps for services offered under the
plan. If you need to expand and remove such limits you would have to
upgrade to a payed account However the free quotas are typically more
than sufficient for testing and learning purposes. For example under
the Lite plan you can use the "Watson Assistant" service with caps
such as 10K API calls per month.
