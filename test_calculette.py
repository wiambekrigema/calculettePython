import pytest
from main import *

# test unitaire
def test_div():
	assert divide(1,2) == 0.5

def test_raise():
	with pytest.raises(Error):
		divide(1,0)
def test_multi():
	assert multiply(3,5) == 15
def test_sum():
	assert sum(4,9) == 13
def test_soustr():
    assert soustr(2,1) == 1
