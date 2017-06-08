#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time

from django.http.response import Http404, HttpResponse
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def upload_image(request):
    if request.method == 'POST':
        callback = request.GET.get('CKEditorFuncNum')
        try:
            path = 'upload/' + time.strftime("%Y%m%d%H%M%S", time.localtime())
            f = request.FILES['upload']
            file_name = path + "_" + f.name
            des_origin_f = open(file_name, 'wb+')
            for chunk in f:
                des_origin_f.write(chunk)
            des_origin_f.close()
        except Exception as  e:
            print (e)
        res = r"<script>window.parent.CKEDITOR.tools.callFunction(" + callback + ", '/" + file_name + " ', ' ');</script>"
        return HttpResponse(res)
    else:
        raise Http404()