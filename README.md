# python
python code practice and exercises!!!

------

I did first commit and while i did push from cmd it says you have shomething from github that remained, so i checked and found you there,
then i did pull and then pusj things!

-----

I have <python> folder in that i have practice code files...

Let note some commands here: inside <python>
1. git init --->IT WILL INITIALIZE EMPTY GIT REPOSITORY
2. git status --->IT WILL SAY: ON BRANCH MAIN, NO COMMITS, AND UNTRACKED FILES LISTS THERE
3. git add . --->IT WILL ADD UNTRACKED FILES ON CURRENT BRANCH
4. git commit -m "message we add" --->IT WILL SAVES LOCALLYYY

5. git remote add origin https://github.com/im-JayChaudhary/python.git --->GIT IS CONNECTED WITH GITHUB REPO,,,"ORIGIN" IS NICHNAME FOR THAT
6. git remove -v --->YOU CAN SEE THAT ORIGIN THING

7. git pull origin main --->INCASE UNTRACED FILES CREATED ON GITHUB SEPERATLY THAT PULL AND MERGE

8. git push -u origin main --->FIRST PUSH OF THE NEW BRANCH, HERE IT IS MAIN

9. git checkout -b new-branch --->TO CREATE NEW BRANCH
10. git push -u origin new-branch --->FIRST PUSH OF THE NEW-BRANCH "-U" IS LIKE SAYS RELATION FIRST TIME

11. git push --->LATER PUSH AFTER
12. git pull --->GET LATEST CHANGES, DOWNLOAD FROM GITHUB

13. git branch --->IT WILL LISTS ALL BRANCH AND SHOWS CURRENT ONE WITH DIFF COLOR
14. git branch -M new-name --->IT WILL RENAME THE CURRENT BRANCH WITH NEW-NAME

15. git checkout main --->SWITCHED FROM NEW-NAME BRANCH TO MAIN BRANCH
16. git merge new-name --->NOW MAIN ALSO HAVE NEW-NAME BRANCH CONTENT AS WELL

17. git branch -d new-name --->IT WILL DELETES THAT BRANCH FROM GIT, LOCALLY
18. git push origin --delete new-name --->IT WILL DELETES ALSO FROM GITHUB, REMOTELY

19. git ls-tree -r --name-only main --->SEE ALL FILES IN MAIN BRANCH
20. git ls-tree -r --name-only new-branch --->SEE FILES PRESENT INSIDE OTHER BRANCH
21. git diff --name-only main new-branch --->DIFFERENT FILE AMONG THAT BOTH BRANCHES


