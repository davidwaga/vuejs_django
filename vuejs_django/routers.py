from rest_framework import routers
from article.viewsets import ArticleViewSet
from subscriptions.viewsets import SubscriptionViewSet

router = routers.DefaultRouter()

router.register('article', ArticleViewSet)
router.register('subscriptions', SubscriptionViewSet)