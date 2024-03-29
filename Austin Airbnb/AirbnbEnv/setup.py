from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='airbnb',
    version='0.1',
    description='Analysis of the AirBnB Austin',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    # Substitute <github_account> with the name of your GitHub account
    url='https://github.com/atalebizadeh/DS-Career-Track/tree/master/Capstone%20Project%202/AirBnB%20Austin/AirBnBEnv',
    author='Alireza Talebizadeh',  # Substitute your name
    author_email='alireza.talebizadeh@gmail.com',  # Substitute your email
    license='MIT',
    packages=['AirBnB'],
    install_requires=[
      	'pypandoc>=1.4'
    ]
)
