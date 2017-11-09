import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-google-authenticator',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3',
    description='A Django app adding Google Authenticator feature',
    url='https://github.com/gnosis/django-google-authenticator',
    author='Gnosis',
    author_email='giacomo.licari@gnosis.pm',
    keywords=['google', 'authenticator', '2fa', 'gnosis'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
