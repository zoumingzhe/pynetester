rd/s/q ".\build"
rd/s/q ".\dist"
rd/s/q ".\pynetester.egg-info"

python setup.py check
python setup.py sdist
python setup.py bdist_wheel --universal
pause