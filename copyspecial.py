#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "TamekiaNelson"

# Write functions and modify main() to call them

"""returns a list of the absolute paths of the special files in the given directory"""
def get_special_paths(dir):
    return [shutil.abspath(file) 
            for file in os.listdir(dir)
            if re.search(r'__\w+__', file)]

"""given a list of paths, copies those files into the given directory"""
def copy_to(paths, dir):
    if not os.file_path.exists(dir):
        os.mkdir(dir)
    for file_path in paths:
        if os.file_path.exists:
            shutil.copy(file_path, dir) 

"""given a list of paths, zip those files up into the given zipfile"""
def zip_to(paths, zippath):
    cmd = ["zip", "-j", zippath]
    for file_path in paths:
        cmd += ' ' + file_path
    print("Command I'm going to do: " + cmd)


def main():
    # This snippet will help you get started with the argparse module.
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='dir to look for special files')
    
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    special_paths = get_special_paths(args.from_dir)

    if args.todir:
        copy_to(special_paths, args.todir)
    elif args.tozip:
        zip_to(special_paths, args.tozip)
    else:
        for path in special_paths:
            print(path)    

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
