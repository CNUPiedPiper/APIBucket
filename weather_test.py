import issue
#import mise
import weather

# print(issue.get_issue())

city = u"Chungnam"
lat = "35.016699999999986"
lon = "126.86669999999998"

#print(weather.get_weather(lat, lon))
print(weather.get_weather(lat, lon, "tomorrow"))
