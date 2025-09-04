# AI implementation of a recommendations engine for all my internal documents

## Implement setup.py
1. Run setup.py using to trigger setup.py including installing requirements and packages
```
pip install -e .
```
Always run this after creating packages and modules, especially as we are adding new config and utils directories.

Note to remove cached files from Github, do
`git rm --cached file_name`
if it is a directory, do
`git rm -r --cached folder_name`
Git will stop tracking the file
Afterwards commit and push changes to remote

2. Implement configuration.