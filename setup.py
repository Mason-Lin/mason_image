from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mason_image',
    version='0.1.5',
    author='Mason Lin',
    author_email='pizza0117@gmail.com',
    description='mess up a image',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Mason-Lin/mason_image',
    packages=find_packages(),
    incude_package_data=True,
    install_requires=['Pillow>=5.1.0'],
    entry_points={
        'console_scripts': [
            'mason_image=mason_image:main'
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
