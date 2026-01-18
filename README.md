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
Cmd: git restore --staged |filename| (git restore --staged app.py)<br>
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
d. git log --graph OR git log --graph --all
Notes: Commit history is provided in reverse chronological order(last to first). Logs provide the info about author, date and time, commit message and hash(40 character SHA-1 ID) of the commit. --online attribute gives commit message and hash for all commits in one line each. --stat attribute will show changes , insertions and deletions during each commit. -p displays actual code changes for each commit. --graph displays a tree to understand commit history and branching and merges. <br>
<img width="1039" height="708" alt="image" src="https://github.com/user-attachments/assets/cca6dd66-e716-4942-93c5-5e96833276d2" /><br>
<img width="1066" height="761" alt="image" src="https://github.com/user-attachments/assets/80918c25-4fc5-4611-b3ae-ed36b6581cc8" /><br>
<img width="1116" height="706" alt="image" src="https://github.com/user-attachments/assets/9c7acc1e-9680-464b-9da5-637405bb47a2" /><br>

11. Checking out a commit<br>
Cmd: git show |commit hash| <br>
Notes: Author, date, lines added and deleted line of code, all is shown for the particular commit.<br>
<img width="615" height="390" alt="image" src="https://github.com/user-attachments/assets/2949707b-2dc7-48e5-aacc-b1ca0c4cb67a" /><br>


12. Reset<br>
Cmd: a. git reset --soft |commit hash| <br>
b. git reset --hard |commit hash| <br>
c. git reset |commit hash|<br>
Notes: Reset means moving the HEAD pointer to a previous commit. Moreover, it is powerful when we want to squash many comits into one single commit(Check point for squashing). --soft reset is sprecually dobe when commit message is to be chnaged - herein the new commit's changes are saved in stage area (local git directory) and thus a new commit can be done along with git oush --force. Suppose commits are A->->B->C (HEAD) - then the directory becomes A->B (HEAD) and C commit is staged. Then once you modify the commit and suppose chnage it to C' and do git push -force the directory become - A->B->C' (HEAD). Simple reset or also termed as mixed reset required you to stage and commit chnages i.e. pointer moves to B and also the changes of commit C becone unstaged. git reset --hard comepletely deleted the C commit from local repo and moves HEAD pointer to previous commit i.e. B. However, the changes in commit C would be completely lost. New changes and new commit can be later done. A->B->C (HEAD) changes to A->B (HEAD) and later if a new commit comes then - A->B->D (HEAD). If chnages are pushed to github then the reset command will have to be followed by either git push --force or git pull --rebase. Else, only HEAD is moved and commits can be modified and then altogether pushed. To conclude reset is used only when we have not pushed code to remote repo/github. But ofc we can handle cases when code is pushed. However, especially in hard reset, a whole commit is lost.
<img width="759" height="342" alt="image" src="https://github.com/user-attachments/assets/415f2258-0616-4d11-b621-70ff57578e49" /><br>
<img width="536" height="333" alt="image" src="https://github.com/user-attachments/assets/fea446da-583a-4297-a427-ca712d4a750f" /><br>
<img width="810" height="763" alt="image" src="https://github.com/user-attachments/assets/0764531a-c028-4184-97d8-a926bf29dba6" /><br>
<img width="831" height="811" alt="image" src="https://github.com/user-attachments/assets/193d07d3-dc19-4b49-9402-35d04f833f6b" /><br>

13.Branching<br>
Cmd: a. git switch -c <branch name> OR git checkout -b |branch name| <b>(Used to create new branch and switch to it immmediately after creation.)</b> <br>
b. git push --set-upstream origin |branch name| <b> (Used to set the create branch upstream and push it to remote repo along with whatever changes made in it. Before this commit and add commands to be run.)</b> <br>
c. git checkout |branch_name| OR git switch |branch name| <b>(Used to switch to existing branch )</b><br>
d. git branch -m |current branch name| <b>(Used to rename current branch.) </b> <br>
e. git branch -m |old name| |new name| <b> (Used to rename a spacific branch)</b> <br>
f. git branch -a <b> (List out branches in remote repo) </b> <br>
g. git branch -d <b> (Deletes local branch )</b> <br>
h. git branch -D <b> (Deletes local branch forcefully) </b> <br>
i. git push origin --delete <branch name> <b>(Deletes branch from remote repo) </b><br>
Notes: Renaming branch only renames it in local repo, not the remote repo. To change in remote repo also push the current renamed branch to remote using <b>git push -u origin <nre name branch></b> Then, delete the old branch from remote repo with <b>git push origin --delete <old branch name> </b>. This is how renaming will work in remote repo.
<img width="835" height="622" alt="image" src="https://github.com/user-attachments/assets/48b1025b-8bb5-44e6-b229-048c8defe141" /><br>
<img width="1004" height="579" alt="image" src="https://github.com/user-attachments/assets/9b32d05d-e2d5-421a-9d8e-9c06fabce69b" /><br>
<img width="598" height="149" alt="image" src="https://github.com/user-attachments/assets/b66b00b1-50db-47b3-8f6c-78dbba3f1858" /><br>
<img width="827" height="727" alt="image" src="https://github.com/user-attachments/assets/e3d8a1d0-97b7-4942-a77f-5c0c6b5790cd" /><br>
<img width="487" height="154" alt="image" src="https://github.com/user-attachments/assets/22778ef0-fc31-4716-af37-c16adeb3b76f" /><br>

