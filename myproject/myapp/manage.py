from models import Cow
import random

def create_cows():
    for i in range(5):
        cow_id = str(random.randint(1, 9)) + ''.join([str(random.randint(0, 9)) for _ in range(7)])
        Cow.objects.create(
            cow_id=cow_id,
            color='white',
            age_years=random.randint(0, 10),
            age_months=random.randint(0, 11)
        )
    
    for i in range(5):
        cow_id = str(random.randint(1, 9)) + ''.join([str(random.randint(0, 9)) for _ in range(7)])
        Cow.objects.create(
            cow_id=cow_id,
            color='brown',
            age_years=random.randint(0, 10),
            age_months=random.randint(0, 11)
        )
