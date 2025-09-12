# git init is used to initialise a repo for git
# ls -a to list all the files
# rm -rf .git ~ to remove git from the file gitbash is opened in
"""     
There is a staging area in between you and the github repo you are commiting to 
This staging area is knows as index or cache
we use git add file1 command to add the file 1 to staging area and then commit the changes using git commit
Keep in minf git add isn't only used to add a file into the staging area but it adds the current state the file is in it'll
delete the file from staging area if it was deleted from the main working directory.
You can also skip the staging area and commite directly
"""
# ech0 text > file_name will add the text to file but it works in write mode to make it work in read mode we use >>
# git commit -m "Some msg for later review" this is used to commit to git and -m here means msg which we add in inverted commas
# you can type git commit without -m for gitbash to open a file and there you can add a descriptive msg under 80 characters i guess
# git ls-files is the command used to get the files currently present in the staging area  
# git mv file1.js fiel2.js is the way to make git track all moving file and renaming the file
# echo logs/>.gitignore it ignores the content inside log folder for git
# you can write code .gitignore to open the gitignore folder in vs code and add our files in it 
# if a file was first commited and then added to gitignore then git will keep tracking them so we use git --cached -r file_name to remove them from staging area
# git ls-files show all the files present in our staging area 
# git status -s provides a short comprehension to the status of the current repo 
""" These are the status letters in git 
| Code | Meaning                                                         |
| ---- | --------------------------------------------------------------- |
| ??   | **Untracked file** (not staged, Git doesn’t know it yet)        |
| A    | **Added** (new file staged for commit)                          |
| M    | **Modified** (file content changed)                             |
| D    | **Deleted** (file removed)                                      |
| R    | **Renamed** (file was renamed)                                  |
| C    | **Copied** (file was copied from another)                       |
| U    | **Unmerged/conflict** (file has conflicts after a merge/rebase) |
"""
"""Branches are like pointers that point to a commit they kind of provide you a seperate safe place 
    away from the main branch to work on some feture or anything for chekcing or developing or testing 
    and later merge it in th emain branch"""
# git diff --staged is the command used to view all the changes in the index that haven't been commited yet!
# with git diff we can get all the changes that we did to the files that haven't been staged yet
# git branch lets us access all the branches that are present locally and there would a * in front of the branch we are currently on
# git branch new-feature creates a branch named new feature
# git checkout branch_name lets us switch to a branch and work on it rather than being in the main branch
# git branch -d branch_name lets you delete a branch in git if it's been merged but if it's not the use -D to delete it
# git branch -m old_name new_name is used to rename a branch 
# git branch -r shows all the remote branches on github and all
