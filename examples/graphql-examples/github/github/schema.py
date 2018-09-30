import graphene
import github.repos.schema

class Query(github.repos.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)