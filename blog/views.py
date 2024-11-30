from  django.shortcuts import render, redirect, get_object_or_404


from .models import Blog
from .forms import BlogForm

# Create your views here.


def blog_list(request):
    # all records in the db
    # rows : represent the object /columns
    blogs = Blog.objects.all()
    return render(request,'blog/blog_list.html',{'blogs':blogs})

def blog_apply(request):
    # cover validity
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/blog_form.html',{'form': form})

def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()  # Corrected line
        return redirect('blog_list')
    return render(request, 'blog/blog_confirm_delete.html', {'blog': blog})


def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)  # Corrected line
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_form.html', {'form': form})
