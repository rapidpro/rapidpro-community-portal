from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from wagtail.wagtailadmin import messages
from wagtail.wagtailusers.views.users import change_user_perm

from accounts.forms import UserCreationForm, UserEditForm

User = get_user_model()


@permission_required(change_user_perm)
def create(request):
    """
    Custom View to allow for custom users with username as email. Mitigates:

    https://github.com/torchbox/wagtail/issues/158
    """
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, _("User '{0}' created.").format(user), buttons=[
                messages.button(reverse('wagtailusers_users_edit', args=(user.id,)), _('Edit'))
            ])
            return redirect('wagtailusers_users_index')
        else:
            messages.error(request, _("The user could not be created due to errors."))
    else:
        form = UserCreationForm()

    return render(request, 'wagtailusers/users/create.html', {
        'form': form,
    })


@permission_required(change_user_perm)
def edit(request, user_id):
    """
    Custom View to allow for custom users with username as email. Mitigates:

    https://github.com/torchbox/wagtail/issues/158
    """
    user = get_object_or_404(User, id=user_id)
    if request.POST:
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, _("User '{0}' updated.").format(user), buttons=[
                messages.button(reverse('wagtailusers_users_edit', args=(user.id,)), _('Edit'))
            ])
            return redirect('wagtailusers_users_index')
        else:
            messages.error(request, _("The user could not be saved due to errors."))
    else:
        form = UserEditForm(instance=user)

    return render(request, 'wagtailusers/users/edit.html', {
        'user': user,
        'form': form,
    })
