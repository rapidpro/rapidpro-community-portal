import factory
import factory.fuzzy

from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    password = factory.fuzzy.FuzzyText()
    username = factory.Sequence(lambda n: 'user-%d@example.com' % n)
    first_name = factory.fuzzy.FuzzyText()
    last_name = factory.fuzzy.FuzzyText()

    @classmethod
    def _create(cls, target_class, **kwargs):
        """
        Use create_user, which performs some validation and normalizes
        the user's username (email address).
        """
        manager = cls._get_manager(target_class)
        username = kwargs.pop('username')
        password = kwargs.pop('password')
        user = manager.create_user(username, password)
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save(update_fields=kwargs.keys())
        return user
