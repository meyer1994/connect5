# connect-5
AI assignment for INE5430


### Status

|        | Build | Coverage|
|:------|:-----:|:-------:|
| master |[![Build Status](https://travis-ci.org/meyer1994/ai.svg?branch=master)](https://travis-ci.org/meyer1994/ai)|[![codecov](https://codecov.io/gh/meyer1994/ai/branch/master/graph/badge.svg)](https://codecov.io/gh/meyer1994/ai)
| dev    |[![Build Status](https://travis-ci.org/meyer1994/ai.svg?branch=dev)](https://travis-ci.org/meyer1994/ai)|[![codecov](https://codecov.io/gh/meyer1994/ai/branch/dev/graph/badge.svg)](https://codecov.io/gh/meyer1994/ai)

---

### Run

    python main.py

### Test

Install `coverage`:

    pip install -r requirements.txt
    coverage run -m unittest discover -vb tests
    coverage report -m

Or simply:

    python -m unittest discover -vb tests
