class Parrot:

    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self, song):
        print('{} is singing {} song'.format(self.name,song))

    def dance(self):
        print('{} is now dancing'.format(self.name))


first = Parrot('Kuku',3)

print('{} is {} year old and he is {}'.format(first.name,first.age,first.species))

checkSing = raw_input('You want kuku to song(y/n)')
if checkSing is "y" or checkSing is "Y":
    songName = raw_input('Enter song name :')
    first.sing(songName)
else:
    print('kuku will not sing')
