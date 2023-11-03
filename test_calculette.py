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
