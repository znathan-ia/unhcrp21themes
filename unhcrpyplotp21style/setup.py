import atexit
import glob
import os
import shutil

import matplotlib
from setuptools import find_packages, setup
from setuptools.command.install import install

def install_styles():
    # Find all style files
    stylefiles = glob.glob('unhcrpyplop21tstyle/**/*.mplstyle', recursive=True)
    # Find stylelib directory (where the *.mplstyle files go)
    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)
    # Copy files over
    print("Installing styles into", mpl_stylelib_dir)
    for stylefile in stylefiles:
        print(os.path.basename(stylefile))
        shutil.copy(
            stylefile,
            os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))

class PostInstallMoveFile(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)

# Get description from README
with open("README.md", "r") as fh:
    long_description = fh.read()

setup( name='unhcrpyplop21tstyle',
       version='0.0.1',
       author='Zongo Sidkeita',
       author_email="zongoj@unhcr.org",
       description="Set matplotlib style following UNHCR's P21 Data Visualization Guidelines",
       long_description = long_description,
       long_description_content_type='text/markdown',
       license="MIT",
       keywords=[
        "matplotlib-style-sheets",
        "unhcr-plot-style",
        "matplotlib-styles",
        "python"
       ],
       url="https://github.com/znathan-ia/unhcrpyplop21tstyle",
       install_requires=['matplotlib', ],
        packages=find_packages(),
       include_package_data=True,
       cmdclass={'install': PostInstallMoveFile, },
)
