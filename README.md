PayCertify Scripting Challenge
======
We wrote a simple dummy Java app, but we decided that we don't want to use Jenkins nor CircleCI for our Continuous Integration, instead, we've decided to ask you to write a simple Continuous Integration system for us :)

Your challenge is to write a script that will execute a simple pipeline (already designed) inside our Git repository:

https://github.com/PayCertify/devops-scripting-helloworld

Inside the repository, we've added a `pipeline.yml` file. Your CI tool will lookup this file to execute the requested pipeline that will be implemented in your tool.

In a glance, your script needs to:

* Fetch git code (https://github.com/PayCertify/devops-scripting-helloworld)
* Parse the `pipeline.yml`
* Run selected pipeline


Pipeline.yml Format
======
The pipeline file has only three main hashes.

Branch: Repository branch that should be used to execute the code.

Tasks: Commands that can be used to create a pipeline

Pipelines: Group of ordered tasks

Script Arguments
======
* Pipeline name, E.g: build
* Git repository URL

Examples
=====
Assuming your script name is `pipeline` - You're free to give a name to your CI tool :)

Should fetch git code and execute `build` pipeline:
```shell
./pipeline build https://github.com/PayCertify/devops-scripting-helloworld.git
```

Testing
=====
You can test your script on your personal computer if you have `git`, `maven`, `unzip` and `java` installed. 

If you don't have it installed, we got your back, there is `Dockerfile` in this repo that you can use to run your script.

Tasks to be completed
======
* Create a Terraform module that will provision a VM or Container Orchestration Service (EKS? Fargate?)
where the build generated will be deployed.
* Create your CI tool from scratch, using your own code.

Requirements
======
* Your script should execute the pipeline without errors.
* Provide meaningful log to the user during pipeline execution.
* Fail fast if something bad happens

### Language Choice
Your code should be written using one of the below languages:
* Go
* Groovy
* Python
* Ruby
* PHP


Evaluation Topics
======
* Code design
* Best practices
* Unit / Integration Tests
* Comments / Documentation

Delivery Instructions
======
* You must fork this repository into your own account.
* Once finished, you must open a PR in PayCertify's repo and send the PR url to the recruiter.
* After your evaluation, if you passed, the recruiter will schedule the next step in the interview process.

## Format

* You must be prepared to walk an evaluator through all the created artifacts including tests
* Mention anything that was asked but not delivered and why, and any additional comments.

Thank you,
The PayCertify Recruiting Team
