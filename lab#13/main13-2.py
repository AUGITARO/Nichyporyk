# -*- coding: cp1251 -*-
import re


def is_valid_url(url):
    pattern = re.compile(
        r'^(https?://)?'
        r'(?:(?!-)[a-zA-Z]{2,}(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+'
        r'[a-zA-Z]{2,}'
        r'(:\d{1,5})?'
        r'(/[^?#]*)?'
        r'(\?[^#]*)?'
        r'(#.*)?$'
    )

    return bool(pattern.match(url))


# Примеры использования
print(is_valid_url("http://www.zcontest.ru"))
print(is_valid_url("http://www.zcontest.ru?id=1"))
print(is_valid_url("http://zcontest.ru"))
print(is_valid_url("Just Text"))
print(is_valid_url("http://a.com"))
print(is_valid_url("http://valid-domain.com"))
