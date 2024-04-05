from django.http import HttpResponse
from django.shortcuts import render
from Values.models import values
from Products.models import product
from Innovations.models import innovation
from Events.models import events
from Testimonials.models import testimonila
from Gallery.models import gallery
from Team.models import team 
from Feedback.models import Feedback
from Contact.models import Contact
from gemini import gemini_farmer
import json
from django.http import JsonResponse



def Home(request):
    if request.method == "POST":
        chatbot_text = request.POST.get("chatbot_text")
        # Process user input and generate chatbot response
        chatbot_response = gemini_farmer.start_chat(chatbot_text)
        return JsonResponse({'chatbot_text': chatbot_response})
    else:
        # Handle GET request (render initial page)
        products_data = product.objects.all()
        values_data = values.objects.all()
        innovations_data = innovation.objects.all()
        events_data = events.objects.all()
        testimonilas_data = testimonila.objects.all()
        gallerys_data = gallery.objects.all()
        teams_data = team.objects.all()
        chatbot_text = None
        data = {
            "values_data": values_data,
            "products_data": products_data,
            "innovations_data": innovations_data,
            "events_data": events_data,
            "testimonilas_data": testimonilas_data,
            "gallerys_data": gallerys_data,
            "teams_data": teams_data,
            "chatbot_text": chatbot_text
        }
        return render(request, "index.html", data)


def save_feedback(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        date=request.POST.get("date")
        message=request.POST.get("message")
        fd=Feedback(name=name,email=email,phone=phone,date=date,message=message)
        fd.save()
    return render(request, "inner-page.html") 
def save_contact(request):
    if request.method=="POST":
        name=request.POST.get("contact_name")
        email=request.POST.get("contact_email")
        subject=request.POST.get("contact_subject")
       
        message=request.POST.get("contact_message")
        fd=Contact(name=name,email=email,subject=subject,message=message)
        fd.save()
    return render(request, "inner-page.html")

    
    
