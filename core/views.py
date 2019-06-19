from django.shortcuts import render
from django.http import HttpResponse  
from pro1 import settings  
from django.core.mail import send_mail 
from reportlab.pdfgen import canvas  
from django.http import HttpResponse  
from .forms import EmpForm
      
def abc(request):
    return HttpResponse("welcome")     
def mail(request):  
    subject = "Greetings"  
    msg     = "Congratulations diksha you got a mail from priyanka"  
    to      = "sharmadiksha455@gmail.com"  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)  
def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello Django.")  
    p.showPage()  
    p.save()  
    return response  

def xyz(request):
    form = EmpForm(request.POST or None)
    if request.method == 'POST':
       
        if form.is_valid():
            return redirect('abc')
        else:
            form = EmpForm()
    return render(request,'index.html',{'form':form})
     