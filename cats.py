from peewee import *

db = SqliteDatabase('cats.sqlite')

class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.color}, {self.age}'

db.connect()
db.create_tables([Cat])

Cat.delete().execute()

zoe = Cat(name='Zoe', color='Ginger', age=3)
zoe.save()

holly = Cat(name='Holly', color='Tabby', age=5)
holly.save()

#CREATE
fluffy = Cat(name='Fluffy', color='Black', age=1)
fluffy.save()

berry = Cat(name='Berry', color='Orange', age=5)
berry.save()

#READ
cats = Cat.select()
for cat in cats:
    print(cat)

# for cat in Cat.select():
#     print(cat)

list_of_cats = list(cats) #regular Python list

"""CRUD operations Create Read Update Delete"""

#UPDATE
fluffy.age = 2
fluffy.save()

print('After Fluffy age changed.')
cats = Cat.select()
for cat in cats:
    print(cat)

#Can update many rows if needed
rows_modified = Cat.update(age=6).where(Cat.name == 'Holly').execute()

print('After Holly age changed.')
cats = Cat.select()
for cat in cats:
    print(cat)

print(rows_modified)

buzz = Cat(name='Buzz', color='Gray', age=3)
buzz.save()

cats_who_are_3 = Cat.select().where(Cat.age == 3)
for cat in cats_who_are_3:
    print(cat, ' is three.')

cat_with_l_in_name = Cat.select().where(Cat.name % '*l*')
for cat in cat_with_l_in_name:
    print(cat, ' has l in name.')

#case insensitive search
cat_with_b_in_name = Cat.select().where(Cat.name.contains ('b'))
for cat in cat_with_b_in_name:
    print(cat, ' has b in name.')

#returns None if none
zoe_from_db = Cat.get_or_none(name='Zoe')
print(zoe_from_db)

#get or none is safer if you don't know the id exists; crashes if not exists
cat_1 = Cat.get_by_id(1)
print(cat_1)

cat_100 = Cat.get_or_none(id=100)
print(cat_100)

total = Cat.select().count()
print(total)

total_cats_who_are_3 = Cat.select().where(Cat.age == 3).count()
print(total_cats_who_are_3)

cats_by_name = Cat.select().order_by(Cat.name)
print(list(cats_by_name))

cats_by_age = Cat.select().order_by(Cat.age)
print(list(cats_by_age))

cats_by_age = Cat.select().order_by(Cat.age.desc())
print(list(cats_by_age))

cats_by_age = Cat.select().order_by(Cat.age.desc(), Cat.name)
print(list(cats_by_age))

first_3 = Cat.select().limit(3)
print(list(first_3))

first_3 = Cat.select().order_by(Cat.name).limit(3)
print(list(first_3))

#Delete
#Cat.delete().execute() #This deletes all records in the database
rows_deleted = Cat.delete().where(Cat.name == 'Holly').execute()
print(rows_deleted, list(Cat.select()))
