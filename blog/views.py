from django.shortcuts import render

# Create your views here (the logic of our application).
# Views are functions that take a web request 
# and return a web response. 
# This response can be the HTML contents of a web page, 
# or a redirect, or a 404 error, or an XML document, 
# or an image, etc.
# The view itself contains whatever arbitrary logic 
# is necessary to return that response. 
# This code is in blog/views.py
# multiple steps to this bit, change views.py, then urls.py, then urls.py in the project folder!
def post_list(request):
    return render(request, 'blog/post_list.html', {})