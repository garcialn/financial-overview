# What is this for?

This file can be used to provide users with instructions for how to reproduce local configuration with their own credentials. You can edit the file however you like, but you may wish to retain the information below and add your own section in the section titled **Instructions**.

## Main configuration

Since this project uses **Dynaconf** for managing configuration files, `config.py` is the file that will hold information on settings files to be used through out the project.

## Local configuration

The `.secrets.toml` file is used for configuration that is either user-specific (e.g. IDE configuration) or protected (e.g. secrets).

> *Note:* Please do not check in any local configuration to version control.

## Project configuration

The `setting.toml` file is for general configuration, such as non-sensitive and project-related configuration that may be shared across team members.

> **WARNING**: Please do not put access credentials in the base configuration folder.

## Data configuration

The `data_seting.toml` file is meant for values used for any data related configuration that will be required, from extraction, processing and modeling data.
