from django.shortcuts import render, redirect

FOOTER = {
    'Created by Melissa',
    'Thank you for visiting the Django Market'
}

def index(request):
    context = {
        'footer': FOOTER
    }
    return render(request, "index.html", context)

def signup(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'register.html', context)

def register(request):
    if request.method == 'GET':
        return redirect('/register/')
    errors = User.object.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.errors(request, err)
        return redirect('/register/')
    else:
        newUser = User.objects.register(request.POST)
        request.session9['userId'] = newUser.index
        messages.success(request, "You have been registered")
        return redirect('/dashboard/')

def login(request):
    if request.method == 'GET':
        return redirect('/')
    if not User.objects.authenticate(request.POST['username'], request.POST['password']):
        messages.error(request, 'Invalid Username/Password')
        return redirect('/')
    user = User.objects.get(username=request.POST['username'])
    request.session['userId'] = user.id
    messages.success(request, "You have logged in")
    return redirect('/dashboard/')

def logout(request):
    request.session.clear()
    return redirect('/')

def dashboard(request):
    if 'userId' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['userId'])
    context = {
        'footer': FOOTER,
        'user': user
    }
    return render(request, 'dashboard.html', context)