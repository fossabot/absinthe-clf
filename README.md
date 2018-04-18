# absinthe-clf [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
Absinthe Configurable Logic Framework

## Project Goals
This is the beginning of what will have to be a very large and complex project.  There are a lot of goals and where this is going to go is not well defined, so we'll see.  The following are some near-term goals:

- [x] Configure cross-platform Python local build environment (automation with doit).
- [ ] Configure travis-ci build.
- [ ] Configure document generation using readthedocs.
- [ ] Implement extensible RISC-V32i ALU as Python module to validate MyHDL toolchain (including tests).
- [ ] Develop configurable RISC-V soft core for FPGA implementation.

## Quick Start
This project requires Python 3 to be installed on the development workstation. It creates a Python3 virtual environment in the absinthe-clf project directory.  Needed modules are installed into that virtual environment.

To configure build environment:
```bash
git clone https://github.com/edwardgjohns3/absinthe-clf.git
cd absinthe-clf
```
To perform build:
```bash
python3 dodo.py
```
