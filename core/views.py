# views.py (core/views.py)
# --------------------------
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Preguntas recientes
@login_required
def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'questions': questions})

# Ver una pregunta
@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        Answer.objects.create(
            question=question,
            body=request.POST["body"],
            author=request.user
        )
        return redirect("question_detail", question_id=question.id)
    return render(request, "question_detail.html", {"question": question})

# Hacer pregunta
@login_required
def ask_question(request):
    if request.method == "POST":
        Question.objects.create(
            title=request.POST["title"],
            body=request.POST["body"],
            author=request.user
        )
        return redirect("home")
    return render(request, "ask_question.html")

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
