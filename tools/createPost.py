from application import collections

alias = raw_input('alias: ')

title = raw_input('title: ')

content = raw_input('post (must be under 1000 characters): ')

user = collections.User.object(alias=alias)[0]  # returns user object by alias

post = collections.Posts(user=user, title=title, content=content)

post.save()
