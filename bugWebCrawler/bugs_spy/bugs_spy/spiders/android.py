# -*- coding: utf-8 -*-
import scrapy
import logging

GOOGLE_USER = "virginiapmontilla@gmail.com"
GOOGLE_PSWD = "LyVy05251"

# http://scrapingauthority.com/scrapy-javascript


class AndroidSpider(scrapy.Spider):
    # Web to check different browser statuses: https://www.whatismybrowser.com/detect
    name = 'android'
    year = 2018

    reports_file_name = 'android_reports.xml'
    log_file_name = 'saved_android_log.txt'
    SETTINGS_SEARCH = 'ANDROID_SEARCH_URL'
    SETTINGS_DETAIL_URL = 'ANDROID_DETAIL_URL'

    start_urls = ['https://accounts.google.com/ServiceLogin?nojavascript=1']
    handle_httpstatus_list = [404, 405]

    def parse(self, response):
        print('inside parse')
        print(response.url)
        print(response.headers)
        return scrapy.FormRequest.from_response(
            response,
            formdata={'Email': GOOGLE_USER},
            callback=self.login_password
        )

    def login_password(self, response):
        print('inside login_password')
        print(response.url)
        return scrapy.FormRequest.from_response(
            response,
            formdata={'Passwd': GOOGLE_PSWD},
            callback=self.after_login)

    def after_login(self, response):
        base_search_url = self.settings.get(self.SETTINGS_SEARCH)
        # check login succeed before going on
        print('inside after_login')
        print(response.url)
        print(response.headers)
        if "Sign in" in response.text or "Acceder" in response.text:
            self.log("Login failed", level=logging.ERROR)
            print("NOOOOOO!!")
            return
        else:
            print("Login Successful!!")
            return scrapy.Request(
                url='https://issuetracker.google.com/issues?q=assignee:virginia.pujols.ti@gmail.com',
                headers=[{
                      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                      'Galaxy-Ajax': 'true',
                      'Origin': 'https://analytics.google.com',
                      'Referer': 'https://analytics.google.com/analytics/web/?hl=fr&pli=1',
                      'User-Agent': 'My-user-agent'}],
                callback=self.parse_issue_list)

    def parse_issue_list(self, response):
        print('\n\n\nShow me something: ', response.css('h1.bv2-app-title a::text').get())
        print('something 1: ', response.css('title::text').getall())
        print('something 2: ', response.css('title::text').get())
        print('something 3: ', response.xpath('//title'))
        print('something 4: ', response.xpath('//title/text()').get())

        bug_ids = response.xpath('//td[@data-template="issueId"]/a/text()').getall()
        print('the bug id is =', bug_ids)

        for bug_id in bug_ids:
            print('the bug id is =', bug_id)
            yield {'item': bug_id}

