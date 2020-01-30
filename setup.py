import setuptools
from distutils.core import setup
setup(
    name='mason_image',
    version='0.1.0',
    description='mess up a image',
    author='Mason Lin',
    author_email='pizza0117@gmail.com',
    url='https://github.com/Mason-Lin',
    packages=setuptools.find_packages(),
    install_requires=['Pillow>=5.1.0', 'numpy==1.14.4'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'mason_image=mason_image:main'
        ],
    },
)
