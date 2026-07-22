from rest_framework.routers import DefaultRouter

from .views import GradeViewSet, LessonViewSet

router = DefaultRouter()
router.register("grades", GradeViewSet, basename="grade")
router.register("lessons", LessonViewSet, basename="lesson")

urlpatterns = router.urls
