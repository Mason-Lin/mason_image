# mason_image [![Version][version-badge]][version-link] ![MIT License][license-badge]
A small tool to mess up a image

`mason_image` is a small tool to mess up a image


### Demo

Before

![](https://raw.githubusercontent.com/Mason-Lin/mason_image/master/lenna_in.jpg)

After

![](https://raw.githubusercontent.com/Mason-Lin/mason_image/master/lenna_out.jpg)


### Usage

```
usage: mason_image [-h] [--in IN_IMAGE] [--out OUT_IMAGE]

optional arguments:
  -h, --help         show this help message and exit
  --in IN_IMAGE      path of image to mess up
  --out OUT_IMAGE    path of output image
```

### Install

```
$ pip install mason_image
```


### Pack it
```
pip3 install setuptools
pip3 install wheel

python3 setup.py sdist bdist_wheel
```


### Try to install locally
```
pip3 install dist/mason_image-0.1.2-py3-none-any.whl
```


### Upload to PyPI
```
pip3 install twine
twine upload dist/mason_image-0.1.2-py3-none-any.whl
```


### License

[MIT](https://github.com/Mason-Lin/mason_image/blob/master/LICENSE)

[version-badge]:   https://img.shields.io/badge/version-0.1.2-brightgreen.svg
[version-link]:    https://pypi.python.org/pypi/mason_image/
[license-badge]:   https://img.shields.io/github/license/Mason-Lin/mason_image.svg


