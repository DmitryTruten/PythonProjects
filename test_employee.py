import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for class Employee"""

    def setUp(self):
        """Create exemplar of employee
        for testing method"""
        self.my_employee = Employee('dima', 'truten', 0)
        self.employee_check = ['dima', 'truten', 0]

    def test_give_default_raise(self):
        self.my_employee.show_employee_info()

if __name__ == '__main__':
    unittest.main()
