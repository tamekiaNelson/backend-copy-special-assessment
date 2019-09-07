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
import argparse
import sys
import subprocess

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
    if not os.path.exists(dir):
        os.mkdir(dir)
    for path in paths:
        if os.path.exists:
            shutil.copy(path, dir) 

"""given a list of paths, zip those files up into the given zipfile"""
def zip_to(paths, zippath):
    cmd = ['zip -j ' + zippath]
    for path in paths:
        cmd += ' ' + path
    print("Command I'm going to do: " + cmd)
    subprocess.call(cmd)
    


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

    paths = get_special_paths(args.from_dir)

    if args.todir:
        copy_to(paths, args.todir)
    elif args.tozip:
        zip_to(paths, args.tozip)
    else:
        for path in paths:
            print(path)    

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
