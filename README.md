## NAME

hubstar is a command line tool to star/unstar a repository.

    $ hubstar satojkovic/hubstar
    Starred: https://github.com/satojkovic/hubstar
    
    $ hubstar -u satojkovic/hubstar
    Unstarred: https://github.com/satojkovic/hubstar

## SYNOPSIS

    % hubstar [-u|--unstar] <owner/repository>

## OPTIONS
    
    -u --unstar  unstar a target repository

## REQUIREMENTS

    PyGithub >= 1.24.1
    requests >= 2.2.1
