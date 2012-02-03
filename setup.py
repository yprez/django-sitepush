from setuptools import setup, find_packages

setup(
    name='django-sitepush',
    author='Yuri Prezument',
    author_email='y@yprez.com',
    version='0.1dev1',
    packages=find_packages(),
    license='ISC',
    url='http://github.com/yprez/django-sitepush',
    description='Redeploy Django projects using management commands',
    long_description=open('README.rst').read(),
    install_requires=[
        'Django >= 1.3',
        'fabric >= 1.3.3',
    ],
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
