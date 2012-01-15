from distutils.core import setup

setup(
    name='django-sitepush',
    author='Yuri Prezument',
    author_email='y@yprez.com',
    version='0.1.0dev',
    packages=['sitepush'],
    license='ISC',
    url='http://github.com/yprez/django-sitepush',
    description='TODO',
    long_description=open('README.rst').read(),
    install_requires=[
        'Django >= 1.3',
        'fabric >= 1.3.3',
    ],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)