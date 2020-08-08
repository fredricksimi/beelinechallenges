from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.contrib import messages
from mainapp.models import Challenges
# Create your views here.
@login_required
def profile(request):
    user = request.user
    favourite_posts = Challenges.objects.all().filter(favourite=user)[:4]
    avatar_list = []
    avatar_name = request.user.username
    for ava in avatar_name:
        avatar_list.append(ava)
    
    avatar_holder = avatar_list[0]
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('userprofiles:profile')
        else:
            messages.warning(request, 'Please correct the errors shown.')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
    'p_form':p_form,
    "account_page":"active",
    'favourite_posts':favourite_posts,
    'avatar_holder':avatar_holder
    }
    return render(request, 'users/profile.html', context)
