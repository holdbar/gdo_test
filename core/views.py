# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse

from core.models import Answer
from core.pdf_generator import generate_pdf

def index(request):
    answers = Answer.objects.get_answers_dict()
    generate_pdf(answers=answers)
    with open('form.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read())
        response['content_type'] = 'application/pdf'
        response['Content-Disposition'] = 'attachment;filename=form.pdf'
        return response
