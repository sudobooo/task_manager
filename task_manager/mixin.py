from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class HandleNoPermissionMixin(AccessMixin):
    no_permission_url = ''
    error_message = ''
    request = ''

    def handle_no_permission(self):
        messages.error(self.request, self.error_message)
        return redirect(self.no_permission_url)
