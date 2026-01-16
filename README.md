Created a directory named git-practice. Added some python code.

1. Initializing an empty git repository
Cmd: git init
<img width="813" height="305" alt="image" src="https://github.com/user-attachments/assets/8e29240b-23fb-4fd9-ba44-73f93094c8bb" />


2. Staging the changes. 
Cmd: git add .
Notes: Instead of . at the and specific files that are to be staged can be mentioned. The . specifies all the files/new files/ chnages are to be staged.

3. Commiting the changes
Cmd: git commit -m "This is the firs commit"
Notes: The -m attribute stands for message. The message in quotes can be customized as per the changes made and saved in staging.

<img width="722" height="101" alt="image" src="https://github.com/user-attachments/assets/4623ecd8-2ac6-4e87-bc70-2bc038794f99" />

4. Stage and commit together
Cmd: git commit -a -m "This is commit"
Notes: he -a attribute helps to skip git add . command.

5. Rename the current branch to main for github nomenclature.
Cmd: git branch -M main
Notes:  As per git, the name of the first branch is always master branch We can change it to match the github nomenclature.
<img width="583" height="24" alt="image" src="https://github.com/user-attachments/assets/074719ab-938f-436a-b739-e003bd4d1a57" />

6. Connect the local git repository to remote github repo.
Cmd: git remote add origin https://github.com/user/repo.git
Notes: "remote" is repository in github. "add" adds a new remote reference. "origin" is name of remote repository on github. URL is the actul location of repository.
<img width="924" height="22" alt="image" src="https://github.com/user-attachments/assets/06d1e084-ee29-46f5-9b32-1e8391350fa3" />


7. Pushing to the main branch of origin repo.
Cmd: git push -u origin main
Notes: -u atribute stands for -upstream. It creates a permanent link between the local git main branch and remote origin repo's main branch. Tells to track all the chnages from local to github repo's branch.
<img width="683" height="221" alt="image" src="https://github.com/user-attachments/assets/ce2b8b65-16ad-40f4-ade5-3c8d7820c809" />
