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

11. Checking out a commit<br>
Cmd: git show <commit hash><br>
Notes: Author, date, lines added and deleted line of code, all is shown for the particular commit.<br>
<img width="615" height="390" alt="image" src="https://github.com/user-attachments/assets/2949707b-2dc7-48e5-aacc-b1ca0c4cb67a" /><br>


12. Reset<br>
Cmd: a. git reset --soft <commit hash> <br>
b. git reset --hard <commit hash> <br>
c. git reset <commit hash><br>
Notes: Reset means moving the HEAD pointer to a previous commit. Moreover, it is powerful when we want to squash many comits into one single commit(Check point for squashing). --soft reset is sprecually dobe when commit message is to be chnaged - herein the new commit's changes are saved in stage area (local git directory) and thus a new commit can be done along with git oush --force. Suppose commits are A->->B->C (HEAD) - then the directory becomes A->B (HEAD) and C commit is staged. Then once you modify the commit and suppose chnage it to C' and do git push -force the directory become - A->B->C' (HEAD). Simple reset or also termed as mixed reset required you to stage and commit chnages i.e. pointer moves to B and also the changes of commit C becone unstaged. git reset --hard comepletely deleted the C commit from local repo and moves HEAD pointer to previous commit i.e. B. However, the changes in commit C would be completely lost. New changes and new commit can be later done. A->B->C (HEAD) changes to A->B (HEAD) and later if a new commit comes then - A->B->D (HEAD). If chnages are pushed to github then the reset command will have to be followed by either git push --force or git pull --rebase. Else, only HEAD is moved and commits can be modified and then altogether pushed. To conclude reset is used only when we have not pushed code to remote repo/github. But ofc we can handle cases when code is pushed. However, especially in hard reset, a whole commit is lost.
<img width="759" height="342" alt="image" src="https://github.com/user-attachments/assets/415f2258-0616-4d11-b621-70ff57578e49" /><br>
<img width="536" height="333" alt="image" src="https://github.com/user-attachments/assets/fea446da-583a-4297-a427-ca712d4a750f" /><br>
<img width="810" height="763" alt="image" src="https://github.com/user-attachments/assets/0764531a-c028-4184-97d8-a926bf29dba6" /><br>
<img width="831" height="811" alt="image" src="https://github.com/user-attachments/assets/193d07d3-dc19-4b49-9402-35d04f833f6b" /><br>

13.Branching

14. Revert.<br>
Cmd: a. git revert <commit hash><br>
b. git revert -n <commit hash><br>
c. git revert --no-edit <commit hash><br>
d. git revert <commit hash old>..<commit hash new> OR git revert -n <commit hash of old commit>..HEAD <br> 
e. git revert -m <parent id> <commit hash of merge commit> <br>
Notes: Git revert is used when you want to have a specific commit version of a code without actually moving the HEAD pointer to the version. So if commits are A->B->C and you want to have commit B version of code then use revert and we get A->B->c-C'. This new commit C' is equivalent to B. It reverses all the changes made in code duing C commit. If commits are A->B->C->D and after D revert command to B is run then commit will be A->B->C->D->D' and this D' will be reverse of B. However, changes in C will sustain coz we wanted reversal to B. Merge conflicts can occur in this case and thus can be resolved maully in editor and then git revert --continue can be used futher to complete the revert process. Also, if you want to revert range of commit like D and C both reverting to B then use the c.) command that reverts all changes of D and C to B creating a new commit CD' (A->B->C->D->CD' where CD' is reverted version of B). -n attribute is to skip the git commit entirely. Revert happens but again after this revert command you have to manually do a git add and git commit and then git push commands to actually create a commit. --no-edit attribute is used when we want to skip the commit message. So by default the commit is done with commit message as "Revert <commit msg of commit which we revert>". If A->B->C and we reverted to B from C using --no-edit, "xyz" being commit message of B then we have A->B->C->C' with commit message of C' as "Revert xyz". -m is used when we have branches. If A->B are commits in main brnach and X->Y are commits in branch named pqr and the merge commit of main and pqr is M, then M has 2 parents B and Y. To revert to any one from M we have to use git show command onto M commit to get the number/ID of the intended parent. Suppose 1 is parent ID of A->B and 2 is of X->Y then git revert -m 1 <hashOfM> reverts it to B while  git revert -m 2 <hashOfM> reverts it to Y. 





15. Remove from git directory (local one).<br>
Cmd:git rm <filename><br>
Notes: Removes the file from the intitiated git working directory/tree. This file won't be staged/commited and thus not pushed to remote repo.<br>


16. Squashing
    
17.Stashing <br>
Cmd: a. git stash<br>
b. git stash list<br
c. git stash apply OR git stash apply stash@{n} (n is the ID of stash 1,2,3,4..etc)<br>
d. git stash drop OR git stash drop stash@{n} (n is ID of stash 1,2,3,4 ... etc) <br>
e. git stash pop<br>
f. git stash clear<br>
g. git stash show OR git stash show stash@{n} <br>
h. git stash -u <br>
i. git stash push -m "message here"<br>
j. git stash --keep-index
Notes: If you do not want to commit your code to directory but still save it for future then we use stash. Thus, stashing temporarily shelves your uncommitted changes. a. command stashed the curerent code i.e saves a snapshot of current code and now if you run git status, you will see nothing to commit/stage etc. So current all made chnages are "stashed" but not commited. Suppose you do this multiple times and you want to see list of all such stashes then we use b. command. To go to particular version of code that is stashed we use d. command (if stash id is not specified then the recent most stash is applied). d. id used to delete a recent stash or a specified stash without applying. e. command is used when we want to apply the stash as well as delete it. So as soon as shtash changes are applied, the stash is deleted. f. deleted all the stashes at once without applying any. g. command shows the summary of chnages stored inside recent stash or specified stash. h. command stashes all the untracked files along with the tracked and staged files. As in opposite, j. command stages only the untracked and unstaged files, staged ones containing the chnages are ignored. i. command just labels a stash with the given message. 
<img width="691" height="169" alt="image" src="https://github.com/user-attachments/assets/239226af-acd9-492b-9b07-e5a1a2586d6d" /><br>
<img width="661" height="225" alt="image" src="https://github.com/user-attachments/assets/803edca8-789f-4962-b67d-da6d23b6d271" /><br>
<img width="715" height="429" alt="image" src="https://github.com/user-attachments/assets/7dbf91c0-b031-407b-b5bc-e23a2ff0dd01" /><br>
<img width="575" height="205" alt="image" src="https://github.com/user-attachments/assets/739999cf-a84a-4fd2-a2dd-4f714fab146a" /><br>
<img width="521" height="156" alt="image" src="https://github.com/user-attachments/assets/85f5ba3c-9c6e-4fd7-aaa1-42e8386f69a9" /><br>
<img width="661" height="377" alt="image" src="https://github.com/user-attachments/assets/4d10a475-6ccc-4645-a91e-554871129ae4" /><br>
<img width="476" height="173" alt="image" src="https://github.com/user-attachments/assets/e9bd57fa-976f-4381-bb36-8ed7ae19afba" /><br>






THE 4 Rs in git
(Revert -> REvert to a commit or range of commit without losing the commit history
Rebase -> Forgot to pull before push or rebase the commit history.
Restore -> Remove from stating area. Unstage the changes
Reset-> Reset the commit history and go to desired commit. Also, squash multiple commits to one. History is deleted and prolly as per commands new commit is created)
