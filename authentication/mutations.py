import graphene
from graphene_django.types import DjangoObjectType

from .models import CustomUser


class UserInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    password = graphene.String(required=True)


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email")


class CreateUserMutation(graphene.Mutation):
    class Arguments:
        input_data = UserInput(required=True)

    user = graphene.Field(UserType)
    
    def mutate(self, info, input_data):
        user = CustomUser.objects.create_user(
            email=input_data.email,
            username=input_data.username,
            password=input_data.password
        )
        return CreateUserMutation(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()


class Query(graphene.ObjectType):
    pass
