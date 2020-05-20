#! /usr/bin/python3

import argparse
import validators
import logging
import os
import subprocess
from git import Repo

def checkout(repository_url, target_directory, branch=None):
    repo = Repo.clone_from(repository_url, target_directory)
    logging.info("Respository cloned to {}".format(target_directory))
    
    if branch:
        repo.git.checkout(branch)
        logging.info("Checked out to branch {}".branch)
    
    for line in os.listdir(target_directory):
        logging.info("\t{}".format(line))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("pipeline", help="The pipeline to be executed")
    argument_parser.add_argument("repo", help="The repository where to find the code")
    argument_parser.add_argument("-b", "--branch", required=False, help="A target branch different than master to checkout to")

    arguments = argument_parser.parse_args()
    logging.info("Continuous Integration initiated")
    logging.debug("Loaded arguments {} and {}".format(arguments.pipeline, arguments.repo))


    if not validators.url(arguments.repo):
        logging.error("The given repository URL is not valid, can't work with that: {}".format(arguments.repo))
    else:
        logging.debug("Repository URL validated")
        logging.info("Begin repository checkout")
        if arguments.branch:
            checkout(arguments.repo, "{}/checkout/".format(os.environ["CI_PATH"]), arguments.branch)
        else:
            checkout(arguments.repo, "{}/checkout/".format(os.environ["CI_PATH"]))

