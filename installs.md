sudo apt install python3.10-venv
python3 -m venv .venv
source .venv/bin/activate

optional: sudo rm -r fairpyx.egg-info/ (if there is exsist)

pip install -e .
cd tests/Tests\ for\ Optimization-based\ Mechanisms/
pip install pytest
python3 -m <file without the py>

optional: sudo rm -r .venv