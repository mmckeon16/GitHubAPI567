import unittest
from unittest.mock import Mock, patch

import gitRequest

class gitRequestTest(unittest.TestCase):

	@patch('HW4.services.requests.get')
	def testGetRepos(mockCall):
		mockJson = {
			'id': 87034273,
			'node_id': 'MDEwOlJlcG9zaXRvcnk4NzAzNDI3Mw==',
			'name': 'Collect-Website',
			'full_name': 'mmckeon16/Collect-Website',
			'private': False,
			'owner': 
				{'login': 'mmckeon16',
				'id': 19711687,
				'node_id': 'MDQ6VXNlcjE5NzExNjg3',
				'avatar_url': 'https://avatars1.githubusercontent.com/u/19711687?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/mmckeon16',
				'html_url': 'https://github.com/mmckeon16',
				'followers_url': 'https://api.github.com/users/mmckeon16/followers',
				'following_url': 'https://api.github.com/users/mmckeon16/following{/other_user}',
				'gists_url': 'https://api.github.com/users/mmckeon16/gists{/gist_id}',
				'starred_url': 'https://api.github.com/users/mmckeon16/starred{/owner}{/repo}',
				'subscriptions_url': 'https://api.github.com/users/mmckeon16/subscriptions',
				'organizations_url': 'https://api.github.com/users/mmckeon16/orgs',
				'repos_url': 'https://api.github.com/users/mmckeon16/repos',
				'events_url': 'https://api.github.com/users/mmckeon16/events{/privacy}',
				'received_events_url': 'https://api.github.com/users/mmckeon16/received_events',
				'type': 'User', 'site_admin': False
				},
			'html_url': 'https://github.com/mmckeon16/Collect-Website',
			'description': 'Git Rep for collect website',
			'fork': True, 'url': 'https://api.github.com/repos/mmckeon16/Collect-Website',
			'forks_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/forks',
			'keys_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/keys{/key_id}','collaborators_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/teams', 'hooks_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/hooks', 'issue_events_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/issues/events{/number}', 'events_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/events', 'assignees_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/assignees{/user}', 'branches_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/branches{/branch}', 'tags_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/tags', 'blobs_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/languages', 'stargazers_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/stargazers', 'contributors_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/contributors', 'subscribers_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/subscribers', 'subscription_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/subscription', 'commits_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/contents/{+path}', 'compare_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/merges', 'archive_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/downloads', 'issues_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/issues{/number}', 'pulls_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/labels{/name}', 'releases_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/releases{/id}', 'deployments_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/deployments', 'created_at': '2017-04-03T03:13:54Z', 'updated_at': '2017-04-03T03:42:04Z', 'pushed_at': '2017-04-03T03:42:03Z', 'git_url': 'git://github.com/mmckeon16/Collect-Website.git', 'ssh_url': 'git@github.com:mmckeon16/Collect-Website.git', 'clone_url': 'https://github.com/mmckeon16/Collect-Website.git', 'svn_url': 'https://github.com/mmckeon16/Collect-Website', 'homepage': None, 'size': 2153, 'stargazers_count': 0, 'watchers_count': 0, 'language': 'PHP', 'has_issues': False, 'has_projects': True, 'has_downloads': True, 'has_wiki': True, 'has_pages': False, 'forks_count': 0, 'mirror_url': None, 'archived': False, 'open_issues_count': 0, 'license': None, 'forks': 0, 'open_issues': 0, 'watchers': 0, 'default_branch': 'master'
		}

		mockCall.return_value = Mock()
		mockCall.return_value.json.return_value = mockJson
		
		assert_true(gitRequest.getRepos("mmckeon16"))
		assert_true(gitRequest.getRepos(123))
		assert_true(mockCall.called)

		
	def testGetCommits(mockCall):
		mockJson = {
			'id': 87034273,
			'node_id': 'MDEwOlJlcG9zaXRvcnk4NzAzNDI3Mw==',
			'name': 'Collect-Website',
			'full_name': 'mmckeon16/Collect-Website',
			'private': False,
			'owner': 
				{'login': 'mmckeon16',
				'id': 19711687,
				'node_id': 'MDQ6VXNlcjE5NzExNjg3',
				'avatar_url': 'https://avatars1.githubusercontent.com/u/19711687?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/mmckeon16',
				'html_url': 'https://github.com/mmckeon16',
				'followers_url': 'https://api.github.com/users/mmckeon16/followers',
				'following_url': 'https://api.github.com/users/mmckeon16/following{/other_user}',
				'gists_url': 'https://api.github.com/users/mmckeon16/gists{/gist_id}',
				'starred_url': 'https://api.github.com/users/mmckeon16/starred{/owner}{/repo}',
				'subscriptions_url': 'https://api.github.com/users/mmckeon16/subscriptions',
				'organizations_url': 'https://api.github.com/users/mmckeon16/orgs',
				'repos_url': 'https://api.github.com/users/mmckeon16/repos',
				'events_url': 'https://api.github.com/users/mmckeon16/events{/privacy}',
				'received_events_url': 'https://api.github.com/users/mmckeon16/received_events',
				'type': 'User', 'site_admin': False
				},
			'html_url': 'https://github.com/mmckeon16/Collect-Website',
			'description': 'Git Rep for collect website',
			'fork': True, 'url': 'https://api.github.com/repos/mmckeon16/Collect-Website',
			'forks_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/forks',
			'keys_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/keys{/key_id}','collaborators_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/teams', 'hooks_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/hooks', 'issue_events_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/issues/events{/number}', 'events_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/events', 'assignees_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/assignees{/user}', 'branches_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/branches{/branch}', 'tags_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/tags', 'blobs_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/languages', 'stargazers_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/stargazers', 'contributors_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/contributors', 'subscribers_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/subscribers', 'subscription_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/subscription', 'commits_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/contents/{+path}', 'compare_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/merges', 'archive_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/downloads', 'issues_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/issues{/number}', 'pulls_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/labels{/name}', 'releases_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/releases{/id}', 'deployments_url': 'https://api.github.com/repos/mmckeon16/Collect-Website/deployments', 'created_at': '2017-04-03T03:13:54Z', 'updated_at': '2017-04-03T03:42:04Z', 'pushed_at': '2017-04-03T03:42:03Z', 'git_url': 'git://github.com/mmckeon16/Collect-Website.git', 'ssh_url': 'git@github.com:mmckeon16/Collect-Website.git', 'clone_url': 'https://github.com/mmckeon16/Collect-Website.git', 'svn_url': 'https://github.com/mmckeon16/Collect-Website', 'homepage': None, 'size': 2153, 'stargazers_count': 0, 'watchers_count': 0, 'language': 'PHP', 'has_issues': False, 'has_projects': True, 'has_downloads': True, 'has_wiki': True, 'has_pages': False, 'forks_count': 0, 'mirror_url': None, 'archived': False, 'open_issues_count': 0, 'license': None, 'forks': 0, 'open_issues': 0, 'watchers': 0, 'default_branch': 'master'
		}
		print("second commit test")
		mockCall.return_value = Mock()
		mockCall.return_value.json.return_value = mockJson;
		# assert_equal(gitRequest.getCommits("mmckeon16", "gameStates"), 2)
		# assert_equal(gitRequest.getCommits(123, 5.968), "Not valid input")
		# assert_equal(gitRequest.getCommits("mmckeon16", "48"), 2)
		# assert_equal(gitRequest.getCommits("nfwjfjberfosermf", "fknzefj"), 2)
		assert_true(mockCall.called)
		

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()