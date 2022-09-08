from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .forms import ProfileImageForm
from .models import ProfileImage
# Create your views here.

class ProcessImageView(TemplateView):
    template_name: str = "processimages/image_form.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["form"] = ProfileImageForm()
        return context


    def post(self, request,**kwargs):
        form = ProfileImageForm(request.POST, request.FILES)
        print("\n", request.FILES, "\n")
        if form.is_valid():
            img = form.save()
            messages.add_message(request, messages.SUCCESS, "Image Uploaded")
            return redirect(to="process_image")
        messages.add_message(request, messages.ERROR, message="Something went wrong")
        return render(request, self.template_name,  {"form": form})



class ImageListView(ListView):
    template_name = "processimages/image_list.html"
    context_object_name = "images"
    model = ProfileImage