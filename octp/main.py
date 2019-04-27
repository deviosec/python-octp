import logging
import requests
import json

from .endpoints import *
from .objects import *


class Octp(object):
    def __init__(self, base_url=None):
        if base_url == None:
            logging.error("No valid base_url set, exiting")
            exit()

        self.base_url = base_url
        self.s = requests.session()

    def __keyExists(self, data, key):
        try:
            data[key]
            return True
        except:
            return False

    def __makeRequest(self, method, endpoint, data=None):
        url = "{0}/{1}".format(self.base_url, endpoint)

        headers = {
            "content-type": "application/json",
        }
        if method == "GET":
            req = requests.Request(method, url, headers=headers)
        elif method == "POST":
            req = requests.Request(
                method, url, data=json.dumps(data), headers=headers)
        else:
            req = requests.Request(method, url, headers=headers)

        prep = self.s.prepare_request(req)
        r = self.s.send(prep, timeout=5)
        rjson = r.json()

        if self.__keyExists(rjson, "error") and not rjson["error"] == "":
            raise Exception(rjson["error"])

        return apiResponse(r.status_code, r.text, rjson)

    def __makeGet(self, endpoint):
        return self.__makeRequest("GET", endpoint)

    def __makePost(self, endpoint, data=None):
        return self.__makeRequest("GET", endpoint, data=data)

    def __makeDelete(self, endpoint):
        return self.__makeRequest("DELETE", endpoint)

    def ping(self):
        try:
            res = self.__makeGet(API_GET_PING)
        except requests.exceptions.ConnectionError:
            return False
        except requests.exceptions.Timeout:
            return False

        if not res.json["ok"]:
            return False
        return True

    def conf(self):
        res = self.__makeGet(API_GET_CONF)
        return config(res.json)

    def send_conf(self, conf):
        assert isinstance(conf, config),"The specifed config is not of object octp.object.config"
        res = self.__makePost(API_POST_CONF, data=conf.toJson())

        if not res.json["ok"]:
            return False
        return True

    def get_registry_cert(self):
        res = self.__makeGet(API_GET_REGISTRYCERT)

        return registrycert().fromJson(req.json)

    def heartbeat(self, hb):
        assert isinstance(hb, heartbeat_req),"The specifed heartbeat is not of object octp.object.heartbeat_req"
        res = self.__makePost(API_POST_HEARTBEAT, data=hb.toJson())

        return heartbeat_res().fromJson(res.json)

    def agents(self):
        res = self.__makeGet(API_GET_AGENTS)
        agents = []
        for a in res.json["agents"]:
            agents.append(agent().fromJson(a))

        return agents

    def create_agent(self):
        res = self.__makePost(API_POST_AGENTS)

        if not res.json["ok"]:
            return False
        return True

    def claim_agent(self, name, email):
        data = {"name": name, "email": email}
        res = self.__makePost(API_POST_AGENTS, data=data)

        return agent().fromJson(res.json["agent"])

    def agent(self, agentid):
        res = self.__makeGet(API_GET_AGENT.format(agentid=agentid))
        return agent().fromJson(res.json["agent"])

    def delete_agent(self, agentid):
        res = self.__makeDelete(API_DELETE_AGENT.format(agentid=agentid))

        if not res.json["ok"]:
            return False
        return True

    def frontends(self):
        res = self.__makeGet(API_GET_FRONTENDS)
        frontends = []
        for a in res.json["frontends"]:
            frontends.append(frontend().fromJson(a))

        return frontends

    def create_frontend(self):
        res = self.__makePost(API_POST_FRONTENDS)

        if not res.json["ok"]:
            return False
        return True

    def claim_frontend(self, name, email):
        data = {"name": name, "email": email}
        res = self.__makePost(API_POST_FRONTENDS, data=data)

        return frontend().fromJson(res.json["frontend"])

    def frontend(self, frontendid):
        res = self.__makeGet(API_GET_FRONTEND.format(frontendid=frontendid))
        return frontend().fromJson(res.json["frontend"])

    def delete_frontend(self, frontendid):
        res = self.__makeDelete(
            API_DELETE_FRONTEND.FOrmat(frontendid=frontendid))

        if not res.json["ok"]:
            return False
        return True
