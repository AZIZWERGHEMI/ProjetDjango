from django.urls import path
from .views import index, create_post, PostDetail, like

urlpatterns = [
    path('', index, name='index'),
    path('create_post/', create_post, name='create_post'),  # Added trailing slash for consistency
    path('<uuid:post_id>/', PostDetail, name='post_details'),  # Updated view function to lowercase and added trailing slash
    path('<uuid:post_id>/like/', like, name='like'),  # Added trailing slash for consistency
]
