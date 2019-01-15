"""
	wiki-link
	~~~~~~~~

	wiki-link is a web-scraping application to find minimum number 
	of links between two given wiki pages. 
    
    :copyright: (c) 2016 - 2018 by Tran Ly VU. All Rights Reserved.
    :license: Apache License 2.0.
"""
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name='wikilink',
	version="1.2.0",
	author='Tran Ly Vu',
	author_email='vutransingapore@gmail.com',
	description='A web-scraping application to find the minimum number of links between 2 given wiki pages',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/tranlyvu/wiki-link",
	packages=find_packages("wikilink"),
	package_dir={'':'wikilink'},
	license='Apache License 2.0',
	classifiers=[
		"Programming Language :: Python 3.6",
		"License :: OSI Approved :: Apache Software License ",
		"Operating System :: OS Independent",
		"Development Status :: 5 - Production/Stable",
		"Natural Language :: English",
		"Environment :: Console",
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering :: Artificial Intelligence',
	],
	keywords=["web-scraping", "Artificial Intelligence", "breadth first search", "Graph"],
	project_urls={
    'Source': 'https://github.com/tranlyvu/wiki-link',
    'Tracker': 'https://github.com/tranlyvu/wiki-link/issues',
	},
	install_requires=[
		'bs4',
		'SQLAlchemy',
		"requests"
		],
	python_requires="~=3.6"			
)