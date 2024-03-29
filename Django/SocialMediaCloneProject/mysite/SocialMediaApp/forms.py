from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Create your forms here.
class UserCreateForm(UserCreationForm):
    class meta:
        model = get_user_model()
        fields = ('username','password1','password2','gmail')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['gmail'].label = 'Email Address'


