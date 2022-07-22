# Helper for making new build and uploading it on pypi.org
# so you don't have to remember this shell-commands.
#
# Safe to delete this file if your project is not intended to be published on pypi.

python3 setup.py sdist
python3 -m twine upload dist/* --skip-existing