14. Merging the brnaches and rebasing in different branches.
Cmd: a. git switch |branch into which merging to be done| AND git merge |branch to be merged| OR git merge |branch to be merged| --ff-only<br>
b. git switch |branch into which merging to be done| AND git merge |branch to be merged| (Followed by git add .,git commit -m and git push)
c. git checkout |brach to be merged| AND git rebase |branck into which merging is done| AND git checkout |branch into which merging is done| AND git merge |branch to be merged|(Ex: feature branch to be merged in main then command flow is : git checkout feature -> git rebase main -> git checkout main -> git merge feature)
Notes: a. is called as fast forward merge and the a. command is done when branch to be merged, is predecessor of the brnach into which merging is to be done. Ex: main and feature are to be merged and feature is to be merged into main. Main is A->B->C and feature is X->Y while C being the ancestor of X and so after merge linear graph is formed: A->B->C->X->Y. Do git log --graph to understand this before and after merge. Moreover, git brancg -a command will still show a separate feature brnach, but code chnages will be seen as code from Y will be completely visible onto main branch. But suppose X does not have any immediate ancestor i.e. after branching out from commit C, there were more commits to main branch say D->E->F , then a simple merge and merge commit is created. This is the command b.. In this case, merge conflicts arise and are to be solved using the merge editor, and then do a simple <b>git merge --continue</b> Last but not least comes the rebasing of branches. When we have A->B-C->D as commits on main branch and X->Y on feature where the feature branched out of main from commit C and we want to merge feature into main without a merge commit thne we first rebase the feature branch to make D as X commit's ancestor and then we do fast forward merge. After rebasing it becomes A->B-C->D->X'->Y' and where X' and Y' are still at feature branch only and then after fast forward merge linearity is achieved. If there is merge conflict while rebasing then resolev in editor , then do a manual commit and then <b> git rebase --continue </b> and then checkout to main branch and merge feature branch. New commit willot be visible coz fast forward merge does not create any commit. But a linear gharph i seen
(Fast forward merge):
<img width="772" height="563" alt="image" src="https://github.com/user-attachments/assets/0e2f67c4-c909-4382-994b-3d5c9d0c5c85" /><br>
<img width="636" height="117" alt="image" src="https://github.com/user-attachments/assets/d5fb7ad7-286c-4c55-aa79-9b1e8e8b6501" /><br>
<img width="646" height="107" alt="image" src="https://github.com/user-attachments/assets/613a5c7f-8c3d-4c8c-a94d-f05629ced211" /><br>
<img width="944" height="667" alt="image" src="https://github.com/user-attachments/assets/44b811fa-ea98-4b5b-ab61-d515982d4031" /><br>
(Simple merge)
<img width="860" height="535" alt="image" src="https://github.com/user-attachments/assets/d899d864-a446-4996-8a67-5a0e0eddf7c4" /><br>
<img width="881" height="221" alt="image" src="https://github.com/user-attachments/assets/68b6fde1-c333-4327-8417-ad80075282a2" /><br>
Final graph:
<img width="881" height="754" alt="image" src="https://github.com/user-attachments/assets/326eca23-f7f3-465a-af79-b117c5c15193" /><br>
Rebasing and then fastforward merge.
<img width="920" height="882" alt="image" src="https://github.com/user-attachments/assets/abe2509e-0ce8-4649-8da5-e12e75190610" /><br>
<img width="751" height="268" alt="image" src="https://github.com/user-attachments/assets/1d49300f-ce03-4c89-a008-784943faf775" /><br>
<img width="799" height="357" alt="image" src="https://github.com/user-attachments/assets/1aba1e60-8414-4116-bfb0-cf2f1cb6b8b3" /><br>
<img width="716" height="274" alt="image" src="https://github.com/user-attachments/assets/05df948e-c4de-4483-b569-ff34884e8f64" /><br>


