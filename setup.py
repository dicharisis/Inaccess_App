from setuptools import setup, find_packages



with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()


setup(
    name = 'app',
    version = '0.0.1',
    author = 'Charisis Dimitris',
    author_email = 'dicharisis@gmail.com',
    description = 'A CLI app asked from Inaccess due to hiring proccess',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/dicharisis/Inaccess_App',
    py_modules = ['app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        app=app:main
    '''
)
