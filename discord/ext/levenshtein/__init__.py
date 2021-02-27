from collections import namedtuple

from discord.ext.levenshtein.hoge import Hoge

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')
version_info = VersionInfo(major=0, minor=1, micro=0, releaselevel='alpha', serial=0)

__version__ = '.'.join(map(str, [version_info.major, version_info.minor, version_info.micro]))
