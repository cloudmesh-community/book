import graphene
from graphene_django.types import DjangoObjectType
from github.repos.models import Repo#, Owner

class RepoType(DjangoObjectType):
    class Meta:
        model = Repo

# class OwnerType(DjangoObjectType):
#     class Meta:
#         model = Owner

class Query(graphene.AbstractType):
    all_repos = graphene.List(RepoType)
    # all_owners = graphene.List(OwnerType)

    def resolve_all_repos(self, info, **kwargs):
        return Repo.objects.all()

    # def resolve_all_owners(self, info, **kwargs):
    #     return Owner.objects.all()