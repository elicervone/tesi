import requests, git, random
import os
import subprocess
from time import sleep

def clone_repositories(commits, owner):

    title = commits[0].split("-")[0]

    nums = []
    nums.append(0)
    i = 1

    for commit in commits:
        if title != commit.split("-")[0]:
            nums.append(i)

        title = commit.split("-")[0]
        i+=1

    random_numbers = random.sample(range(412), 30)
    random_numbers.sort()

    for inizio in nums:
        for numero in random_numbers:
            split_result = commits[inizio+numero].split("-")
            commit_sha = split_result[1]
            rep = "-".join(split_result[2:])

            repo_url = f'https://github.com/{owner}/{rep}'
            print(rep)

            destination_folder = r'/home/so/Desktop/commits'
            dest = rep+"-"+commit_sha
            repo_destination = f'{destination_folder}/{dest}'

            try:
                #git.Repo.clone_from(repo_url, repo_destination, branch=commit_sha, depth=1)

                # Clona il repository
                subprocess.run(["git", "clone", repo_url, repo_destination])                
                print(f'Repository "{rep}" clonata con successo.')
            except Exception as e:
                print(f'Errore durante il clone del repository "{rep}": {str(e)}')

            try:
                # Cambia la directory di lavoro
                os.chdir(repo_destination)
                print(f'Successo cd')
            except Exception as e:
                print(f'Errore durante il cd')

            try:
                # Effettua il reset hard al commit specificato
                subprocess.run(["git", "reset", "--hard", commit_sha])
                print(f'Successo commit')
            except:
                print(f'Errore durante il clone del commit {commit_sha}')