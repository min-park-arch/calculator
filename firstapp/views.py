from django.shortcuts import render

def home (request):
  return render (request, "home.html")

def result (request):
  a = int(request.GET['num1'])
  b = int(request.GET['num2'])
  
  choice = request.GET['select']
  if (choice == '더하기'):
    calculation = a+b
  elif (choice == '빼기'):
    calculation = a-b
  elif (choice == '곱하기'):
    calculation = a*b
  elif (choice == '나누기'):
    if (b==0): 
      calculation = "divison by zero"
    else:
      calculation = a/b
      
  
  return render (request, "result.html", {'calculation':calculation})