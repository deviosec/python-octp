from octp import Octp


x = Octp("http://127.0.0.1:8000")

agents = x.agents()
print(agents)
frontends = x.frontends()
print(frontends)
print(x.frontend("eosToken"))

