import setuptools

__version__='0.0.1'

with open('README.md', 'r', encoding='utf-8') as f:
    long_description=f.read()

REPO_NAME='cnn classifier'
AUTHOR_NAME='anjan'
SRC_REPO='CLASSIFIER'
AUTHOR_EMAIL='anjan@outlook.in'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='this is my classification project',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}',

    project_url={
        'Bug_tracker':f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues'},
        package_dir={"":"src"},
        packages=setuptools.find_packages(where='src')
        )