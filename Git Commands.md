

Adding an existing project from local to a git repository

git init
git add  .
git commit -m "initial commit"
git remote add origin "repository_url_of_the_new_repo"
git branch -M main
git push -u origin main