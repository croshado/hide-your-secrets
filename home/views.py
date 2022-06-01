from django.shortcuts import render , HttpResponse
import base64


# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def indexd(request):
    return render(request, 'indexd.html')
def cho(request):
    keyd=request.GET['key']
    dec = []
    msg=request.GET['Plain text']
    enc = base64.urlsafe_b64decode(msg).decode()
    for i in range(len(enc)):
        key_c = keyd[i % len(keyd)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
        print("dec:", dec)
    u="".join(dec)
    return render(request, 'decrypt.html' , {'he': u})
        


def chlo(request):
     key=request.GET['key']
     msg=request.GET['Plain text']
     enc = []
     for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        print("enc:", enc)
     i=base64.urlsafe_b64encode("".join(enc).encode()).decode()
     
   # msg=request.GET["Plain txt"]
     return render(request, 'encrypted.html' , {'here': i})
    
     

