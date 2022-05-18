from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PickerView


picker_list = PickerView.as_view({
    'get': 'index',
    'post': 'pick',
})

urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('picker/', picker_list, name='picker_list'),
])
