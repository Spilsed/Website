import os
from git import Repo

git_executable = r'C:\Program Files\Git\bin\git.exe'

os.environ['GIT_PYTHON_GIT_EXECUTABLE'] = 'C:\Program Files\Git\bin\git.exe'

def clone_and_install_test_folder(repo_url, local_folder):
    try:
        # Clone the repository to the local folder
        Repo.clone_from(repo_url, local_folder)

        print(f'Repository cloned successfully into {local_folder}')

        # Optionally, proceed with further operations here
        # ...

    except Exception as e:
        print(f'Failed to clone repository: {e}')

if __name__ == '__main__':
    github_repo_url = 'https://github.com/SatellaviewPlus/Satellaview-'
    local_folder = 'satdata'

    clone_and_install_test_folder(github_repo_url, local_folder)
    print('Installation completed.')
