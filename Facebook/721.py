class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_account = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_account[email].append(i)
        visited = [False] * len(accounts)
        emails = set()
        def dfs(account):
            if visited[account]:
                return
            visited[account] = True
            for email in accounts[account][1:]:
                emails.add(email)
                for neighbor in email_to_account[email]:
                    dfs(neighbor)
        res = []
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            emails = set()
            dfs(i)
            res.append([account[0]] + sorted(emails))
        return res

# solution 2: disjoint set
class disjoint_set:
    def __init__(self):
        self.parent = [i for i in range(10000)]
    def find(self, a):
        while self.parent[a] != a:
            a = self.parent[a]
        return a
    def union(self, a, b):
        roota, rootb = self.find(a), self.find(b)
        self.parent[rootb] = roota

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        DS = disjoint_set()
        email_to_id = {}
        email_to_name = {}
        emailid = 0
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = emailid
                    emailid += 1
                email_to_name[email] = name
                DS.union(email_to_id[account[1]], email_to_id[email])
        same_person = collections.defaultdict(list)
        for email in email_to_id:
            same_person[DS.find(email_to_id[email])].append(email)
        return [[email_to_name[person[0]]] + sorted(person) for person in same_person.values()]
