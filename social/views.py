from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from social.models import Social


@login_required
@csrf_exempt
def follow_action(request, user_id):
    _owner = request.user

    if _owner.id == int(user_id):
        raise Http404

    try:
        Social.objects.get(
            owner = _owner,
            following_id = user_id
        )
        raise Http404
    except Social.DoesNotExist, e:
        Social.objects.create(
            owner = _owner,
            following_id = user_id
        )
    return


@login_required
@csrf_exempt
def unfollow_action(request, user_id):

    _owner = request.user

    try:
        uf = Social.objects.get(
            owner = _owner,
            following_id = user_id,
        )
        uf.delete()
    except Social.DoesNotExist, e:
        raise Http404
    # return JSONResponse(data={'status':0})


__author__ = 'edison'
