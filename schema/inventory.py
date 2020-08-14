from models.inventory import Item
from graphene_django import DjangoObjectType
import graphene


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class Query(graphene.ObjectType):
    items = graphene.List(ItemType)
    items_filter_by_type = graphene.List(ItemType, _type=graphene.String(name="type"))
    items_filter_by_hostname = graphene.List(ItemType, hostname=graphene.String())
    items_filter_by_uuid = graphene.List(ItemType, uuid=graphene.String())

    @graphene.resolve_only_args
    def resolve_items(self):
        return Item.objects.all()

    @graphene.resolve_only_args
    def resolve_items_filter_by_type(self, **args):
        if args == {}:  # 如果没有参数就返回所有结果
            return Item.objects.all()
        else:
            return Item.objects.all().filter(type=args.get('_type'))

    @graphene.resolve_only_args
    def resolve_items_filter_by_hostname(self, **args):
        if args == {}:  # 如果没有参数就返回所有结果
            return Item.objects.all()
        else:
            return Item.objects.all().filter(hostname=args.get('hostname'))

    @graphene.resolve_only_args
    def resolve_items_filter_by_uuid(self, **args):
        if args == {}:  # 如果没有参数就返回所有结果
            return Item.objects.all()
        else:
            return Item.objects.all().filter(uuid=args.get('uuid'))

    # schema = graphene.Schema(query=Query)

