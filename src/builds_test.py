import unittest
from unittest.mock import patch, ANY
import builds

import json

example_push_payload = """
{
  "ref": "refs/heads/assessment",
  "before": "205a6723f51af1432fb86c83147f3c3daf73e14b",
  "after": "66917246475acdd432e1e10725c9ee913451e488",
  "repository": {
    "id": 336031874,
    "node_id": "MDEwOlJlcG9zaXRvcnkzMzYwMzE4NzQ=",
    "name": "kth_decide",
    "full_name": "kazaaz/kth_decide",
    "private": true,
    "owner": {
      "name": "kazaaz",
      "email": "ayhamkazaz96@gmail.com",
      "login": "kazaaz",
      "id": 22964166,
      "node_id": "MDQ6VXNlcjIyOTY0MTY2",
      "avatar_url": "https://avatars.githubusercontent.com/u/22964166?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/kazaaz",
      "html_url": "https://github.com/kazaaz",
      "followers_url": "https://api.github.com/users/kazaaz/followers",
      "following_url": "https://api.github.com/users/kazaaz/following{/other_user}",
      "gists_url": "https://api.github.com/users/kazaaz/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/kazaaz/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/kazaaz/subscriptions",
      "organizations_url": "https://api.github.com/users/kazaaz/orgs",
      "repos_url": "https://api.github.com/users/kazaaz/repos",
      "events_url": "https://api.github.com/users/kazaaz/events{/privacy}",
      "received_events_url": "https://api.github.com/users/kazaaz/received_events",
      "type": "User",
      "site_admin": false
    },
    "html_url": "https://github.com/kazaaz/kth_decide",
    "description": null,
    "fork": false,
    "url": "https://github.com/kazaaz/kth_decide",
    "forks_url": "https://api.github.com/repos/kazaaz/kth_decide/forks",
    "keys_url": "https://api.github.com/repos/kazaaz/kth_decide/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/kazaaz/kth_decide/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/kazaaz/kth_decide/teams",
    "hooks_url": "https://api.github.com/repos/kazaaz/kth_decide/hooks",
    "issue_events_url": "https://api.github.com/repos/kazaaz/kth_decide/issues/events{/number}",
    "events_url": "https://api.github.com/repos/kazaaz/kth_decide/events",
    "assignees_url": "https://api.github.com/repos/kazaaz/kth_decide/assignees{/user}",
    "branches_url": "https://api.github.com/repos/kazaaz/kth_decide/branches{/branch}",
    "tags_url": "https://api.github.com/repos/kazaaz/kth_decide/tags",
    "blobs_url": "https://api.github.com/repos/kazaaz/kth_decide/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/kazaaz/kth_decide/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/kazaaz/kth_decide/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/kazaaz/kth_decide/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/kazaaz/kth_decide/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/kazaaz/kth_decide/languages",
    "stargazers_url": "https://api.github.com/repos/kazaaz/kth_decide/stargazers",
    "contributors_url": "https://api.github.com/repos/kazaaz/kth_decide/contributors",
    "subscribers_url": "https://api.github.com/repos/kazaaz/kth_decide/subscribers",
    "subscription_url": "https://api.github.com/repos/kazaaz/kth_decide/subscription",
    "commits_url": "https://api.github.com/repos/kazaaz/kth_decide/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/kazaaz/kth_decide/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/kazaaz/kth_decide/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/kazaaz/kth_decide/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/kazaaz/kth_decide/contents/{+path}",
    "compare_url": "https://api.github.com/repos/kazaaz/kth_decide/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/kazaaz/kth_decide/merges",
    "archive_url": "https://api.github.com/repos/kazaaz/kth_decide/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/kazaaz/kth_decide/downloads",
    "issues_url": "https://api.github.com/repos/kazaaz/kth_decide/issues{/number}",
    "pulls_url": "https://api.github.com/repos/kazaaz/kth_decide/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/kazaaz/kth_decide/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/kazaaz/kth_decide/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/kazaaz/kth_decide/labels{/name}",
    "releases_url": "https://api.github.com/repos/kazaaz/kth_decide/releases{/id}",
    "deployments_url": "https://api.github.com/repos/kazaaz/kth_decide/deployments",
    "created_at": 1612459958,
    "updated_at": "2021-02-10T11:39:17Z",
    "pushed_at": 1612959873,
    "git_url": "git://github.com/kazaaz/kth_decide.git",
    "ssh_url": "git@github.com:kazaaz/kth_decide.git",
    "clone_url": "https://github.com/kazaaz/kth_decide.git",
    "svn_url": "https://github.com/kazaaz/kth_decide",
    "homepage": null,
    "size": 104,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "Python",
    "has_issues": true,
    "has_projects": true,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": false,
    "forks_count": 0,
    "mirror_url": null,
    "archived": false,
    "disabled": false,
    "open_issues_count": 0,
    "license": {
      "key": "bsd-2-clause",
      "name": "BSD 2-Clause Simplified License",
      "spdx_id": "BSD-2-Clause",
      "url": "https://api.github.com/licenses/bsd-2-clause",
      "node_id": "MDc6TGljZW5zZTQ="
    },
    "forks": 0,
    "open_issues": 0,
    "watchers": 0,
    "default_branch": "master",
    "stargazers": 0,
    "master_branch": "master"
  },
  "pusher": {
    "name": "aljica",
    "email": "55843246+aljica@users.noreply.github.com"
  },
  "sender": {
    "login": "aljica",
    "id": 55843246,
    "node_id": "MDQ6VXNlcjU1ODQzMjQ2",
    "avatar_url": "https://avatars.githubusercontent.com/u/55843246?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/aljica",
    "html_url": "https://github.com/aljica",
    "followers_url": "https://api.github.com/users/aljica/followers",
    "following_url": "https://api.github.com/users/aljica/following{/other_user}",
    "gists_url": "https://api.github.com/users/aljica/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/aljica/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/aljica/subscriptions",
    "organizations_url": "https://api.github.com/users/aljica/orgs",
    "repos_url": "https://api.github.com/users/aljica/repos",
    "events_url": "https://api.github.com/users/aljica/events{/privacy}",
    "received_events_url": "https://api.github.com/users/aljica/received_events",
    "type": "User",
    "site_admin": false
  },
  "created": false,
  "deleted": false,
  "forced": false,
  "base_ref": null,
  "compare": "https://github.com/kazaaz/kth_decide/compare/205a6723f51a...66917246475a",
  "commits": [
    {
      "id": "66917246475acdd432e1e10725c9ee913451e488",
      "tree_id": "e4a9cbeb2c1f690dde37d06aafa9dace2257dd56",
      "distinct": true,
      "message": ".",
      "timestamp": "2021-02-10T13:24:29+01:00",
      "url": "https://github.com/kazaaz/kth_decide/commit/66917246475acdd432e1e10725c9ee913451e488",
      "author": {
        "name": "aljica",
        "email": "aljica@kth.se"
      },
      "committer": {
        "name": "aljica",
        "email": "aljica@kth.se"
      },
      "added": [

      ],
      "removed": [

      ],
      "modified": [
        "README.md"
      ]
    }
  ],
  "head_commit": {
    "id": "66917246475acdd432e1e10725c9ee913451e488",
    "tree_id": "e4a9cbeb2c1f690dde37d06aafa9dace2257dd56",
    "distinct": true,
    "message": ".",
    "timestamp": "2021-02-10T13:24:29+01:00",
    "url": "https://github.com/kazaaz/kth_decide/commit/66917246475acdd432e1e10725c9ee913451e488",
    "author": {
      "name": "aljica",
      "email": "aljica@kth.se"
    },
    "committer": {
      "name": "aljica",
      "email": "aljica@kth.se"
    },
    "added": [

    ],
    "removed": [

    ],
    "modified": [
      "README.md"
    ]
  }
}
"""

