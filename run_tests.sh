python -m pip install --upgrade pip
pip install tox
pip install pytest 
tox -e py -- --junitxml=test-reports/report.xml