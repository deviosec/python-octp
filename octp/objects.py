class apiResponse(object):
    def __init__(self, status_code, text, jsonObj):
        self.status_code = status_code
        self.text = text
        self.json = jsonObj


class config(object):
    def __init__(self):
        self.initial_agents = 0
        self.buffersize_agents = 0
        self.initial_frontends = 0
        self.buffersize_frontends = 0
        self.challenges = []

    def toJson(self):
        data = {
            "initialagents": self.initial_agents,
            "buffersizeagents": self.buffersize_agents,
            "initialfrontends": self.initial_frontends,
            "buffersizefrontends": self.buffersize_frontends,
            "challenges": self.challenges,
        }
        return data

    def fromJson(self, jsonObj):
        self.initial_agents = jsonObj["initialagents"]
        self.buffersize_agents = jsonObj["buffersizeagents"]
        self.initial_frontends = jsonObj["initialfrontends"]
        self.buffersize_frontends = jsonObj["buffersizefrontends"]
        self.challenges = []
        if jsonObj["challenges"]:
            for chal in jsonObj["challenges"]:
                self.challenges.append(challenge(chal))
        return self

class heartbeat_req(object):
    def __init__(self):
        self.id = ""
        self.containers = []

    def toJson(self):
        data = {"id": self.id, "containers": self.containers}
        return data

    def fromJson(self, jsonObj):
        self.id = jsonObj["id"]
        self.containers = jsonObj["containers"]
        return self

class heartbeat_res(object):
    def __init__(self):
        self.action = False
        self.containers = []

    def toJson(self):
        data = {"id": self.id, "containers": self.containers}
        return data

    def fromJson(self, jsonObj):
        self.action = jsonObj["id"]
        self.containers = []
        if jsonObj["containers"]:
            for cont in jsonObj["containers"]:
                self.containers.append(container().fromJson(cont))
        return self

class registrycert(object):
    def __init__(self):
        self.cert = ""

    def toJson(self):
        data = {"cert": self.cert}
        return data

    def fromJson(self, jsonObj):
        self.cert = jsonObj["cert"]
        return self

class frontend(object):
    def __init__(self):
        self.id = ""
        self.claim = ""
        self.password = ""
        self.ip = ""

    def toJson(self):
        data = {"id": self.id, "claim": self.claim, "password": self.password, "ip": self.ip}
        return data

    def fromJson(self, jsonObj):
        self.id = jsonObj["id"]
        self.claim = jsonObj["claim"]
        self.password = jsonObj["password"]
        self.ip = jsonObj["ip"]
        return self


class agent(object):
    def __init__(self):
        self.id         = ""
        self.secret     = "" 
        self.trusted    = False
        self.lastbeat   = 0 
        self.claim      = "" 
        self.ip         = "" 
        self.privatekey = "" 
        self.publickey  = "" 
        self.containers = []

    def toJson(self):
        data = {
                "id": self.id,
                "secret": self.secret,
                "trusted": self.trusted,
                "lastbeat": self.lastbeat,
                "claim": self.claim,
                "ip": self.ip,
                "privatekey": self.privatekey,
                "publickey": self.publickey,
                "containers": self.containers,
                }
        return data

    def fromJson(self, jsonObj):
        self.id = jsonObj["id"]
        self.secret = jsonObj["secret"]
        self.trusted = jsonObj["trusted"]
        self.lastbeat = jsonObj["lastbeat"]
        self.claim = jsonObj["claim"]
        self.ip = jsonObj["ip"]
        self.privatekey = jsonObj["privatekey"]
        self.publickey = jsonObj["publickey"]
        self.containers = []
        if jsonObj["containers"]:
            for cont in jsonObj["containers"]:
                self.containers.append(container().fromJson(cont))
        return self

class container(object):
    def __init__(self):
        self.id         = ""
        self.image      = ""
        self.envs       = []
        self.ports      = []
        self.mounts     = []
        self.privileged = False
        self.state      = ""
        self.registry   = ""
        self.action     = ""

    def toJson(self):
        data = {
            "id":         self.id,
            "image":      self.image,
            "envs":       self.envs,
            "ports":      self.ports,
            "mounts":     self.mounts,
            "privileged": self.privileged,
            "state":      self.state,
            "registry":   self.registry,
            "action":     self.action,
        }

        return data

    def fromJson(self, jsonObj):
        self.id = jsonObj["id"]
        self.image = jsonObj["image"]
        self.envs = jsonObj["envs"]
        self.ports = jsonObj["ports"]
        self.mounts = jsonObj["mounts"]
        self.privileged = jsonObj["privileged"]
        self.state = jsonObj["state"]
        self.registry = jsonObj["registry"]
        self.action = jsonObj["action"]
        return self


# currently the same as a container
class challenge(container):
    pass
