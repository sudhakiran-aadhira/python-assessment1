class Employee:

    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        salary: float
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = salary

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"