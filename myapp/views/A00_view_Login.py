from django.shortcuts import render,redirect
from django.http import JsonResponse

from myapp.forms import LoginForm
from myapp.forms import LoginButton







from django.http import HttpResponse
import json
import logging
logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger = logging.getLogger("myapp")

def login_view(request):
    import os
    import ast

    if request.method == 'POST':
        logger.debug(f"Hello23")
        logger.info("This is an info message")

        return redirect('browse')

    else:


        loginForm = LoginForm()
        submitButton = LoginButton()



        #logger.debug(f"request.POST = {MainDfgForm(request.POST)}")
        #logger.debug(f"request.GET = {MainDfgForm(request.GET)}")
        return render(request, 'A00_Login.html', {
                                            'loginForm': loginForm,
                                            'submitButton': submitButton,

                                            }
                  )


