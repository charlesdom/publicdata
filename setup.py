from setuptools import setup
import sys
import os

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='publicdata',
    version='0.1.0',
    url='https://github.com/CivicKnowledge/publicdata',
    license='MIT',
    author='Eric Busboom',
    author_email='eric@busboom.org',
    description='Appurl And Rowgenerators for public datasets',
    packages=['publicdata'],
    zip_safe=True,
    install_requires=[
        'fs >= 2',
        'appurl',
        'rowgenerators',
        'pandas',
        'requests',
        'geoid'
        ],
    entry_points={
        'appurl.urls': [
            "censusreporter: = publicdata.censusreporter:CensusReporterURL",
            "censusreportergeo: = publicdata.censusreporter:CensusReporterShapeURL"
        ],
        'rowgenerators': [
            "CRJSON+ = publicdata.censusreporter:CensusReporterSource"

        ]

    },

)