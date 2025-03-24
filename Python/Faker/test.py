from faker import Faker
import random

fake = Faker('zh_CN')

with open('id.txt', 'w', encoding='utf-8') as f:
    for _ in range(5):
        name = fake.name()
        gender = random.choice(['男', '女'])
        age = random.randint(18, 60)
        id_number = fake.ssn()
        phone_number = fake.phone_number()
        
        f.write(f'姓名: {name}\n性别: {gender}\n年龄: {age}\n身份证号码: {id_number}\n电话号码: {phone_number}\n-----------------\n')