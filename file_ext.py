filename=input("Enter File Name :")
n=len(filename)
for i in range(0,n):
    if filename[i]==".":
        break
extension=filename[i:n]
if ".py" in extension :
    print("PYTHON FILE")
elif ".c" in extension :
    print("C")
elif ".html" in extension :
    print("HTML FILE")
elif ".pdf" in extension :
    print("PDF FILE")
elif ".php" in extension :
    print("PHP FILE")
    

#Alot of file extensions exist but i have used some of them for this code
