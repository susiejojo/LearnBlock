import subprocess as cmd

cp = cmd.run("git init", check=True, shell=True)
repo = input("Enter link to repository to push commits to:\n")
cp = cmd.run("git remote add origin {repo}", check=True, shell=True)
cp = cmd.run("git add <path_to_working_dir>/code.py", check=True, shell=True)
#print(cp)

def commit():
	response = input("Do you want to use the default message for this commit?([y]/n)\n")
	message = "update the repository"

	if response.startswith('n'):
	    message = input("What message do you want?\n")

	cp = cmd.run(f"git commit -m '{message}'", check=True, shell=True)
	cp = cmd.run("git push -u origin master -f", check=True, shell=True)
	return