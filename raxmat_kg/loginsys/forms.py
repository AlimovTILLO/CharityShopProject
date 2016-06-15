from django.contrib.auth.forms import UserChangeForm


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Since the pk is set this is not a new instance
            self.fields['username'] = self.instance.username
            self.fields['username'].widgets.attrs['readonly'] = True
