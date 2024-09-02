from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import IncomeForm
from .models import TotalValue, Expenses, Income
from register.views import register
# Create your views here.

def main(request):
    if request.user.is_authenticated:
        income_form = IncomeForm()
        total_money, created = TotalValue.objects.get_or_create(user = request.user)
        expenses = Expenses.objects.all()
        income = total_money.income_set.all()
        if total_money.total <= 0 and request.method == 'POST' and request.POST.get('submit'):
                income_form = IncomeForm(request.POST)
                if income_form.is_valid():
                    income_data = income_form.cleaned_data['income']
                    total_money.total += int(income_data)
                    total_money.save()
                    print(total_money.total)
                    if request.POST.get('logout') == 'logged out':
                        print('logout')
                        return HttpResponseRedirect('logout/')
                    return render(request, 'main/expense.html', {})
        elif total_money.total > 0:
            if request.method == 'POST':
                if request.POST.get('calculate') == 'clicked':
                    expense_cause = request.POST.get('cause')
                    expense_amount = request.POST.get('amount')
                    if int(expense_amount) <= 0:
                        pass
                    elif int(expense_amount) > 0 and expense_cause != 'None':
                        subtract = total_money.total - int(expense_amount)
                        total_money.total= subtract
                        total_money.save()
                        expense_db = Expenses(name = expense_cause, amount = int(expense_amount))
                        expense_db.save()
                        print('saved...')
                    else:
                        return HttpResponse('<h1>Something went wrong!</h1>')
                elif request.POST.get('add') == 'added':
                    addincome_cause = request.POST.get('incause')
                    addincome_amount = request.POST.get('inamount')
                    if int(addincome_amount) <= 0:
                        pass
                    elif int(addincome_amount) > 0 and addincome_cause != 'None':
                        add = total_money.total + int(addincome_amount)
                        total_money.total = int(add)
                        total_money.income_set.create(name = addincome_cause, amount = int(addincome_amount))
                        total_money.save()
                        print('added...')

                elif request.POST.get('logout') == 'logged out':
                    print('log')
                    return HttpResponseRedirect('/logout')

                else:
                    print('Error')

            return render(request, 'main/expense.html', {'tm':total_money, 'expenses':expenses, 'inc':income})
        return render(request, 'main/index.html', {'form':income_form, 'tm':total_money})

    else:
        print('Error found')
        return redirect(register)