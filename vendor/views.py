from django.shortcuts import render,redirect

# Create your views here.

def vendor_message(request):
    return render(request, 'vendor/message.html')


def vendor_message_comp(request):
    return render(request, 'vendor/message-compose.html')

def vendor_dashboard(request):
    return render(request, 'vendor/vendor_dashboard.html')

def become_vendor(request):
    return render(request, 'vendor/how-it-works.html')


def vendor_dashboard_purchase(request):
    return render(request, 'vendor/vendor_dashboard-purchase.html')

def vendor_dashboard_statement(request):
    return render(request, 'vendor/vendor_dashboard-statement.html')

def vendor_edit_item(request):
    return render(request, 'vendor/vendor_edit_item.html')

def vendor_items(request):
    return render(request, 'vendor/vendor_items.html')

def vendor_uploads(request):
    return render(request, 'vendor/vendor_uploads.html')

def vendor_reviews(request):
    return render(request, 'vendor/vendor_reviews.html')

def vendor_withdrawal(request):
    return render(request, 'vendor/vendor_withdrawal.html')
