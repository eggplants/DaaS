# DaaS

![test](https://github.com/rits-dajare/DaaS/workflows/test/badge.svg)
![code check](https://github.com/rits-dajare/DaaS/workflows/code%20check/badge.svg)
![deploy](https://github.com/rits-dajare/DaaS/workflows/deploy/badge.svg)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
![version 1.0](https://img.shields.io/badge/version-1.0-yellow.svg)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
[![Twitter](https://img.shields.io/badge/Twitter-%40rits_dajare-blue?style=flat-square&logo=twitter)](https://twitter.com/rits_dajare)

<div align="center">

![Ritsumeikan-Dajare-Circle logo](https://raw.githubusercontent.com/Ritsumeikan-Dajare-Circle/media/d72e2dbf8459689384af0de9e8b8d3e2d36a9cd2/logo/source.svg?sanitize=true)

</div>

## Description

This project's objective is to spread puns posted on RDC official slack's #ダジャレ channel through an official [Twitter account](https://twitter.com/rits_dajare).
Automatically determines whether a posted sentence is pun, and if true, gives a star with the rating engine.

## Requiremenst

- Python ~> 3.9
- Poetry

## Installation

```sh
pip install git+https://github.com/rits-dajare/DaaS
```

## Usage

### Run

```sh
daas --start
```

If you want to know the details of how to use this, run the following command.

```sh
daas --help
```

## Contributing

Bug reports and pull requests are welcome on GitHub at <https://github.com/rits-dajare/DaaS>.

You can setup development environment with:

```sh
git clone https://github.com/rits-dajare/DaaS
cd DaaS
poetry shell
poetry install && pre-comit install
```

## Refarence

- [Swagger UI](https://dajare.abelab.dev/docs)
- [ダジャレステーション](https://dajare.jp/) - used dajare data as teacher in this project.

## Author

- [Averak](https://github.com/averak)
- `abe12<at>mccc.jp`
