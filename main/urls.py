from django.urls import path
from .views import get_tokens_for_user,BusinessCardListView

urlpatterns = [
    path('api/token/', get_tokens_for_user, name='token_obtain_pair'),

    path('api/business_cards/', BusinessCardListView.as_view(), name='business_card_list'),
    path('api/business_cards/<int:pk>/', BusinessCardListView.as_view(), name='business_card_list_edit'),
]