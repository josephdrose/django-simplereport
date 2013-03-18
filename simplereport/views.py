from django.shortcuts import get_object_or_404, render

from simplereport.models import Report

def index(request):
    return render(request, 'reports/index.html', {
        'reports':Report.objects.all().order_by('priority','name')
    })
    
def detail(request, report_id):
    report=get_object_or_404(Report, pk=report_id)
    header, results=report.get_results()
    
    r=render(request, ["reports/%s" % request.GET.get('template',''), 'reports/detail.html'], {
        'header':header,
        'results':results,
        'report':report,
        'back_link':'/admin/simplereports/report/',
    })
    
    if 'download' in request.GET:
        r['Content-Disposition'] = 'attachment; filename=report.csv'
    
    return r