from distutils.core import setup
setup(
  name='mimms',
  version='3.2',
  description='mimms is an mms (e.g. mms://) stream downloader',
  author='Wesley J. Landaker',
  author_email='wjl@icecavern.net.',
  license='GPLv3',
  url='http://savannah.nongnu.org/projects/mimms/',
  packages=['libmimms'],
  scripts=['mimms'],
  data_files=[
    ('share/man/man1', ['mimms.1'])
    ]
  )
