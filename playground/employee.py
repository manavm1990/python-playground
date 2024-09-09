class Employee:
    def __init__(self, name: str, emp_id: int, monthly_salary: float) -> None:
        self.__name = name
        self.__emp_id = emp_id
        self.__salary = monthly_salary

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def emp_id(self) -> int:
        return self.__emp_id

    @emp_id.setter
    def emp_id(self, emp_id: int) -> None:
        self.__emp_id = emp_id

    @property
    def salary(self) -> float:
        return self.__salary

    def get_annual_salary(self) -> float:
        return self.__salary * 12

    def apply_raise(self, raise_amount: float) -> None:
        self.__salary += raise_amount
