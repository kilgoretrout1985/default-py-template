from typing import List
import setuptools
import os
from pkg_resources import parse_requirements


def load_requirements(fname: str) -> List[str]:
    """
    This allows us to store all project requirements in `requirements*.txt`
    files, lots of people are used to. And here in setup.py we dynamically 
    read them from txt-files to avoid duplication.
    """
    requirements = []

    # Since this is a default stub there will be projects with empy or with no
    # requirements.txt and requirements.dev.txt. Handle that gracefully.
    # This also helps to avoid copying requirements.dev.txt into Docker container.
    if not os.path.isfile(fname):
        return []
    
    with open(fname, 'r') as fp:
        for req in parse_requirements(fp.read()):
            extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
            requirements.append(
                '{}{}{}'.format(req.name, extras, req.specifier)
            )
    return requirements


if __name__ == "__main__":
    SETUP_CWD = os.path.dirname(os.path.abspath(__file__))
    try:
        README = open(os.path.join(SETUP_CWD, 'README.md')).read()
    except FileNotFoundError:
        README = ""

    setuptools.setup(
        # metadata
        name = 'projectname',
        version = '0.0.1',
        author = 'Yuriy Zemskov',  # TODO: CHANGE THIS
        author_email = 'zemskyura@gmail.com',  # TODO: CHANGE THIS
        license = 'MIT',
        license_files = ('LICENSE',),
        description = 'your description here',
        long_description = README,
        long_description_content_type = "text/markdown; charset=UTF-8",
        url = 'https://github.com/kilgoretrout1985/default-py-template',  # TODO: CHANGE THIS
        platforms = 'unix, linux, osx, cygwin, win32',
        classifiers = [
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
        ],

        # options
        python_requires = '>=3.7',
        # packages = find_packages(exclude=['tests']),
        packages = ['projectname'],
        include_package_data = True,
        # for package_data see MANIFEST.in file
        package_dir = {'': 'src'},
        install_requires = load_requirements(os.path.join(SETUP_CWD, 'requirements.txt')),
        extras_require = {'dev': load_requirements(os.path.join(SETUP_CWD, 'requirements.dev.txt'))}
    )
