from django.shortcuts import render, redirect
from .models import RecordListItem
from django.http import HttpResponseRedirect
from .form import RecordForm


def baseView(request):
    return render(request, 'base.html', {})


def recordView(request):
    all_records_items = RecordListItem.objects.all()
    return render(request, 'viewrecords.html',
                  {'all_items': all_records_items})


def addRecordView(request):
    form = RecordForm()
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            user = form.save()
        return redirect('base')
    context = {'form': form}
    return render(request, 'addrecord.html', context)


def deleteRecordView(request, i):
    y = RecordListItem.objects.get(id=i)
    y.delete()
    all_records_items = RecordListItem.objects.all()
    return render(request, 'viewrecords.html',
                  {'all_items': all_records_items})
