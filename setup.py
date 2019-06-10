import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='tagged-users',
    version='1.1',
    author='Siddharth Dushantha',
    author_email='siddharth.dushantha@gmail.com',
    description='Get all the usernames of the people who got tagged in an Instagram post',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sdushantha/tagged-users',
    py_modules=['tagged-users'],
    scripts=['tagged-users/tagged-users'],
    install_requires=['requests']
)
