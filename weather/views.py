from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city=request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather/?q='+city+'&appid=84b9f3830de8f88f17ab51b1cc869638').read()
        json_data=json.loads(res)
        data={
            "coutry_code":str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon'])+' '+
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),

        }

    else:
        data={}

   
    return render(request,'index.html',data)