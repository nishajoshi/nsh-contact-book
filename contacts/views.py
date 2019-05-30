import csv
import io

from django.shortcuts import render
from django.shortcuts import redirect

from .forms import ContactForm
from .models import Contact, Friend


def upload(request):
    """Upload contacts for name."""
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.DictReader(
                io.StringIO(str(request.FILES['file'].read(), 'utf-8'))
            )
            names = reader.fieldnames
            if 'name' not in names or 'phone' not in names:
                form.add_error(
                    field='file',
                    error="Please add csv with name and phone header"
                )
            else:
                contact, _ = Contact.objects.get_or_create(
                    name=form.cleaned_data['name']
                )
                for row in reader:
                    if not row['name'] or not row['phone']:
                        continue
                    Friend.objects.get_or_create(
                        contact=contact,
                        name=row['name'],
                        phone=row['phone'],
                    )
            if not form.errors:
                return redirect(search)
                
    else:
        form = ContactForm()
    return render(request, 'upload.html', context={'form': form})


def search(request):
    """Search for contact."""
    params = {}
    contact = request.GET.get('contact')
    friend = request.GET.get('friend')
    if contact:
        params['contact__name'] = contact
    if friend:
        params['name'] = friend
    friends = None
    if params:
        friends = Friend.objects.filter(**params).all()
    return render(request, 'search.html', context={'friends': friends})


