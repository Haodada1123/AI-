from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.character import Character
from web.views.utils.photo import remove_old_photo


class RemoveCharacterView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            character_id = request.data['character_id']
            Character.objects.filter(pk=character_id, author__user=request.user).delete()
            remove_old_photo(character.photo)
            remove_old_photo(character.background_image)
            character.remove()
            return Response({
                'result':'成功'
            })
        except:
            return Response({
                'result': '系统异常，请稍后重试'
            })
