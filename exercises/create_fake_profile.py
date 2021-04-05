from faker import Faker
fake = Faker('ru_RU')

def create_fake_profiles(num_rows=10):
    fake_profiles = []
    for _ in range(num_rows):
        fake_profiles.append(fake.simple_profile())
    return fake_profiles

if __name__ == '__main__':
    print(create_fake_profiles())