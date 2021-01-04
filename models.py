from tortoise import Model,fields

class Users(Model):
    id=fields.IntField(pk=True)
    name=fields.CharField(30)

    def __str__(self):
        return f'User {self.id}: {self.name}'