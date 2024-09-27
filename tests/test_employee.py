# tests/test_employee.py
import pytest

from playground.classes.employee import Employee


@pytest.fixture
def employee():
    return Employee(name="Jane Doe", emp_id=5678, monthly_salary=6000.0)


def test_get_annual_salary(employee):
    assert employee.get_annual_salary() == 72000.00


def test_apply_raise(employee):
    employee.apply_raise(raise_amount=1000.0)
    assert employee.get_annual_salary() == 84000.00
