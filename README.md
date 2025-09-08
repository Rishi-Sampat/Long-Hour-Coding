I built a Python package signal_ICT_RishiSampat_169 for basic Signals and Systems. It mainly uses Python, NumPy, and Matplotlib.

What the code does

Generates unit step, unit impulse, and ramp signals (returns NumPy arrays and plots them).

Generates sine, cosine, and exponential signals with amplitude, frequency, phase, and time as inputs.

Performs operations like time shifting, time scaling, signal addition, and multiplication.

The main.py file demonstrates:

Step and impulse of length 20

Sine wave (amplitude=2, frequency=5 Hz, phase=0, time=0 to 1 sec)

Shifting sine wave by +5

Adding step and ramp

Multiplying sine and cosine

Folder structure

signal_ICT_RishiSampat_169/

init.py

unitary_signals.py

trigonometric_signals.py

operations.py

main.py

dist/ (wheel and source distribution)

setup.cfg, pyproject.toml, LICENSE.md, README.md, egg-info

How the package was built and tested

First, installed build and twine

python -m pip install -U build twine


Built the package (wheel and tar.gz go to dist/)

python -m build


Uploaded to TestPyPI

twine upload --repository testpypi dist/*


Installed back from TestPyPI to check

pip install --index-url https://test.pypi.org/simple/ --no-deps signal-ICT-RishiSampat-169


Running the demo

python main.py


This shows all the signals and operations through plots.