from .proxies import proxy_list
import requests
import random


class ParentChecker:
    """init has card as arg"""
    def __init__(self, card: str):
        data = card.split("|")
        try:
            self.ccn, self.month, self.year, self.cvc = data[0].strip(), data[1].strip(), data[2].strip(), data[3].strip()
        except IndexError:
            self.invalid = True

        self.session = requests.session()
        self.session.proxies.update(random.choice(proxy_list))


    @staticmethod
    def format_headers(unformatted_headers):
        """Formats Headers"""
        formatted_headers = dict()
        lines = unformatted_headers.split("\n")
        for line in lines:
            if len(line)>1:
              index= line.find(":")
              formatted_headers[line[:index].strip()] = line[index+1:].strip()
        return formatted_headers

    def add_cookies(self, cookies: str):
        """Adds cookies to requests session. Reqeusts session can be called by self.session.(method)"""
        cookies_dict = dict()
        for item in cookies.splitlines():
            cookie = item.split("okie:", maxsplit= 1)[1]
            key, value = cookie.split("=", maxsplit= 1)
            cookies_dict[key] = value
        cj = requests.utils.cookiejar_from_dict(cookies_dict)
        self.session.cookies = cj


