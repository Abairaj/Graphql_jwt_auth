import graphene
import graphql_jwt
from .import mutations


class JWTMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Mutation(JWTMutation, mutations.Mutation):
    pass


schema = graphene.Schema(mutation=Mutation)
