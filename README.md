Created a directory named git-practice. Added some python code.

1. Initializing an empty git repository<br>
Cmd: git init<br>
<img width="813" height="305" alt="image" src="https://github.com/user-attachments/assets/8e29240b-23fb-4fd9-ba44-73f93094c8bb" /><br>

2. Staging the changes. <br>
Cmd: git add . <br>
Notes: Instead of . at the and specific files that are to be staged can be mentioned. The . specifies all the files/new files/ chnages are to be staged.<br>

3. Commiting the changes<br>
Cmd: git commit -m "This is the firs commit"<br>
Notes: The -m attribute stands for message. The message in quotes can be customized as per the changes made and saved in staging.<br>

<img width="722" height="101" alt="image" src="https://github.com/user-attachments/assets/4623ecd8-2ac6-4e87-bc70-2bc038794f99" /><br>

4. Stage and commit together<br>
Cmd: git commit -a -m "This is commit"<br>
Notes: he -a attribute helps to skip git add . command.<br>

5. Rename the current branch to main for github nomenclature.<br>
Cmd: git branch -M main<br>
Notes:  As per git, the name of the first branch is always master branch We can change it to match the github nomenclature.<br>
<img width="583" height="24" alt="image" src="https://github.com/user-attachments/assets/074719ab-938f-436a-b739-e003bd4d1a57" /><br>

6. Connect the local git repository to remote github repo.<br>
Cmd: git remote add origin https://github.com/user/repo.git<br>
Notes: "remote" is repository in github. "add" adds a new remote reference. "origin" is name of remote repository on github. URL is the actul location of repository.<br>
<img width="924" height="22" alt="image" src="https://github.com/user-attachments/assets/06d1e084-ee29-46f5-9b32-1e8391350fa3" /><br>

7. Pushing to the main branch of origin repo.<br>
Cmd: git push -u origin main<br>
Notes: -u atribute stands for -upstream. It creates a permanent link between the local git main branch and remote origin repo's main branch. Tells to track all the chnages from local to github repo's branch.<br>
<img width="683" height="221" alt="image" src="https://github.com/user-attachments/assets/ce2b8b65-16ad-40f4-ade5-3c8d7820c809" /><br>

8. Checking how many files are commmited/un-comittec staged etc. Basically checking ststus of files.<br>
Cmd: git status<br>
Notes: States files are chnaged and are not staged for committingor staged but not committed. Also states the files that are "untracked" i.e. these are newly created files/directories and are to be staged and committed.<br>
<img width="724" height="278" alt="image" src="https://github.com/user-attachments/assets/92a57701-3d49-4c0e-9ab8-44b16ed3b4a3" /><br>

9. Unstaging your changes<br>
Cmd: git restore --staged <filename> (git restore --staged app.py)<br>
Notes: We know git add . stages all files for commit. To unstage or remove the file from commiting we can unstage it using this command.<br>
<img width="688" height="621" alt="image" src="https://github.com/user-attachments/assets/d8e17e87-a9e0-4817-86a1-58d16bd0c11b" /><br>

9. Rebasing on main branch<br>
Cmd: a. git rebase origin main (does not work if the origin is not upstreamed)<br>
   b. git rebase origin/main<br>
   c. git pull --rebase origin main (pulls and rebases in one command)<br>
Notes: Suppose your commit history is A->B->C. Now on another person's laptop, the git tree looks like A->B (he has not pulled the C commit) and yet maked chnages with commit D. Now when he tries to push, fatal error is seen. To tackle this, we use git rebase. First he runs this command and then pull and then  runs git push. Rebase command takes all the commits that are not pulled (in this case commit C) and updated the local directory to include commit C. Then it puts the further commits onto it (in this case commit D). And then all the commits are pushed. Tree will look like A->B->C->D.  Commit D is rebased to start from commit C instead of commit B.<br>
<img width="692" height="180" alt="image" src="https://github.com/user-attachments/assets/784eaed0-080c-4b23-9679-d9df798f6329" /><br>
<img width="663" height="366" alt="image" src="https://github.com/user-attachments/assets/528b3ed0-894e-4aa1-9227-b2962050e402" /><br>


10. Checking logs <br>
Cmd: a. git log<br>
b. git log --oneline<br>
c. git log --stat
d. git log -p
d. git log --graph
Notes: Commit history is provided in reverse chronological order(last to first). Logs provide the info about author, date and time, commit message and hash(40 character SHA-1 ID) of the commit. --online attribute gives commit message and hash for all commits in one line each. --stat attribute will show changes , insertions and deletions during each commit. -p displays actual code changes for each commit. --graph displays a tree to understand commit history and branching and merges. <br>
<img width="1039" height="708" alt="image" src="https://github.com/user-attachments/assets/cca6dd66-e716-4942-93c5-5e96833276d2" /><br>
<img width="1066" height="761" alt="image" src="https://github.com/user-attachments/assets/80918c25-4fc5-4611-b3ae-ed36b6581cc8" /><br>
<img width="1116" height="706" alt="image" src="https://github.com/user-attachments/assets/9c7acc1e-9680-464b-9da5-637405bb47a2" /><br>






