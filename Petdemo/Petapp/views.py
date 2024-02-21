from django.shortcuts import render,redirect
from .models import Pet,Cart
from django.db.models import Q

# Create your views here.
def index(req):
    data= Pet.objects.all()
    context ={'data':data}
    return render(req,"index.html",context)

def details(req,pid):
    pets= Pet.objects.get(id=pid)
    context = {'pets': pets}
    return render(req,"details.html",context)

def cart(req):
    allPets = Cart.objects.all()
    context={}
    context['cart_items']= allPets
    total_price=0
    allpets = Cart.objects.all()
    for x in allpets:
        total_price += (x.pet.price * x.quantity)
        print(total_price)
    context['total'] = total_price
    length = len(allpets)
    context['items']= length
    return render(req,"cart.html",context)

def add_cart(req,pid):
    pets= Pet.objects.get(id=pid)
    print(pets)
    cart_item,created=Cart.objects.get_or_create(pet=pets)
    print(cart_item,created)
    if not created:
        cart_item.quantity +=1
    else:
        cart_item.quantity =1
    cart_item.save()
    

    return redirect("/cart")

def delete(req,pid):
    print("ID to be deleted",pid)
    #return HttpResponse("ID to be deleted" + rid)
    m= Cart.objects.filter(id=pid)
    m.delete()
    return redirect("/cart")

def search(req):
    query = req.POST['q']
    print(f"recieved Query is {query}")
    if not query:
        result = Pet.objects.all()
    else:
        result = Pet.objects.filter(
            Q(name__icontains = query)|
            Q(category__icontains = query)|
            Q(price__icontains = query)
        )
    return render(req,'index.html',{'results':result,'query':query})


def range(req):
    if req.method == "GET":
        return redirect("/")
    else:
        r1 = req.POST.get("min")
        r2 = req.POST.get("max")
        print(r1,r2)
        if r1 is not None and r2 is not None:
            queryset = Pet.prod.get_price_range(r1,r2)
            context={'data':queryset}
            return render(req,'index.html',context)
        else:
            queryset = Pet.objects.all()
            context = {'data': queryset}
            return render (req,"index.html",context)

def catList(req):
    queryset=Pet.prod.cat_list()
    context={'data':queryset}
    return render(req,"index.html",context)  

def dogList(req):
    queryset=Pet.prod.dog_list()
    context={'data':queryset}
    return render(req,"index.html",context)

def fishList(req):
    queryset=Pet.prod.fish_list()
    context={'data':queryset}
    return render(req,"index.html",context)

def birdList(req):
    queryset=Pet.prod.bird_list()
    context={'data':queryset}
    return render(req,"index.html",context)

def tortoiseList(req):
    queryset=Pet.prod.tortoise_list()
    context={'data':queryset}
    return render(req,"index.html",context)