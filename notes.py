    form = UserCreationForm()
    
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'accounts/register.html',context)