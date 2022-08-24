from allauth.socialaccount.forms import SignupForm


class MyCustomSocialSignupForm(SignupForm):
    def save(self, request):
        user = super(MyCustomSocialSignupForm, self).save(request)
        user.is_active = True
        user.save()
        return user
