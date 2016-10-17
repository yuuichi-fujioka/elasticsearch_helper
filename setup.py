import setuptools


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


with open('README.rst') as f:
    description = f.read()


setuptools.setup(
    name='elasticsearch_helper',
    version='0.1',
    description=description,
    url='http://github.com/yuuichi-fujioka/setuptools_elasticsearch_helper.git',  # noqa
    author='Yuuichi Fujioka',
    author_email='fujioka.yuuichi@gmail.com',
    entry_points={
    },
    classifiers=[
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=['elasticsearch_helper'],
    install_requires=requirements
)
