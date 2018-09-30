import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from .models import Repo, CreateRepo


class RepoType(DjangoObjectType):
    class Meta:
        model = Repo


class Query(graphene.ObjectType):
    repos = graphene.List(RepoType)

    @login_required
    def resolve_repos(self, info, **kwargs):
        return Repo.objects.all()

class Mutation(graphene.ObjectType):
    create_repo = CreateRepo.Field()