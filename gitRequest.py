import requests
import json
import pprint

def getRepos(user):
	if(isinstance(user, str)):
		url = "https://api.github.com/users/"+user+"/repos"
		req = requests.get(url = url) 
		res = req.json()

		#pprint.pprint(res)
		if(res):
			#print repos very nicely
			for repo in res:
				name = repo["name"]
				commitNum = getCommits(user, name)
				print("REPO: "+name+", Commits: "+str(commitNum))

			return True
		else:
			return False
	else:
		print("Not a valid user")
		return False

def getCommits(user, repo):
	if(isinstance(user, str) and isinstance(repo, str)):
		url = "https://api.github.com/repos/"+user+"/"+repo+"/commits"
		req = requests.get(url = url) 
		res = req.json()

		if(res):
			#count number of commits
			return len(res)
		else:
			return "Not valid repo or user"
	else:
		return "Not valid input"
	