# Concourse Reports

## Purpose
Concourse Reports intends to recreate Jenkins JUnit reporting functionality in [Concourse CI](http://concourse.ci/), by giving a web interface that allows users to easily view and maintain JUnit test results originating from Concourse tasks.

## Who and why?
My name is Eric Duvic. As a fullstack/devops engineer, I feel like it's time to move away from Jenkins to better CI tooling. As I prefer Concourse, I would like to implement this feature to convince others that making the switch is possible.

## Components
Concourse Reports is comprised of three pieces:
- A Python application that provides functionality for storing, parsing, and maintaining JUnit test results. This includes shell commands as well as a RESTful API.
- A Dockerfile representing a Concourse resource that leverages the Python application to store JUnit test results generated from pipeline tasks.
- An Ember web frontend that gives users a graphical view and management of JUnit test results.

## Todo
- [ ] Add documentation on how to install all of this.
- [ ] Add unit tests for Python code
- [ ] Create frontend in Ember