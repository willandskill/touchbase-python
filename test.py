from touchbase_python.touchbase import Client

print '-------------'
# AUTH
print 'AUTH'
client = Client()
client.authenticate('ica_manager', 'ICA2015!')
print client.HEADERS
print '-------------'

# VISUALIZE
print 'VISUALIZE - MEDIA - LIST'
media = client.media
results = media.list_next().results
print results
print 'VISUALIZE - MEDIA - DETAIL'
pk = results[0]['id']
print media.detail(pk)

# UPLOADIFY
print 'UPLOADIFY - FILEZILLA - LIST'
filezilla = client.filezilla
results = filezilla.list_next().results
print results
print 'UPLOADIFY - FILEZILLA - DETAIL'
pk = results[0]['id']
print filezilla.detail(pk)


# BLOGIFY
print 'BLOGIFY - POST - LIST'
post = client.post
results = post.list_next().results
print results
print 'BLOGIFY - POST - DETAIL'
pk = results[0]['id']
print post.detail(pk)
