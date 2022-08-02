# default-py-template

Default Python project template with linter, type checking and test environment 
setup. Also supporting github auto-running tests on push to repository.

![Tests](https://github.com/kilgoretrout1985/default-py-template/actions/workflows/tests.yaml/badge.svg)

## Use

To use this project's structure in a new project without leaving dependency 
on this stub project:

1)
```
git clone https://github.com/kilgoretrout1985/default-py-template.git yourrealprojectname 
cd yourrealprojectname
rm -drf .git
git init .
```

2) Search all occurences of `projectname` in project files (and in dir- and file-names!) 
and replace them with `yourrealprojectname`.

3) Browse `setup.cfg` and `README.md` to change author name, email and github 
links to the actual ones.

4)
```
python3 -m venv .env && \
source .env/bin/activate && \
pip install -U pip && \
pip install -r requirements_dev.txt
```

Happy commits!

## (c)

This repo is mainly based on [this video](https://www.youtube.com/watch?v=DhUpxWjOhME).
