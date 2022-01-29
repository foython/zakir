from django.shortcuts import render


# Create your views here.
def zakatcalculat(request):
  if request.method == 'POST':
    currency = request.POST.get('currency')
    base = request.POST.get('base').lower
    gold = request.POST.get('gold', 0)
    silver = request.POST.get('silver', 0)
    cash = request.POST.get('cash', 0)
    bank_diposit = request.POST.get('diposit', 0)
    given_loan = request.POST.get('gloan', 0)
    investments = request.POST.get('investments', 0)
    stock = request.POST.get('stock', 0)
    liabilities = request.POST.get('liabilities', 0)

    nisab = 0
    if base == 'vori':
      nisab = 7.5 #minimum amount
    else:
      nisab = 87.48 #minimum amount