from django.shortcuts import render

def inicio(request):
	context={'nombre':'todo lo que queremos pasarle a la vista','apellido':'probando'}
	return render(request,"inicio.html",context)