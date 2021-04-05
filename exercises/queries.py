from exercises_db import db_session
from test_models import Company, Employee
import time

def employees_by_company(company_name):
    company = Company.query.filter(Company.name == company_name).first()
    employee_list = []
    if company:
        for emploee in Employee.query.filter(Employee.company_id == company.id):
            employee_list.append(f'{company.name} - {emploee.name}')
        return employee_list


def employees_by_company_joined(company_name):
    query = db_session.query(Employee, Company).join(
        Company, Employee.company_id == Company.id
    ).filter(Company.name == company_name)
    company = Company.query.filter(Company.name == company_name).first()
    employee_list = []
    for employee, company in query:
        employee_list.append(f'{company.name} - {employee.name}')
    return employee_list


def employees_by_company_relation(company_name):
    company = Company.query.filter(Company.name == company_name).first()
    employee_list = []
    if company:
        for emploee in company.employees:
            employee_list.append(f'{company.name} - {emploee.name}')
        return employee_list


if __name__ == '__main__':
#    start_time = time.perf_counter()
#    for _ in range(10000):
#        employees_by_company('Самсунг Электроникс Рус Калуга (Samsung)')
#    print(f'employees_by_company: {time.perf_counter() - start_time}')
#    print(employees_by_company_joined('Самсунг Электроникс Рус Калуга (Samsung)'))

#    start_time = time.perf_counter()
#    for _ in range(100):
#        employees_by_company_joined('Самсунг Электроникс Рус Калуга (Samsung)')
#    print(f'employees_by_company_joined: {time.perf_counter() - start_time}')

    start_time = time.perf_counter()
    for _ in range(100):
        employees_by_company_relation('Самсунг Электроникс Рус Калуга (Samsung)')
    print(f'employees_by_company_relation: {time.perf_counter() - start_time}')