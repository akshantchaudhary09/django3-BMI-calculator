from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'bmi/home.html')

def calculator(request):
    height = float(request.GET.get('height'))
    weight = float(request.GET.get('weight'))
    bmi = round(weight/(height*height), 2)
    if bmi < 18.5:
        condition = 'Underweight'
        s1 = 'Eat more often'
        s2 = 'Drink Milk'
        s3 = 'Try Weight gainer shakes'
        s4 = 'Use Bigger Plates'
        s5 = 'Add cream to your coffee'
    if (bmi > 18.5) and (bmi < 24.9):
        condition = 'Normal'
        s1 = 'Eat healthy food'
        s2 = 'Do not eat junk food'
        s3 = 'Your meal should contain all the essential nutrients'
        s4 = 'Minimize the intake of alcohol'
        s5 = 'Do regular exercise'
    if bmi > 25:
        condition = 'Overweight'
        s1 = 'Eat Whole grains (whole wheat, steel cut oats, brown rice, quinoa)'
        s2 = 'Eat Vegetables (a colorful variety-not potatoes)'
        s3 = 'Eat Whole fruits (not fruit juices)'
        s4 = 'Eat Nuts, seeds, beans, and other healthful sources of protein (fish and poultry)'
        s5 = 'Eat Plant oils (olive and other vegetable oils)'
    return render(request, 'bmi/calculator.html', {'bmi':bmi, 'condition':condition,
           's1':s1, 's2':s2, 's3':s3, 's4':s4, 's5':s5})







