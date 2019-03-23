import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()
VERSION="0.3.11"    

setuptools.setup(
    name="dbdreader",
    version=VERSION,
    author="Lucas Merckelbach",
    author_email="lucas.merckelbach@hzg.de",
    description="A python module to access binary data files generated by Teledyne WebbResearch gliders",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://dockserver0.hzg.de/software/dbdreader/index.html',
    packages=setuptools.find_packages(),
    py_modules=['dbdreader'],
    entry_points = {'console_scripts':[],
                    'gui_scripts':[]
    },
    scripts = ['dbdrename.py','cac_gen.py'],
    install_requires = 'numpy'.split(),
    ext_modules = [
           setuptools.Extension("_dbdreader",
                                ["extension/py_dbdreader.c","extension/dbdreader.c"],
                                include_dirs=['extension/include'])
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: POSIX",
    ],
)