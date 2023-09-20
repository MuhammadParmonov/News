from django.urls import path
from .views import main_page, batafsil_page, category_page, add_news, add_category, admin_page, del_news, yangilik_holati

urlpatterns = [
    path('', main_page, name="home-page"),
    path('category/<int:cat_id>', category_page, name="category-page"),
    path('batafsil/<int:id>', batafsil_page, name="batafsil-page"),
    path('addnews/', add_news, name="add-news-page"),
    path('addcategory/', add_category, name="add-category-page"),
    path('admin-panel/', admin_page, name="admin-page"),
    path('admin-panel/delete/<int:news_id>', del_news, name="del_news"),
    path('admin-panel/change/<int:news_id>', yangilik_holati, name="change_news"),
]