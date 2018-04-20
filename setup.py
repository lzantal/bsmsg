from setuptools import setup
from bsmsg import VERSION


setup(
    name = 'bsmsg',
    version = VERSION,
    description = 'Bootstrap Messages',
    long_description = 'Bootstrap Messages using the builtin Django messages framework',
    author = 'LZAntal',
    author_email = 'LZAntal@gmail.com',
    url = 'https://github.com/lzantal/bsmsg',
    license = 'MIT',
    platforms = ['any'],
    include_package_data = True,
)