import graphene
from django.db import models

# Create your models here.

class Repository(models.Model):
    url = models.URLField()
    name = models.TextField(blank=False)
    full_name = models.TextField(blank=False)
    description = models.TextField(blank=True)


class CreateRepository(graphene.Mutation):
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
        repository = Repository(url=url, name=name, full_name=full_name, description=description)
        repository.save()

        return CreateRepository(url=repository.url, name=repository.name, full_name=repository.full_name, description=repository.description)



