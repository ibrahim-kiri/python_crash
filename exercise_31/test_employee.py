import pytest
from employees import Employee

@pytest.fixture
def employee():
    return Employee("Ibrahim", "Kiri", 50000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 55000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 60000