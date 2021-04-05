from faker import Faker
fake = Faker('ru_RU')

def create_fio(gender):
    if gender == 'man':
        fio = fake.name_male().split()
    else:
        fio = fake.name_female().split()
    if len(fio) == 3:
        return fio
    else:
        print(fio)
        fio.pop(0)
        print(fio)

if __name__ == '__main__':
    for _ in range(100):
        create_fio('man')
