#! /usr/bin/python3

import argparse
import validators
import logging
import os
import subprocess
import yaml
from git import Repo

def finish(result):
    if result:
        logging.info("Pipeline fineshed successfuly!")
    else:
        logging.info("Pipeline execution failed!")

def checkout_to_branch(target_directory, branch):
    try:
        repo = Repo(target_directory)
        repo.git.checkout(branch)
    except CheckoutError:
        logging.error("Branch {} not found".format(branch))
        finish(False)

def checkout(repository_url, target_directory, branch=None):
    repo = Repo.clone_from(repository_url, target_directory)
    logging.info("Respository cloned to {}".format(target_directory))
    
    if branch:
        repo.git.checkout(branch)
        logging.info("Checked out to branch {}".branch)
    
    for line in os.listdir(target_directory):
        logging.info("\t{}".format(line))

def execute_pipeline(pipeline, tasks):
    pipeline_tasks = dict()
    for task in tasks:
        task_name = list(task.keys())[0]
        pipeline_tasks[task_name] = task[task_name]
    
    try:
        for step in pipeline:
            step_name = list(step.keys())[0]
            logging.info("Begin execution of step {}".format(step_name))
            for task in step[step_name]:
                logging.info("Executing task {}".format(task))
                logging.debug("{}".format(pipeline_tasks[task]))
            logging.info("Finished execution of step {}".format(step_name))
    except KeyError as e:
        logging.error("Task not found: {}".format(e))
        finish(False)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("pipeline", help="The pipeline to be executed")
    argument_parser.add_argument("repo", help="The repository where to find the code")
    argument_parser.add_argument("-b", "--branch", required=False, help="A target branch different than master to checkout to") # maybe that was useless

    arguments = argument_parser.parse_args()
    logging.info("Continuous Integration initiated")
    logging.debug("Loaded arguments {} and {}".format(arguments.pipeline, arguments.repo))

    if not validators.url(arguments.repo):
        logging.error("The given repository URL is not valid, can't work with that: {}".format(arguments.repo))
        result = False
        finish(result)
    else:
        logging.debug("Repository URL validated")
        logging.info("Begin repository checkout")
        repository_path = "{}/checkout/".format(os.environ["CI_PATH"])

        if arguments.branch:
            checkout(arguments.repo, repository_path, arguments.branch)
        else:
            checkout(arguments.repo, repository_path)
        
        try:

            with open("{}pipeline.yml".format(repository_path)) as pipeline_file:
                pipeline = yaml.load(pipeline_file)
                
                checkout(repository_path, pipeline["branch"])
                execute_pipeline(pipeline["pipelines"], pipeline["tasks"])
        except FileNotFoundError:
            logging.error("Did not found a pipeline.yml file in the given repository")
            finish(False)