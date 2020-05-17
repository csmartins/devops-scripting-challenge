#! /usr/bin/python3

import argparse

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("pipeline", help="The pipeline to be executed")
argument_parser.add_argument("repo", help="The repository where to find the code")

arguments = argument_parser.parse_args()

print(arguments.pipeline)
print(arguments.repo)