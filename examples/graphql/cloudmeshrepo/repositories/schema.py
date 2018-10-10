import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from .models import Repository, CreateRepository


class RepositoryType(DjangoObjectType):
    class Meta:
        model = Repository


class Query(graphene.ObjectType):
    repositories = graphene.List(RepositoryType)

    @login_required
    def resolve_repositories(self, info, **kwargs):
        return Repository.objects.all()

class Mutation(graphene.ObjectType):
    create_repository = CreateRepository.Field()