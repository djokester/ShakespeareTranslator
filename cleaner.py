import os
 
 
files = os.listdir()
files.remove('newscraper.py')
files.remove('LICENSE')
files.remove('README.md')
files.remove('.git')
files.remove('.gitignore')
files.remove('cleaner.py')
a=files
splitup = []
print(a)
for folder in a:
	files_in_folder=os.listdir(str(folder))
	for file1 in files_in_folder:
		f=open("/home/vaibhav/ShakespeareTranslator/"+str(folder)+"/"+str(file1))
		text=f.read()
		text=text.split("#LBSFORGOLD")
		if len(text)>2:
			splitup.append(text[:2])
		else: 
			splitup.append(text)

clean = [i for i in splitup if len(i)>2]
print(len(clean))
print(len(splitup))