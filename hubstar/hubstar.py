#!-*- coding: utf-8 -*-
from __future__ import with_statement
import os
import requests
import getpass
from collections import defaultdict
import github
import json

GITHUB_API_URL = "https://api.github.com/authorizations"

HTTPUnauthorized = 401
HTTPCreated = 201


class Hubstar(object):

    def __init__(self, owner_reposname):
        self._owner = owner_reposname.split('/')[0]
        self._reposname = owner_reposname.split('/')[1]
        self.__login()

    def star(self):
        auth_user, repos = self.__setup()
        if auth_user.has_in_starred(repos):
            print "You already starred: %s" % repos.html_url
        else:
            auth_user.add_to_starred(repos)
            print "Starred: %s" % repos.html_url

    def unstar(self):
        auth_user, repos = self.__setup()
        if not auth_user.has_in_starred(repos):
            print "You already unstarred: %s" % repos.html_url
        else:
            auth_user.remove_from_starred(repos)
            print "Unstarred: %s" % repos.html_url

    def __setup(self):
        gh = github.Github(login_or_token=self._access_token)

        try:
            user = gh.get_user(self._owner)
            repos = user.get_repo(self._reposname)
            auth_user = gh.get_user()
        except UnknownObjectException, e:
            raise HsErrorUnknownObject(e.data['message'])

        return auth_user, repos

    def __login(self):
        if os.path.isfile(os.path.join(os.environ["HOME"], ".hubstar")):
            self._access_token = self.__read_access_token_from_file()
        else:
            self._access_token = self.__get_new_access_token()

    def __read_access_token_from_file(self):
        with open(os.path.join(os.environ["HOME"], ".hubstar")) as f:
            access_token = f.readline().rstrip()
        return access_token

    def __get_new_access_token(self):
        print "Obtaining OAuth2 access_token from github"

        username = raw_input("Github username: ")
        password = getpass.getpass("Github password: ")

        url = GITHUB_API_URL
        payload = {"scopes": ["repo"],
                   "note": "hubstar"}
        headers = {"content-type": "application/json"}
        auth = (username, password)

        r = requests.post(url, data=json.dumps(payload),
                          headers=headers, auth=auth)

        if r.status_code == HTTPUnauthorized and r.headers["X-Github-OTP"]:
            twofa_code = raw_input("2-factor auth code: ")
            headers["X-Github-OTP"] = twofa_code
            rr = requests.post(url, data=json.dumps(payload),
                               headers=headers, auth=auth)

            if rr.status_code == HTTPCreated:
                with os.fdopen(
                        os.open(
                            os.path.join(os.environ["HOME"], ".hubstar"),
                            os.O_WRONLY | os.O_CREAT, 0600),
                        'w') as f:
                    f.write(rr.json()["token"])
                print "Success!"
                return rr.json()["token"]
            elif rr.status_code == HTTPUnauthorized:
                raise HsErrorUnauthorized(rr.json()["message"])
            else:
                raise HsErrorInternal(rr.content)
