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
