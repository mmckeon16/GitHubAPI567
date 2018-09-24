import unittest

import gitRequest

class gitRequestTest(unittest.TestCase):
	def testGetRepos(self):
		self.assertTrue(gitRequest.getRepos("mmckeon16"))
		#self.assertFalse(gitRequest.getRepos(123))
		
	def testGetCommits(self):
		print("second commit test")
	#	self.assertEqual(gitRequest.getCommits("mmckeon16", "GitHubAPI567"), 1)
	#	self.assertEqual(gitRequest.getCommits(123, 5.968), "Not valid input")
	#	self.assertEqual(gitRequest.getCommits("mmckeon16", "48"), "No commits, valid user")
	#	self.assertEqual(gitRequest.getCommits("nfwjfjberfosermf", "fknzefj"), "Not valid repo or user")
		

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()