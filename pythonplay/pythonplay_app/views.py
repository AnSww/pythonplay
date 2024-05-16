from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic



class HomePageView(TemplateView):
    template_name = 'home.html'

class LetsgoPageView(TemplateView):
    template_name = 'letsgo.html'


class LoginPageView(TemplateView):
    template_name = 'login.html'


@login_required
def roadmapPageView(request):
    template_name = 'roadmap.html'

    return render(request, template_name,)


def create_level_view(level_number):
    class_name = f"Level_{level_number}_View"
    template_name = f"level{level_number}.html"

    # Создание класса динамически с помощью type()
    dynamic_class = type(
        class_name,
        (TemplateView,),
        {'template_name': template_name}
    )

    return dynamic_class

Level_0_View = create_level_view(0)
Level_1_View = create_level_view(1)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess


@csrf_exempt
def run_code(request):
    if request.method == 'POST':
        try:
            code = request.POST.get('code', '')
            language = request.POST.get('language', '')

            if language == 'python':
                input_data = request.POST.get('input', '')  # Get input data
                result = run_python_code(code, input_data)
            else:
                result = "Language not supported for execution."

            return JsonResponse({'result': result})

        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method'})



def run_python_code(code, input_data):
    try:
        # Use Popen to pass input to subprocess
        process = subprocess.Popen(['python3', '-c', code], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=input_data, timeout=5)

        if stderr:
            return stderr
        else:
            return stdout
    except subprocess.TimeoutExpired:
        return "Error: Process timed out."
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"
