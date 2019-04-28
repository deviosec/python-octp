from octp import Octp
import octp


x = Octp("http://127.0.0.1:8000")

try:
    agents = x.agents()
except octp.exceptions.Timedout as e:
    agents = []
    print("error")
print(agents)
# frontends = x.frontends()
# print(frontends)
# print(x.frontend("eosToken"))