15.  Revert.<br>
Cmd: a. git revert |commit hash|<br>
b. git revert -n |commit hash|<br>
c. git revert --no-edit |commit hash| AND git commit --allow-empty -m "Revert 675af5c (no-op after conflict resolution)"<br>
d. git revert |commit hash old|..|commit hash new| OR git revert -n |commit hash of old commit|..HEAD <br> 
e. git revert -m |parent id| |commit hash of merge commit| <br>
Notes: Git revert is used when you want to have a specific commit version of a code without actually moving the HEAD pointer to the version. So if commits are A->B->C and you want to have commit B version of code then use revert and we get A->B->c-C'. This new commit C' is equivalent to B. It reverses all the changes made in code duing C commit. If commits are A->B->C->D and after D revert command to B is run then commit will be A->B->C->D->D' and this D' will be reverse of B. However, changes in C will sustain coz we wanted reversal to B. Merge conflicts can occur in this case and thus can be resolved maully in editor and then git revert --continue can be used futher to complete the revert process. Also, if you want to revert range of commit like D and C both reverting to B then use the c.) command that reverts all changes of D and C to B creating a new commit CD' (A->B->C->D->CD' where CD' is reverted version of B). -n attribute is to skip the git commit entirely. Revert happens but again after this revert command you have to manually do a git add and git commit and then git push commands to actually create a commit. --no-edit attribute is used when we want to skip the commit message. So by default the commit is done with commit message as "Revert |commit msg of commit which we revert|". If A->B->C and we reverted to B from C using --no-edit, "xyz" being commit message of B then we have A->B->C->C' with commit message of C' as "Revert xyz". This achieved by the second --alow-empty attribute command. -m is used when we have branches. If A->B are commits in main brnach and X->Y are commits in branch named pqr and the merge commit of main and pqr is M, then M has 2 parents B and Y. To revert to any one from M we have to use git show command onto M commit to get the number/ID of the intended parent. Look gor line Merge: |commitHash1| |commitHash2| where the commitHash1 will be of the parent 1 ie. the branch you were on while merge while commitHash2 is is the commit hash of the branch which was merged onto commitHash1 branch. So, if you merged branch named feature into main then commitHash1 id of main and commitHsh2 is of feature branch and thus parent ID of main becomes 1 and that of feature becomes 2. In our case now, suppose 1 is parent ID of A->B and 2 is of X->Y then git revert -m 1 <hashOfM> reverts it to B while  git revert -m 2 <hashOfM> reverts it to Y. <b> Note! Safest attribute of revert  to use is -n. Coz after this you can do a commit yourself</b>
(This is the initial 4 commits (Revert A,B,C,D)):<br>
<img width="885" height="618" alt="image" src="https://github.com/user-attachments/assets/6a28b332-cd6c-4e1b-8d7d-8f64d96bfba1" /><br>
<img width="873" height="253" alt="image" src="https://github.com/user-attachments/assets/90730aa0-b2ef-4f7d-a42e-83cdc80285f2" /><br>
--no-edit revert:<br>
<img width="896" height="727" alt="image" src="https://github.com/user-attachments/assets/7ef508b9-3677-49b7-a592-f070723c7fb0" /><br>
(After this do git commit --allow-empty -m "Revert msg")<br>
<img width="715" height="541" alt="image" src="https://github.com/user-attachments/assets/fd649536-0a96-4e4e-965a-6976be290312" /><br>
Range revert:<br>
<img width="757" height="780" alt="image" src="https://github.com/user-attachments/assets/886ecfa9-5e9e-455a-be8f-21082571f424" /><br>
<img width="1141" height="324" alt="image" src="https://github.com/user-attachments/assets/cf4a1f5a-53c7-4097-95c8-868e8daf350b" /><br>
<img width="881" height="917" alt="image" src="https://github.com/user-attachments/assets/a110dbe4-8505-4e80-a6a3-59c7826b8e03" /><br>
Merge revert:<br>
<img width="909" height="666" alt="image" src="https://github.com/user-attachments/assets/1babe0ed-673c-4b9d-93d1-715b35dfce52" /><br>
<img width="988" height="301" alt="image" src="https://github.com/user-attachments/assets/92c5b72c-8acd-4aa4-8c26-79306413a488" /><br>
<img width="889" height="274" alt="image" src="https://github.com/user-attachments/assets/4a7f22df-3db4-40d5-a3b5-22945da90e8c" /><br>





16. Remove from git directory (local one).<br>
Cmd:git rm |filename|<br>
Notes: Removes the file from the intitiated git working directory/tree. This file won't be staged/commited and thus not pushed to remote repo.<br>


