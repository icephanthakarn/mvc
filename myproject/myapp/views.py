from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Cow

def enter_cow_id_view(request):
    if request.method == 'POST':
        cow_id = request.POST.get('cow_id')
        try:
            cow = Cow.objects.get(cow_id=cow_id)
        except Cow.DoesNotExist:
            return HttpResponse("Cow not found.")
        return render(request, 'cow_details.html', {'cow': cow})
    
    return render(request, 'enter_cow_id.html')

def milk_cow_view(request, cow_id):
    cow = get_object_or_404(Cow, cow_id=cow_id)
    lemon = request.POST.get('lemon', False)
    result = cow.produce_milk(lemon)
    cow.save()
    return render(request, 'milk_result.html', {'result': result, 'cow': cow})


def reset_bsod_view(request):

    cows = Cow.objects.filter(is_bsod=True)
    for cow in cows:
        cow.is_bsod = False  
        cow.save() 

  
    return redirect('milk_report')  

def cow_report_view(request):
    cows = Cow.objects.all()
    return render(request, 'cow_report.html', {'cows': cows})



def cow_details_view(request):
    if request.method == 'POST':
        cow_id = request.POST.get('cow_id')
        cow = get_object_or_404(Cow, cow_id=cow_id)
        return render(request, 'cow_details.html', {'cow': cow})
    return render(request, 'enter_cow_id.html')


def list_cows_view(request):
    cows = Cow.objects.all()
    return render(request, 'list_cows.html', {'cows': cows})

def home_view(request):
    cows = Cow.objects.all() 

    query = request.GET.get('search', '')  
    if query:
        cows = Cow.objects.filter(cow_id__icontains=query) 
    else:
        cows = Cow.objects.all()  

    return render(request, 'home.html', {'cows': cows, 'query': query})

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

def reset_all_milk_view(request):
 
    cows = Cow.objects.all() 
    for cow in cows:
        cow.milk_bottles_produced = 0
        cow.plain_milk_bottles = 0
        cow.sour_milk_bottles = 0
        cow.chocolate_milk_bottles = 0
        cow.almond_milk_bottles = 0
        cow.soy_milk_bottles = 0
        cow.save()  

    return redirect('milk_report')  