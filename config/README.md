# What is this for?

This file can be used to provide users with instructions for how to reproduce local configuration with their own credentials. You can edit the file however you like, but you may wish to retain the information below and add your own section in the section titled **Instructions**.

## Main configuration

Since this project uses Dynaconf for managing configuration files, `config.py` is the file that will hold information on settings files and load it like module.

## Local configuration

The `local` folder should be used for configuration that is either user-specific (e.g. IDE configuration) or protected (e.g. secrets).

> *Note:* Please do not check in any local configuration to version control.

## Base configuration

The `base` folder is for shared configuration, such as non-sensitive and project-related configuration that may be shared across team members.

WARNING: Please do not put access credentials in the base configuration folder.

#### Model configuration

The `model` folder is meant for values used in statistical models used in the project. Making it easier for code maintenance and code cleaning.

#### Process configuration

The `process` folder is used to store configuration values for processing data used in the application.