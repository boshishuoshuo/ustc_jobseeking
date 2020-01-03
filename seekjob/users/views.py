from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileRegisterForm,UserUpdateForm, ProfileUpdateForm
from django.db.models import Q
from .models import Profile
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        ur_form = UserRegisterForm(request.POST)
        # pr_form = ProfileRegisterForm(request.POST,
        #                               request.FILES,
        #                               instance=request.user.profile)
        if ur_form.is_valid(): #and pr_form.is_valid():
            ur_form.save()
            #pr_form.save()
            username = ur_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('profile')
    else:
        ur_form = UserRegisterForm()
        #pr_form = ProfileRegisterForm(instance=request.user.profile)

    # context = {
    #     'ur_form': ur_form,
    #     'pr_form': pr_form
    # }
    return render(request, 'users/register.html', {'ur_form':ur_form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

@login_required
def search_referrals(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(career_path__icontains=query)

            results = Profile.objects.filter(lookups)

            context = {
                'results': results,
                'submitbutton': submitbutton
            }

            return render(request, 'users/search_referrals.html', context)

        else:
            return render(request, 'users/search_referrals.html')

    else:
        return render(request, 'users/search_referrals.html')

@login_required
def search_candidates(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(career_path__icontains=query) & Q(employment_status__exact='1')

            results = Profile.objects.filter(lookups)

            context = {
                'results': results,
                'submitbutton': submitbutton
            }

            return render(request, 'users/search_candidates.html', context)

        else:
            return render(request, 'users/search_candidates.html')

    else:
        return render(request, 'users/search_candidates.html')