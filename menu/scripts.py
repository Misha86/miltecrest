from menu.models import Item, Category


def scrab(cls1, cls2=None):
    categories = cls1.objects.all()

    # for category in categories:
    i = cls2.objects.all()[0]
    return i


# if __name__ == '__main__':
t = scrab(Category, Item)
print(t.children.all())
