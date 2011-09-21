def cas_context_processor(request):
    return {
        "user": request.user
    }