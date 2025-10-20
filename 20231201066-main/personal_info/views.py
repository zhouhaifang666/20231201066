from django.shortcuts import render
from django.http import HttpResponse

def personal_info_view(request):
    """个人信息展示页面"""
    context = {
        'name': '周海方',
        'student_id': '20231201066',
        'class_name': '23医信'
    }
    return render(request, 'personal_info/index.html', context)
