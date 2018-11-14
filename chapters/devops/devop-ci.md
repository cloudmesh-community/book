# DevOp - Continuous Improvement: :exclamation: fa18-516-11


|          |                                       |
| -------- | ------------------------------------- |
| title    | DevOp - Continuous Improvement        | 
| status   | 10                                    |
| section  | DevOp                                 |
| keywords | DevOp, CI, CD, Continuous Improvement |

Deploying enterprise applications has been always challenging. Without consistent and reliable processes and practices, 
it would be impossible to track and measure the deployment artifacts – which code-files and configuration data have been 
deployed to what servers and what level of unit and integration tests have been done among various components of the 
enterprise applications. Deploying software to cloud is much more complex, given **Dev-Op** teams do not have extensive access 
to the infrastructure and they are forced to follow the guidelines and tools provided by the cloud companies. 
In recent years, Continuous Integration (**CI**) and Continuous Deployment (**CD**) are the **Dev-Op** mantra for 
delivering software reliably and consistently. 

While **CI/CD** process is, as difficult as it gets, monitoring the deployed applications is emerging as new challenge, 
especially, on an infrastructure that is sort of virtual with VMs in combination with containers. 
Continuous Monitoring (**CM**) is somewhat new concept, that has gaining rapid popularity and becoming integral part of the 
overall **Dev-Op** functionality. Based on where the software has been deployed, continuous monitoring can be as simple as, 
monitoring the behavior of the applications to as complex as, end-to-end visibility across infrastructure, heart-beat and 
health-check of the deployed applications along with dynamic scalability based on the usage of these applications. 
To address this challenge, building robust monitoring pipeline process, would be a necessity. Continuous Monitoring aspects get 
much better control, if they are thought as early as possible and bake them into the software during the development. 
We can provide much better tracking and analyze metrics much closer to the application needs, if these aspects are considered very early into the process. 
Cloud companies aware of this necessity, provide various **Dev-Op** tools to make **CI/CD** and continuous monitoring as easy as possible. 
While, some of these tools and aspects are provided by the cloud offerings, some of them must be planned and planted into our software.


At high level, we can think of a simple pipeline to achieve consistent and scalable deployment process. 
**CI/CD** and Continuous Monitoring Pipeline:

**Step 1 - Continuous Development - Plan, Code, Build and Test:** Planning, Coding, building the deployable artifacts – code, configuration, database, etc. 
and let them go through the various types of tests with all the dimensions – 
technical to business and internal to external, as automated as possible. All these aspects come under Continuous Development.

**Step 2 - Continuous Improvement - Deploy, Operate and Monitor:** Once deployed to production, how these applications get operated – bug and health-checks, performance and 
scalability along with various high monitoring – infrastructure and cold delays due to on-demand VM/container 
instantiations by the cloud offerings due to the nature of the dynamic scalability of the deployment and 
selected hosting options. Making necessary adjustments to improve the overall experience is 
essentially called Continuous Improvement.
