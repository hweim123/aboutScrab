import re
import urllib.request
import urllib.error


def craw(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
    imagelist = re.compile(pat2).findall(result1)
    x = 1
    for image_url in imagelist:
        image_name = "F:/myweb/img1/" + str(page) + str(x) + ".jpg"
        image_url = "http://" + image_url
        try:
            urllib.request.urlretrieve(image_url, filename=image_name)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                x += 1
            if hasattr(e, "reason"):
                x += 1
        x += 1


for i in range(1, 50):
    url = "http://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
    craw(url, i)
