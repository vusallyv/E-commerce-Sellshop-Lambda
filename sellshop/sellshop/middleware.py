import socket
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class IPAddressMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(socket.gethostbyname(socket.gethostname()))

    def process_response(self, request, response):
        BLOCKED_IP = ['127.0.0.1']
        if socket.gethostbyname(socket.gethostname()) in BLOCKED_IP:
            return render(request, "error-404.html")
            return HttpResponse("Blocked IP Address")
        return response

