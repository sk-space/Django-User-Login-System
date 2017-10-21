from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

# @login_required
def profile(request, pk):
    u = User.objects.get(pk = pk)
    return render(request, 'actor/profile.html', {'pk':u})

# @login_required
def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    user_form = UserProfileForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('website', 'bio', 'phone', 'city', 'country', 'organization'))
    formset = ProfileInlineFormset(instance=user)

    # if request.user.is_authenticated() and request.user.id == user.id:
    if request.method == "POST":
        user_form = UserProfileForm(request.POST, request.FILES, instance=user)
        formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

        if user_form.is_valid():
            created_user = user_form.save(commit=False)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

            if formset.is_valid():
                created_user.save()
                formset.save()
                return HttpResponseRedirect(reverse('profile:index', kwargs={'pk': pk, }))

    return render(request, "actor/profile_edit.html", {
        "noodle": pk,
        "noodle_form": user_form,
        "formset": formset,
    })
    # else:
    #     raise PermissionDenied
