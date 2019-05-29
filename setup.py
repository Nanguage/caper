import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='caper',
    version='v0.2.0.1',
    python_requires='>3.4.1',
    scripts=['bin/caper', 'mysql/run_mysql_server_docker.sh',
             'mysql/run_mysql_server_singularity.sh'],
    author='Jin Lee',
    author_email='leepc12@gmail.com',
    description='Cromwell Assisted Pipeline ExecutoR',
    long_description='https://github.com/ENCODE-DCC/caper',  #long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ENCODE-DCC/caper',
    packages=setuptools.find_packages(exclude=['mysql*', 'docs']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    install_requires=['pyhocon', 'requests']
)