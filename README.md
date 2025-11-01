# BSTT
An application written in Micropython for the Raspberry Pico, which controls a step-down converter.

## Dependencies
- mpremote
- mpy-cross
``` bash
pip install mpremote mpy-cross
```
You must use a compatible version of mpy-cross for your MicroPython firmware (major version must match).
``` bash
mpy-cross --version
```
## Deploy Process
From your command line:
```bash
# Clone this repository
$ git clone https://github.com/MarklPlz/BSTT.git

# Go into the repository
$ cd BSTT

# Build and deploy
$ python deploy.py
```
