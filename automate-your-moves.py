import sys
import mechanize

def main():
    file = open("login.txt", "r")
    username = file.readline().rstrip()
    password = file.readline().rstrip()
    file.close()

    reload(sys)
    sys.setdefaultencoding('utf8')
    br = mechanize.Browser()
    uri = "https://champchange.msu.montana.edu/"
    login = "index.php?location=/mypoints/&err0=7"

    br.open(uri+login)
    print br.title()
    br.select_form(nr=0)
    br.form['username'] = username
    br.form['password'] = password
    req = br.submit()
    print br.title()
    if br.title() != 'ChampChange - Point Totals':
        print "login failed"
        return
    

    for link in br.links():
        if link.text == "Nutrition":
            try:
                req = br.follow_link(link)
                br.select_form(nr=1)
                br.find_control("plate").items[0].selected=True
                req = br.submit()
            except:
                print "Already done Nutrition"
        if link.text == "Fitness":
            try:
                req = br.follow_link(link)
                br.select_form(nr=1)
                br.find_control("exercise").items[0].selected=True
                req = br.submit()
            except:
                print "Already done Fitness"
        if link.text == "Community":
            try:
                req = br.follow_link(link)
                br.select_form(nr=1)
                br.find_control("share").items[0].selected=True
                req = br.submit()
            except:
                print "Already done Community"
        if link.text == "Mental Health":
            try:
                req = br.follow_link(link)
                br.select_form(nr=1)
                br.find_control("relax").items[0].selected=True
                req = br.submit()
            except:
                print "Already done Mental Health"

    print "completed"

if __name__ == '__main__':
    main()