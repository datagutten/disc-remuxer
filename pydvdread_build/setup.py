import sys
from distutils.core import setup, Extension
import os

majv = 2
minv = 0

dvdread = Extension(
    '_dvdread',
    define_macros=[
        ('MAJOR_VERSION', str(majv)),
        ('MINOR_VERSION', str(minv))
    ],
    include_dirs=['libdvdread/include'],
    library_dirs=['libdvdread/lib/x64'],
    libraries=['dvdread'],
    sources=['src/dvdread.c'],
    # extra_compile_args=['-std=c11']
)

print('Include dirs', os.path.realpath(dvdread.include_dirs[0]))
print('Lib dirs', os.path.realpath(dvdread.library_dirs[0]))

setup(
    name='dvdread',
    version='%d.%d' % (majv, minv),
    description='Python wrapper for libdvdread',
    author='Colin ML Burnett',
    author_email='cmlburnett@gmail.com',
    url="https://github.com/cmlburnett/PyDvdRead",
    download_url="https://pypi.python.org/pypi/dvdread",
    packages=['dvdread'],
    ext_modules=[dvdread],
    requires=['crudexml'],
    classifiers=[
        'Programming Language :: Python :: 3.12'
    ]
)
