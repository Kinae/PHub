import pyArango.connection

from sample.entity.User import User

conn = pyArango.connection.Connection(username='root', password='root')
db = conn['pornhub']
collection = db['Users']


def find_by_email(email):
    aql = "FOR u IN Users FILTER u.email == @email RETURN u"
    result = db.AQLQuery(aql, rawResults=False, batchSize=1, bindVars={'email': email})
    if not result: raise ValueError('User does not exist : ' + email)
    return User(result[0])


def create_user(email):
    aql = "FOR u IN Users FILTER u.email == @email RETURN u"
    result = db.AQLQuery(aql, rawResults=False, batchSize=1, bindVars={'email': email})
    if not result:
        user = User(collection.createDocument())
        user.email = email
        return user
    else:
        raise ValueError('User already exist : ' + email)


def save_user(user):
    user.save()
