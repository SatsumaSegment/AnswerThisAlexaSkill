import mechanicalsoup

def swear_check(words):
    
    URL = 'https://github.com/coffee-and-fun/google-profanity-words/blob/main/data/list.txt'
    WORD_LIST = 958
    
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(URL)

    finding = browser.page.find_all('td')
    del finding[::2]

    for j in range(WORD_LIST):
        if finding[j].text in words:
            return 1
        
    return 0

def answer_search(s):

    q = str(s)
    q.replace(" ", "%20")
    
    URL = 'https://www.answers.com/search?q=' + q
    
    browser = mechanicalsoup.StatefulBrowser()
    browser.session.cookies.set('OptanonConsent', 'isGpcEnabled=0&datestamp=Tue+Nov+22+2022+17%3A49%3A28+GMT%2B0000+(Greenwich+Mean+Time)&version=6.36.0&isIABGlobal=false&hosts=&consentId=9867d29f-a972-4743-b082-d76c3817d192&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CSTACK42%3A0&geolocation=GB%3BENG&AwaitingReconsent=false', domain='.answers.com')
    browser.open(URL)
    
    finding = browser.page.find('div', id='best-answer').text[15:]

    end = "Q:"
    finding = finding[:finding.find(end)]

    return str(finding)




