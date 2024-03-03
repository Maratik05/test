from django.shortcuts import render

class Product(View):
    def get(self,request,):
        
        return render(request,'index.html')
