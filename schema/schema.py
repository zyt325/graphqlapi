import graphene
from schema import inventory


class Query(inventory.Query, graphene.ObjectType):
    pass


class Mutations(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
