


# Make Class
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return getattr(F'{self.name}', F'{self.description}')

    # def showItems(self):
    #     return F"{self.name} has {len(self.items)} items in it."

# Hold Items