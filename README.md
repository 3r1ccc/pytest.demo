Running Tests
=============
run all tests: 
--------------
	py.test tests

run all tests except: 
---------------------
	py.test tests ?

run all tests with webtest mark:
--------------------------------
	py.test -v -m webtest

run a set of tests based on their names (has "answer" in them)
--------------------------------------------------------------
	py.test -v -k answer

run a set of tests based on their names (don't has the word "answer" in them)
-----------------------------------------------------------------------------
	py.test -v -k "not answer"

run a single module: 
--------------------
	py.test tests/sms/test_4.py

run a single test
------------------------------------------------------------
	py.test -q tests/clock/test_1.py::test_answer

run 2 tests in different module 
------------------------------------------------------------
	py.test tests/clock/test_1.py::test_answer tests/sms/test_5.py::test_create_file2

slip later test if previous test failed
------------------------------------------------------------
	py.test tests/simple/test_26.py

Fixture
=======
fixture
------------------------------------------------------------
	py.test tests/fixtures/test_32.py

fixture in conftest.py
------------------------------------------------------------
	py.test tests/fixtures/test_42.py

fixture in conftest.py with fin
------------------------------------------------------------
	py.test tests/fixtures/fin/test_41.py

fixture in conftest.py can accept a request
------------------------------------------------------------
	py.test tests/fixtures/request/test_22.py

fixture with session & autouse
------------------------------------------------------------
	py.test -s -v tests/clock/test_print.py

fixture with different parameters
------------------------------------------------------------
	py.test -s -v  tests/fixtures/parametrized/test_19.py

Running Order
=============
ordering 
------------------------------------------------------------
	pip install pytest-ordering
	py.test tests/order/test_45.py -vv
	


Commandline 
===========
run a test that requires commandline input
------------------------------------------------------------
	py.test tests/simple/test_22.py --cmdopt=type2

run tests according to commandline option & markers
------------------------------------------------------------
	py.test tests/simple/test_24.py --runslow --rungood
	py.test tests/simple/test_24.py --runslow 
	py.test tests/simple/test_24.py           --rungood
	py.test tests/simple/test_24.py

plugin: conftest.py can be in high level
------------------------------------------------------------
	py.test tests/simple/another --rungood --runslow


Information
===========
show marker information
------------------------------------------------------------
	py.test --markers

show all tests
------------------------------------------------------------
	py.test --collect-only


Log
===
Save resultlog
------------------------------------------------------------
	py.test -s -v tests/clock/test_print.py --resultlog=log.txt

Save html log
------------------------------------------------------------
	py.test -s -v tests/clock/test_print.py --html=tests/report.html

Plugin
======
Add this to setup.py
--------------------
	pip install pytest-ordering
	pip install pytest-variables
	pip install pytest-html
