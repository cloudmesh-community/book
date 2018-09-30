import graphene
from django.db import models

# Create your models here.

class Repo(models.Model):
    url = models.URLField()
    name = models.TextField(blank=False)
    full_name = models.TextField(blank=False)
    description = models.TextField(blank=True)


class CreateRepo(graphene.Mutation):
    url = graphene.String()
    name = graphene.String()
    full_name = graphene.String()
    description = graphene.String()

    class Arguments:
        url = graphene.String()
        name = graphene.String()
        full_name = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, name, full_name, description):
        repo = Repo(url=url, name=name, full_name=full_name, description=description)
        repo.save()

        return CreateRepo(url=repo.url, name=repo.name, full_name=repo.full_name, description=repo.description)



