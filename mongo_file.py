from IPython.display import Image

from mongoengine import connect,Document,fields
#connect and creat db
connect(db="mongodb" , host="localhost", port=27017)

#creat a user class


class User(Document):

    meta = {"collections": "my_user"}
    username = fields.StringField(required=True)
    profile_image=fields.ImageField(thumbnail_size=(150, 150, False))


db_name = User(username='dummy')
my_image = open('static/uploads/test/arslan.jpg' , 'rb')
db_name.profile_image.replace(my_image, filename="dummy.jpg")
db_name.save()

user = User.objects(username="dummy").first()
Image(user.profile_image.read())





