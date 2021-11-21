
def verificate_email(request):
    verify_message = ""
    if request.user.is_authenticated == True and request.user.is_active == False:
        verify_message = "Please, verify your email address."
    return verify_message