class TestBuilds(unittest.TestCase):

    @patch("db.create_connection")
    @patch("db.select_commit")
    def test_get_should_return_build_with_correct_id(self, select_commit_patch, create_connection_patch):
        # Arrange
        commit_id = "04dbec97248ca15f8db8567efbe48b3b2e85a32e"
        build_details = {
            "commit_id": commit_id,
            "build_date": "20200202",
            "build_logs": "Testing...Test OK",
            "url": "/builds/"+commit_id
        }
        select_commit_patch.return_value = build_details

        # Act
        got = builds.get(commit_id)

        # Assert
        ## builds.get should return correct build details
        self.assertEqual(build_details, got)
        ## builds.get should connect to db
        create_connection_patch.assert_called_once()
        ## builds.get fetches build with correct id
        select_commit_patch.assert_called_with(ANY, commit_id)



    @patch("db.create_connection")
    @patch("db.select_all")
    def test_list(self, select_all_patch, create_connection_patch):
        # Arrange
        commit_id_1 = "14dbec97248ca15f8db8567efbe48b3b2e85a32e"
        build_details_1 = {
            "commit_id": commit_id_1,
            "build_date": "20200202",
            "build_logs": "Testing...Test OK",
            "url": "/builds/"+commit_id_1
        }
        commit_id_2 = "14dbec97248ca15f8db8567efbe48b3b2e85a32e"
        build_details_2 = {
            "commit_id": commit_id_2,
            "build_date": "20200201",
            "build_logs": "Testing...Test Failed",
            "url": "/builds/"+commit_id_2
        }
        all_commits = [build_details_1, build_details_2]
        select_all_patch.return_value = all_commits

        # Act
        got = builds.list()

        # Assert
        ## should connect to db
        create_connection_patch.assert_called_once()
        ## should select all from db
        select_all_patch.assert_called_once()
        ## should return all commits
        self.assertEqual(all_commits, got)


    @patch("db.create_connection")
    @patch("db.insert_commit")
    def test_create(self, insert_patch, create_connection_patch):
        # Act
        builds.create(json.loads(example_push_payload))

        # Assert
        ## should connect to db
        create_connection_patch.assert_called_once()
        ## should insert correct values
        insert_patch.assert_called_with(ANY, ("66917246475acdd432e1e10725c9ee913451e488", "20210210_132429", ANY, "/builds/66917246475acdd432e1e10725c9ee913451e488"))

if __name__ == '__main__':
    unittest.main()

