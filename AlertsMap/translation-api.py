#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Translate.

Command-line application that translates some text.
"""
from __future__ import print_function

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

from googleapiclient.discovery import build


def main():
    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build('translate', 'v2', developerKey='AIzaSyC20MzMnsej9TiaqhuNtAzPyBH4Ph4lQr8')

    return service.translations().list(
        source='en',
        target='uk',
        q=[
            u"There are 15 disabled persons in village, 10 out of them have cancer. There is neither a hospital, nor a pharmacy in the village, just some medical point run by one doctor. Reportedly, people stated that they do not have access to confidential medical assistance (including PSS and visit to a gynecologist). People also informed that they have not received any humanitarian aid.",
            u'собака']
    ).execute()


# result = main()


result = {u'translations': [{
                       u'translatedText': u'\u0423 \u0441\u0435\u043b\u0456 15 \u0456\u043d\u0432\u0430\u043b\u0456\u0434\u0456\u0432, 10 \u0437 \u043d\u0438\u0445 \u043c\u0430\u044e\u0442\u044c \u0440\u0430\u043a. \u0423 \u0441\u0435\u043b\u0456 \u043d\u0435\u043c\u0430\u0454 \u043d\u0456 \u043b\u0456\u043a\u0430\u0440\u043d\u0456, \u043d\u0456 \u0430\u043f\u0442\u0435\u043a\u0438, \u0430 \u043f\u0440\u043e\u0441\u0442\u043e \u043c\u0435\u0434\u0438\u0447\u043d\u0438\u0439 \u043f\u0443\u043d\u043a\u0442, \u0437\u0430 \u044f\u043a\u0438\u043c \u043a\u0435\u0440\u0443\u0454 \u043e\u0434\u0438\u043d \u043b\u0456\u043a\u0430\u0440. \u042f\u043a \u043f\u043e\u0432\u0456\u0434\u043e\u043c\u043b\u044f\u0454\u0442\u044c\u0441\u044f, \u043b\u044e\u0434\u0438 \u0437\u0430\u044f\u0432\u0438\u043b\u0438, \u0449\u043e \u043d\u0435 \u043c\u0430\u044e\u0442\u044c \u0434\u043e\u0441\u0442\u0443\u043f\u0443 \u0434\u043e \u043a\u043e\u043d\u0444\u0456\u0434\u0435\u043d\u0446\u0456\u0439\u043d\u043e\u0457 \u043c\u0435\u0434\u0438\u0447\u043d\u043e\u0457 \u0434\u043e\u043f\u043e\u043c\u043e\u0433\u0438 (\u0432\u043a\u043b\u044e\u0447\u0430\u044e\u0447\u0438 PSS \u0442\u0430 \u0432\u0456\u0437\u0438\u0442 \u0434\u043e \u0433\u0456\u043d\u0435\u043a\u043e\u043b\u043e\u0433\u0430). \u041b\u044e\u0434\u0438 \u0442\u0430\u043a\u043e\u0436 \u043f\u043e\u0432\u0456\u0434\u043e\u043c\u0438\u043b\u0438, \u0449\u043e \u043d\u0435 \u043e\u0442\u0440\u0438\u043c\u0430\u043b\u0438 \u0436\u043e\u0434\u043d\u043e\u0457 \u0433\u0443\u043c\u0430\u043d\u0456\u0442\u0430\u0440\u043d\u043e\u0457 \u0434\u043e\u043f\u043e\u043c\u043e\u0433\u0438.'},
                   {u'translatedText': u'\u0421\u043e\u0431\u0430\u043a\u0430'}]}

print(map(lambda x: x['translatedText'], result['translations'])[0])

