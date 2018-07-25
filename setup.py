from setuptools import setup

setup(
    name = 'declutter',
    version = '0.1',
    packages = ['declutter'],
    entry_points = {
        'console_scripts': [
            'declutter = declutter.__main__:main'
        ]
    })