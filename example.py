import json

f = open("IC.json")
IC = json.load(f)
print(IC["rho"][0]["right"])
f.close()
