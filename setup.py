from setuptools import setup

with open('README.md', encoding='utf-8') as f:
	  long_description = f.read()

setup(
	name='iso-container',
	version='1.0.0',
	long_description=long_description,
	long_description_content_type = 'text/markdown',
	description='A Python package for ISO 6346 container information and validation.',
	author='Jiseoup',
	author_email='jseoup@gmail.com',
	url='https://github.com/Jiseoup/container-iso',
	license='MIT',
	python_requires='>=3.7',
	install_requires=[],
	packages=['iso_container'],
	package_data={'': ['datasets.json']},
	keywords=['container', 'iso container', 'container validate', 'iso', 'iso6346'],
	classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ]
)
