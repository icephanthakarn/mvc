from django.db import models
import random

from django.shortcuts import render

class Cow(models.Model):
    COLOR_CHOICES = [
        ('white', 'White'),
        ('brown', 'Brown')
    ]
    
    cow_id = models.CharField(max_length=8, unique=True)
    color = models.CharField(max_length=5, choices=COLOR_CHOICES)
    age_years = models.IntegerField()
    age_months = models.IntegerField()
    milk_bottles_produced = models.IntegerField(default=0)
    is_bsod = models.BooleanField(default=False)
    plain_milk_bottles = models.IntegerField(default=0)
    sour_milk_bottles = models.IntegerField(default=0)
    chocolate_milk_bottles = models.IntegerField(default=0)
    almond_milk_bottles = models.IntegerField(default=0)
    soy_milk_bottles = models.IntegerField(default=0)

    def __str__(self):
        return f'Cow {self.cow_id} - {self.color}'

    def produce_milk(self, lemon=False):
        if self.is_bsod:
            return "This cow is in BSOD state and cannot produce milk."


        if self.color == 'white':
            if lemon:
                self.sour_milk_bottles += 1
                self.milk_bottles_produced += 1
                self.save()
                return "Produced sour milk."
            else:
                # ตรวจสอบโอกาสในการผลิตนมถั่วเหลือง
                chance_of_soy_milk = 0.005 * self.age_months
                if random.random() < chance_of_soy_milk:
                    self.soy_milk_bottles += 1
                    self.is_bsod = True
                    self.save()
                    return "Produced soy milk (BSOD occurred)."
                else:
                    self.plain_milk_bottles += 1
                    self.milk_bottles_produced += 1
                    self.save()
                    return "Produced plain milk."

        elif self.color == 'brown':
            chance_of_almond_milk = 0.01 * self.age_years
            if random.random() < chance_of_almond_milk:
                self.almond_milk_bottles += 1
                self.is_bsod = True
                self.save()
                return "Produced almond milk (BSOD occurred)."
            else:
                self.chocolate_milk_bottles += 1
                self.milk_bottles_produced += 1
                self.save()
                return "Produced chocolate milk."
            


def create_cows():
    for _ in range(5):
        cow_id = f"{random.randint(1, 9)}{random.randint(1000000, 9999999)}"
        Cow.objects.create(
            cow_id=cow_id,
            color='white',
            age_years=random.randint(0, 10),
            age_months=random.randint(0, 11)
        )
    
    for _ in range(5):
        cow_id = f"{random.randint(1, 9)}{random.randint(1000000, 9999999)}"
        Cow.objects.create(
            cow_id=cow_id,
            color='brown',
            age_years=random.randint(0, 10),
            age_months=random.randint(0, 11)
        )

def milk_report_view(request):
    cows = Cow.objects.all()
    
    total_plain_milk = sum([cow.plain_milk_bottles for cow in cows])
    total_sour_milk = sum([cow.sour_milk_bottles for cow in cows])
    total_chocolate_milk = sum([cow.chocolate_milk_bottles for cow in cows])
    total_almond_milk = sum([cow.almond_milk_bottles for cow in cows])
    total_soy_milk = sum([cow.soy_milk_bottles for cow in cows])
    
    total_milk = total_plain_milk + total_sour_milk + total_chocolate_milk

    return render(request, 'milk_report.html', {
        'cows': cows,
        'total_plain_milk': total_plain_milk,
        'total_sour_milk': total_sour_milk,
        'total_chocolate_milk': total_chocolate_milk,
        'total_almond_milk': total_almond_milk,
        'total_soy_milk': total_soy_milk,
        'total_milk': total_milk
    })