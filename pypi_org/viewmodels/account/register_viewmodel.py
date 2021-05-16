from pypi_org.services import user_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.name = self.request_dict.name
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()

    def validate(self):
        if not self.name or not self.name.strip():
            self.error = 'Must specify a name.'
        elif not self.email or not self.email.strip():
            self.error = 'Must specify an email.'
        elif not self.password:
            self.error = 'Must specify a password.'
        elif len(self.password.strip()) < 5:
            self.error = 'Password must be at least 5 characters long.'
        elif user_service.find_user_by_email(self.email):
            self.error = 'User with that email address already exists.'
