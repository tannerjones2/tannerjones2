import os
def main():

    # Create directory
    dirName1 = '1.Documentation'
    dirName2 = '2.Findings'
    dirName3 = '3.Data'

    #Create Documentation Dirctory
    dirname1 = '1.Documentation'
    try:
        # Create target Directory
        os.makedirs(dirName1)
        print("Directory " , dirName1 ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName1 ,  " already exists")

    #Create Findings Directory
    dirName2 = "2.Findings"

    try:
        # Create target Directory
        os.makedirs(dirName2)
        print("Directory " , dirName2 ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName2 ,  " already exists")

    #Create Data Directory
    dirName3 = "3.Data"

    # Create target Directory if don't exist DOCUMENATION
    if not os.path.exists(dirName1):
        os.makedirs(dirName1)
        print("Directory " , dirName1 ,  " Created ")
    else:
        print("Directory " , dirName1 ,  " already exists")

    dirName1 = '1.Documentation/a. Customer Info'

    # Create target Directory if don't exist DOCUMENATION
    if not os.path.exists(dirName1):
        os.makedirs(dirName1)
        print("Directory " , dirName1 ,  " Created ")
    else:
        print("Directory " , dirName1 ,  " already exists")

    dirName1 = '1.Documentation/b. Reports'

###############################################################################

    # Create target Directory if don't exist FINDINGS
    if not os.path.exists(dirName2):
        os.makedirs(dirName2)
        print("Directory " , dirName2 ,  " Created ")
    else:
        print("Directory " , dirName2 ,  " already exists")

    dirName2 = '2.Findings/a. External'

    # Create target Directory if don't exist FINDINGS
    if not os.path.exists(dirName2):
        os.makedirs(dirName2)
        print("Directory " , dirName2 ,  " Created ")
    else:
        print("Directory " , dirName2 ,  " already exists")

    dirName2 = '2.Findings/b. Internal'

    # Create target Directory if don't exist FINDINGS
    if not os.path.exists(dirName2):
        os.makedirs(dirName2)
        print("Directory " , dirName2 ,  " Created ")
    else:
        print("Directory " , dirName2 ,  " already exists")

    dirName2 = '2.Findings/c. Phishing'

###############################################################################

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/a. Database'

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/b. Phishing'

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/c. Network Mapping'

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/d. Penetration Test'

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/e. Vulnerability Scanning'

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/f. Web App'

###############################################################################
    # Create target Directory if don't exist in DATA/Phishing Subfolders
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/b. Phishing/i. Templates'

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/b. Phishing/ii. Payloads'

###############################################################################
    # Create target Directory if don't exist in DATA/Network Mapping Subfolders
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/c. Network Mapping/i. External'

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/c. Network Mapping/ii. Internal'

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/c. Network Mapping/i. External/1. Nmap'

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/c. Network Mapping/i. External/2. Eyesitness'

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/c. Network Mapping/ii. Internal/1. Nmap'

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/c. Network Mapping/ii. Internal/2. Eyesitness'

###############################################################################
# Create target Directory if don't exist in DATA/Vulnerability Test Subfolders
    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/e. Vulnerability Scanning/i. External/1. Nessus'

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/e. Vulnerability Scanning/ii. Internal/1. Nessus'

###############################################################################
# Create target Directory if don't exist in DATA/Web App Subfolders
    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/f. Web App/i. Burp/'

    # Create target Directory if don't exist in DATA
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

    dirName3 = '3.Data/f. Web App/ii. Nikto/'

    # Create target directory & all intermediate directories if don't exists
    try:
        os.makedirs(dirName1)
        print("Directory " , dirName1 ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName1 ,  " already exists")

    # Create target directory & all intermediate directories if don't exists
    if not os.path.exists(dirName2):
        os.makedirs(dirName2)
        print("Directory " , dirName2 ,  " Created ")
    else:
        print("Directory " , dirName2 ,  " already exists")

    # Create target directory & all intermediate directories if don't exists
    if not os.path.exists(dirName3):
        os.makedirs(dirName3)
        print("Directory " , dirName3 ,  " Created ")
    else:
        print("Directory " , dirName3 ,  " already exists")

if __name__ == '__main__':
    main()
