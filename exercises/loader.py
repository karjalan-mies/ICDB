import csv

from exercises_db import db_session
from test_models import Company, Employee, Payment

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['company', 'city', 'address', 'phone_company', 'name', 'job',
                  'phone_person', 'email', 'date_of_birth', 'payment_date', 'ammount']
        reader = csv.DictReader(f, fields, delimiter=';')
        payments_data = []
        for row in reader:
            payments_data.append(row)
        return payments_data


def save_companies(data):
    processed = []
    unique_companies = []
    for row in data:
        if row['company'] not in processed:
            company = {'name': row['company'], 'city': row['city'],
                       'address': row['address'], 'phone': row['phone_company']}
            unique_companies.append(company)
            processed.append(company['name'])
            print(unique_companies)
    db_session.bulk_insert_mappings(Company, unique_companies, return_defaults=True)
    db_session.commit()
    return unique_companies


def get_company_by_id(companies, company_name):
   for company in companies:
       if company['name'] == company_name:
           return company['id']

def save_employees(data, companies):
    processed = []
    unique_emloyees = []
    for row in data:
        if row['phone_person'] not in processed:
            emploeyee = {'name': row['name'], 'job': row['job'], 'phone': row['phone_person'],
                         'email': row['email'], 'date_of_birth': row['date_of_birth'],
                         'company_id': get_company_by_id(companies, row['company'])}
            unique_emloyees.append(emploeyee)
            processed.append(emploeyee['phone'])
    db_session.bulk_insert_mappings(Employee, unique_emloyees, return_defaults=True)
    db_session.commit()
    return unique_emloyees


def get_employee_by_id(employees, employee_phone):
    for employee in employees:
        if employee['phone'] == employee_phone:
            return employee['id']


def save_payments(data, employees):
    payments = []
    for row in data:
        payment = {'payment_date': row['payment_date'], 'ammount': row['ammount'],
                   'employee_id': get_employee_by_id(employees, row['phone_person'])}
        payments.append(payment)
    db_session.bulk_insert_mappings(Payment, payments)
    db_session.commit()

if __name__ == '__main__':
    all_data = read_csv('salary.csv')
    companies = save_companies(all_data)
    employees = save_employees(all_data, companies)
    save_payments(all_data, employees)