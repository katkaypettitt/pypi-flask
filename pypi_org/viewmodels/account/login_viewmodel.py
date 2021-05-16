from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase


class LoginViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()

    def validate(self):
        if not self.email or not self.email.strip():
            self.error = 'Must specify a email.'
        elif not self.password:
            self.error = 'Must specify a password.'
