from googlesearch import search
import requests
request = search.SearchAPIRequest(email=u"clark.kent@example.com")
response = request.send()

print(response.image.get_thumbnail_url(200, 100, zoom_face=True, favicon=False))
print(response.name)
print(response.education)
print(response.username)
print(response.address)
print(", ".join(map(str, response.person.jobs)))
print(", ".join(map(str, response.person.relationships)))
                                
