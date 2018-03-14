from setuptools import setup

VERSION = '1.0.0'
REPO = 'https://github.com/sw5cc/Excel2MySQL'

setup(
    name='Excel2MySQL',
    py_modules=['Excel2MySQL'],
    version=VERSION,
    description='',
    author='sw5cc',
    author_email='sw5cc.125pflops@gmail.com',
    license='MIT',
    url=REPO,
    download_url='{0}/archive/{1}.tar.gz'.format(REPO, VERSION),
    keywords=['Excel', 'MySQL'],
    install_requires=['mysql-connector-python', 'openpyxl', 'redis']
)
