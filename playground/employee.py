class Employee:
    def __init__(self, name: str, emp_id: int, monthly_salary: float) -> None:
        self.name = name
        self.emp_id = emp_id
        self.salary = monthly_salary

    def get_annual_salary(self) -> float:
        return self.salary * 12

    def apply_raise(self, raise_amount: float) -> None:
        self.salary += raise_amount