17. Squashing and interactive rebasing, and fixup<br>
Cmd: a. git rebase -i |commitHash| <br>
b. git checkout |branch in into whoch merge will happen| AND git merge --squash |branch to be merged|<br>
Notes: Squashing means to combine one or more commits into one. Helps to curb number of commits in limit. This is achieved by rebasing and that too in interactive mode. An older commit squashes the further commits into it. Suppose you have A->B->C->D->E and you want to squash all commits into B then use a. command and an interactive rebase opens an editor and now chnage all the "pick" words to "squash" for the commits you want to squash into B. Then save and exit. Then enter the combined commit message in another editor already open and then save and exit it.Trick here is when you want to squash into B , you have to give the commit hash of commit A while entering the interactvive rebase : git rebase - i |commitHashOfA| and then the rest 4 B,C,D,E commits will appear in the editor where you squash C,D,E into E and so chnage the "pick" to "squash" for only C,D,E commits not the B. B remains "pick". You can also squash and mearge a branch into another. b. command is used. However, here merge commit is not created, so log does not show it. In fixup, instead of "squash" you write "fixup" in the interactive editor file opened after command <b>git rebase -i |commitHash|</b>. Fixup combines the commits but it does not give a new commit message to combined commits, but the parent's commit message is carried forward. Ex: We have A->B-C->D->E commits and we give command git rebase -i |commitHashOfA| then in editor we will have commits with pick word prefixed to commit B,C,D,E. We chnage "pick" to "fixup" for C,D,E commits. Once we close and exit then the ommit message of B will be commit message after fixup.
Rebase and squash:<br>
<img width="791" height="433" alt="image" src="https://github.com/user-attachments/assets/26ecf177-1a46-4bad-b825-f4861de8acd4" /><br>
<img width="844" height="148" alt="image" src="https://github.com/user-attachments/assets/853ada08-d8d7-429f-bb0d-9f2a66108e0e" /><br>
<img width="799" height="764" alt="image" src="https://github.com/user-attachments/assets/09ba46cb-65b1-40ed-8dec-bf34829bd953" /><br>
<img width="803" height="761" alt="image" src="https://github.com/user-attachments/assets/1fd9b5de-3edf-48a2-a2cf-0429388bd0e5" /><br>
<img width="642" height="157" alt="image" src="https://github.com/user-attachments/assets/ae4b586a-d61b-46e0-8dc0-85bc4b75569f" /><br>
<img width="729" height="151" alt="image" src="https://github.com/user-attachments/assets/03a1585e-19d9-45b9-9944-cdc6d6dd0793" /><br>
Squash branch:<br>
<img width="843" height="465" alt="image" src="https://github.com/user-attachments/assets/c018610c-8158-4730-92a2-05acdfa3791e" /><br>
Fixup:<br>
<img width="732" height="144" alt="image" src="https://github.com/user-attachments/assets/e656fb65-fc49-4b08-8553-78cb7bda10fd" /><br>
<img width="916" height="744" alt="image" src="https://github.com/user-attachments/assets/7351a599-adc4-4fac-bf5a-15050cad549a" /><br>
<img width="702" height="180" alt="image" src="https://github.com/user-attachments/assets/0ab8c9a4-156e-4033-8098-70d80f69a1c7" /><br>



18.Stashing <br>
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



19. Common git config commands:<br>
a. git config --global --list <b>To check the global git config</b><br>
b. git config --global user.name |your username| <b> To set the username globally for git onto machine</b><br>
c. git conig --global user.name <b> If you have already set user name and want to check it what it is then use this</b><br>
d. git config --global user.email |your email| <b>To set user email globally for git onto machine </b><br>
e. git config --global user.email <b>If you have already set user email and want to check what it is</b><br>
f.git config --global core.editor |editor name like vim/nano| <b>To set the editor for git. Useful in commands like interactive rebase</b><br>
g. git config --global color.ui auto <b>To enable coloured UI for git output</b><br>
h. git config --global alias.|shortcut| "git command for which shortform stands" <b> Useful to create shortcuts for very long commands.Ex: git config --global alias.lg "git log --graph --oneline --all". So now you have to put <i>git lg</i> when ever you want log in graph format or want to basically run git log --graph --oneline --all command.


THE 4 Rs in git
(Revert -> REvert to a commit or range of commit without losing the commit history
Rebase -> Forgot to pull before push or rebase the commit history.
Restore -> Remove from stating area. Unstage the changes
Reset-> Reset the commit history and go to desired commit. Also, squash multiple commits to one. History is deleted and prolly as per commands new commit is created)
