import re
import setuptools

with open('discord/ext/levenshtein/__init__.py') as f:
    VERSION_MATCH = re.search(
        r'VersionInfo\(major=(\d+)?,\s*?minor=(\d+)?,\s*?micro=(\d+)?, .*',
        f.read(),
        re.MULTILINE
    )
if not VERSION_MATCH:
    raise RuntimeError('VersionInfo not found')

VERSION = '.'.join([VERSION_MATCH.group(i) for i in range(1, 4)])

with open('README.rst') as f:
    LONG_DESCRIPTION = f.read()

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: Implementation :: CPython',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

REQUIRES = [
    'discord.py',
    'python-Levenshtein',
]

EXTRA_REQUIRES = {
    'docs': [
        'sphinx',
        'sphinxcontrib_trio',
        'sphinxcontrib-websupport',
        'sphinx-rtd-theme',
    ],
}

PROJECT_URLS = {
    'Documentation': 'https://discord-ext-levenshtein.readthedocs.io/en/latest/',
    'Source': 'https://github.com/shirataki2/discord-ext-levenshtein',
    'Tracker': 'https://github.com/Shirataki2/discord-ext-levenshtein/issues',
}

setuptools.setup(
    name='discord-ext-levenshtein',
    author='Shirataki2',
    author_email='tmy1997530@gmail.com',
    classifiers=CLASSIFIERS,
    description='A discord.py extension for command name suggestion',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    extras_require=EXTRA_REQUIRES,
    install_requires=REQUIRES,
    license='MIT',
    packages=['discord.ext.levenshtein'],
    project_urls=PROJECT_URLS,
    python_requires='>=3.6.0',
    url='https://github.com/shirataki2/discord-ext-levenshtein',
    version=VERSION,
)
