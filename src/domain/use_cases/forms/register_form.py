from typing import Type, Dict
from infra.repositories.interfaces import Forms as RepositoryInterface
from domain.use_cases.interfaces.forms.register_form import RegisterForm
from data.models import Forms


class RegisterForm(RegisterForm):
    """class to define Register Field"""

    def __init__(self, form_repository: Type[RepositoryInterface]):
        self.form_repository = form_repository

    def registry(
        self,
        owner_id: str,
        title: str,
        description: str,
        active: bool,
    ) -> Dict[bool, Forms]:

        response = None

        validate_entry = (
            isinstance(owner_id, str)
            and isinstance(title, str)
            and isinstance(description, str)
            and isinstance(active, bool)
        )

        if validate_entry:
            response = self.form_repository.insert_form(
                owner_id, title, description, active
            )

        return {"Success": "true", "Data": response}
