import os
from django import template


register = template.Library()


@register.filter()
def get_usernames(queryset):
    """
    获取name
    :param queryset:
    :return:
    """
    # print(queryset.values_list('group.user_set.all', flat=True))
    perm_names =queryset.values_list("username", flat=True)
    return ",".join(perm_names)


@register.filter()
def get_names(queryset):
    """
    获取name
    :param queryset:
    :return:
    """
    # print(queryset.values_list('group.user_set.all', flat=True))
    perm_names =queryset.values_list("name", flat=True)
    return ",".join(perm_names)


@register.filter()
def cut(string, length):
    """
    截取字符串
    :param string:
    :param length:
    :return:
    """
    if len(string) <= length:
        return string
    else:
        s = string[:length] + "......"
        return s