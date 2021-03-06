from django.urls import path

from .import views


urlpatterns = [
    path('',views.user),
    path('dashboard',views.dashboard),
    path('create/user',views.create_user),
    path('user/login',views.login),
    path('user/logout',views.logout),
    path('new/job',views.new_job),
    path('add/job',views.add_job),
    path('delete/<int:job_id>/',views.delete_job),
    path('edit/<int:job_id>/',views.edit_job),
    path('edit/<int:job_id>/update',views.update_job),
    path('view/<int:job_id>/', views.view_job),
    path('user/reviews/<int:job_id>',views.load_review_page), # path for review page
    path('create-review',views.create_review),# path that renders the review form
    path('acceptbid/<int:id>',views.acceptbid),
    path('cancelbid/<int:id>',views.cancelbid)
    ]