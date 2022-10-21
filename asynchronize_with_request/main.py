import requests
from threading import Thread


class SDrequests(Thread):

    def __init__(self, url, method, headers=None, data=None, cookies=None):
        super(SDrequests, self).__init__()
        self.url = url
        self.method = method
        self.headers = headers if isinstance(headers, dict) else None
        self.data = data
        self.cookies = cookies
        self.start()

    def run(self):
        url = self.url
        headers = self.headers
        data = self.data
        cookies = self.cookies
        method = self.method

        if method.lower() == "post":
            r = requests.post(url=url, headers=headers, data=data, cookies=cookies)
        else:
            r = requests.get(url=url, headers=headers, data=data, cookies=cookies)

        response = r.content
        r.close()

        return response


if __name__ == "__main__":
    cookies = {
        'Cookie:T': 'BR%3Acjvqzhglu1mzt95aydzhvwzq1.1558031092050',
        'SWAB': 'build-44be9e47461a74d737914207bcbafc30',
        'lux_uid': '155867904381892986',
        'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
        'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C18041%7CMCMID%7C63273353035509304576927719203948933246%7CMCAID%7CNONE%7CMCOPTOUT-1558686245s%7CNONE%7CMCAAMLH-1559283845%7C12%7CMCAAMB-1559283845%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI',
        's_cc': 'true',
        'SN': '2.VI8085A6A237EB4C62836C8809F0D312EB.SI21A9EC4E99B949B2ACE6361B3F0208CC.VS187649B2B06A44C69824006710CB6D83.1558679078',
        'gpv_pn': 'HomePage',
        'gpv_pn_t': 'Homepage',
        'S': 'd1t17GQVqPz9KPzobP3M4GQkjPy34TjfJxI4SbXVIvhwzm3mE13vfSEulmf90D/7L710qUpMq8mA0k2bx6b2DuwIS4g==',
        's_sq': '%5B%5BB%5D%5D'}

    headers = {
        'Host': 'www.flipkart.com',
        'Connection': 'keep-alive',
        'Content-Length': '60',
        'X-user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36 FKUA/website/41/website/Desktop',
        'Origin': 'https://www.flipkart.com',
        'Save-Data': 'on',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Referer': 'https://www.flipkart.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
    }

    data = {
        'loginId': '+919904554170',
        'state': 'VERIFIED',
        'churnEmailRequest': 'false'
    }

    mu_req = SDrequests(url="https://www.flipkart.com/api/5/user/otp/generate", method="post", headers=headers,
                        data=data, cookies=cookies)

    print(mu_req)

