from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        # Por ahora solo mostramos mensaje (luego podemos guardar o enviar mail)
        messages.success(request, "Tu mensaje fue enviado correctamente . ¡Gracias por contactarnos!")
        return redirect("contacto:contacto")

    return render(request, "contacto/contacto.html")