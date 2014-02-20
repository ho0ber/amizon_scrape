import mechanize
import cookielib
import os
import sys
import random
import yaml

class Scraper(object):

  def __init__(self):
      self.logins = self._get_config()
      self.browser = self._set_up_browser()


  def _get_config(self):
      base_path = os.path.dirname(os.path.abspath(__file__))
      logins_file = open(os.path.join(base_path, os.pardir, "config", 'logins.yml'))
      logins = yaml.safe_load(logins_file)
      return logins


  def _set_up_browser(self):
      # Browser
      br = mechanize.Browser()

      # Cookie Jar
      cj = cookielib.LWPCookieJar()
      br.set_cookiejar(cj)

      # Browser options
      br.set_handle_equiv(True)
      #br.set_handle_gzip(True)
      br.set_handle_redirect(True)
      br.set_handle_referer(True)
      br.set_handle_robots(False)

      # Follows refresh 0 but not hangs on refresh > 0
      br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

      # Want debugging messages?
      #br.set_debug_http(True)
      #br.set_debug_redirects(True)
      #br.set_debug_responses(True)

      # User-Agent (this is cheating, ok?)
      br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

      return br

  def scrape(self):
      url = 'http://www.occamsrazorlarp.com/cdb/'
      results = []
      for login in self.logins:
        self._open_and_log_in(self.browser, url, login, self.logins[login])
        results.append(self._get_items(self.browser))

      return results

  def _open_and_log_in(self, browser, url, user, password):
    # Open some site, let's pick a random one, the first that pops in mind:
    browser.open(url)

    # Show the source
    browser.select_form(nr=0)
    browser.form['data[User][username]'] = user
    browser.form['data[User][password]'] = password
    browser.form.action = url

    browser.submit()

    return browser

  def _get_items(self, browser):
    browser.follow_link(text='Amizon')
    browser.follow_link(text='Buy Items')

    html = browser.response().read()

    lines = html.split("\r\n")
    for line in lines:
      if "$scope.marketplace = " in line:
        return line[len("$scope.marketplace = ")+1:-1]

    return ""
