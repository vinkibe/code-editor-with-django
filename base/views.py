from django.shortcuts import render
import traceback
from django.http import JsonResponse
from .forms import CodeSnippetForm


def code_editor(request):
    form = CodeSnippetForm(request.POST or None)
    output = None
    if request.method == 'POST':
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                # Redirect stdout to capture output
                import sys
                from io import StringIO
                original_stdout = sys.stdout
                sys.stdout = StringIO()
                exec(code)
                output = sys.stdout.getvalue()
                # Restore stdout
                sys.stdout = original_stdout
            except Exception as e:
                output = f"Error: {e}<br>{traceback.format_exc()}"
            return JsonResponse({'output': output})
    return render(request, 'index.html', {'form': form})


def save_code(request):
    if request.method == 'POST':
        form = CodeSnippetForm(request.POST)
        if form.is_valid():
            code_snippet = form.save()  # Save the code snippet to the database
            return JsonResponse({'success': True, 'id': code_snippet.id})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        return JsonResponse({'success': False, 'errors': 'Invalid request method'})
    
