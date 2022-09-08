import base64

from django.http import HttpResponse
from django.shortcuts import HttpResponse, render
from django.template import loader
from ipware import get_client_ip

from .models import IncomingRequest


def ipinfo_get_client_ip(request):
    if hasattr(request, "ipinfo"):
        return request.ipinfo.all
    else:
        return dict()


def ipware_get_client_ip(request):
    result = dict()
    client_ip, is_routable = get_client_ip(request)
    # Able to get the client's IP address
    if client_ip is not None:
        # We got the client's IP address
        # routable is True, The client's IP address is publicly routable on the Internet
        # routable is False, The client's IP address is private
        result.update({
            "routable": is_routable,
            "client_ip": client_ip
        })

    return result


# Create your views here.
def landing(request):
    ipinfo_data = ipinfo_get_client_ip(request)
    ipware_data = ipware_get_client_ip(request)

    IncomingRequest.objects.create(
        ipware=ipware_data,
        ipinfo=ipinfo_data,
    )

    context = {}
    template = loader.get_template("landing.html")

    return HttpResponse(template.render(context, request))


def collect_loc(request, text):
    ipinfo_data = ipinfo_get_client_ip(request)
    ipware_data = ipware_get_client_ip(request)

    try:
        mystr_encoded = base64.b64decode(text).decode('utf-8')
        lat, long = mystr_encoded.replace(" ", "").split(",")
    except Exception as e:
        print(e)
        lat = None
        long = None

    IncomingRequest.objects.create(
        ipware=ipware_data,
        ipinfo=ipinfo_data,
        latitude=lat,
        longitude=long,
    )
    response = "405 Not found."
    return HttpResponse(response)
