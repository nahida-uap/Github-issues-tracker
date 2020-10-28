from django.core.paginator import Paginator

from django.shortcuts import render
from django.template.context import RequestContext

from .models import Issue

import requests
import json
import ast

def home(request):
    response = requests.get('https://api.github.com/repos/walmartlabs/thorax/issues')
    issues = response.json()

    for issue in issues:
        iss_id = issue['url'].split('/')[-1]
        iss = Issue(url=issue['url'], title=issue['title'], state=issue['state'], issue_id=iss_id, detail=issue)
        try:
            iss.save()
        except:
            pass

    issues = Issue.objects.all()
    paged_issues = Paginator(issues, 10)

    page_number = request.GET.get('page')
    page_obj = paged_issues.get_page(page_number)

    return render(request, "home.html", {'title': "List of Issues from: “WalmartLabs”",
                                         'page_obj': page_obj
                                         })


def details(request, issue_no):
    issue_details = Issue.objects.filter(issue_id=issue_no)
    attempts = 0

    while not issue_details and attempts < 4:
        attempts = attempts + 1
        response = requests.get('https://api.github.com/repos/walmartlabs/thorax/issues/' + str(issue_no))
        issue = response.json()

        if issue['message'] == 'Not Found':
            break
        iss_id = issue['url'].split('/')[-1]
        iss = Issue(url=issue['url'], title=issue['title'], state=issue['state'], issue_id=iss_id, detail=issue)
        try:
            iss.save()
            break
        except:
            pass

    issue_detail = Issue.objects.filter(issue_id=issue_no)

    for issued in issue_details:
        issue_data = ast.literal_eval(issued.detail)

    if issue_detail:
        return render(request, "detail.html", {'title': "Details of Issue No: " + str(issue_no),
                                               'issue' : issue_detail,
                                               'issue_data': issue_data
                                               })
    else:
        return render(request, "detail.html", {'title': "Issue not found!"})