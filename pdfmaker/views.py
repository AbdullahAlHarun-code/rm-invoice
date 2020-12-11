from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
import os
import tempfile

# Create your views here.

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice3.html')
        context = {
            'invoice_id':12345,
            'customer_name':'Abdullah Al Harun',
            'today':'Today',
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice3.html',context)

        return HttpResponse(pdf, content_type='application/pdf')
        #return HttpResponse(html)
        # if pdf:
        #     response = HttpResponse(pdf, content_type='application/pdf')
        #     filename = "Invoice_%s.pdf" %("124578")
        #     content = "inline; filename='%s'" %(filename)
        #     print(filename)
        #     download = request.GET.get('download')
        #     if download:
        #         content = "attachment; filename='%s'" %(filename)
        #     response['Content-Disposition'] = content
        #     return html
        # return HttpResponse("Not found!")

class GenerateHtmlPdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice2.html')
        context = {
            'invoice_id':12345,
            'customer_name':'Abdullah Al Harun',
            'today':'Today',
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice2.html',context)
        printfile = tempfile.mktemp(".txt")
        open (printfile, "w").write("hello mammaa adsasd")
        os.startfile(printfile, "print")
        #return HttpResponse(pdf, content_type='application/pdf')
        return HttpResponse(html)
        # if pdf:
        #     response = HttpResponse(pdf, content_type='application/pdf')
        #     filename = "Invoice_%s.pdf" %("124578")
        #     content = "inline; filename='%s'" %(filename)
        #     print(filename)
        #     download = request.GET.get('download')
        #     if download:
        #         content = "attachment; filename='%s'" %(filename)
        #     response['Content-Disposition'] = content
        #     return html
        # return HttpResponse("Not found!")
