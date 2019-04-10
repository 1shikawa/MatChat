from django.contrib import admin
from match.models.userinfo import UserInfo, Image


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id','name',)  # 一覧に出したい項目
    list_display_links = ('name',)  # 修正リンクでクリックできる項目

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','origin',)  # 一覧に出したい項目
    list_display_links = ('id',)  # 修正リンクでクリックできる項目

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Image, ImageAdmin)