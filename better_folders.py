import os

# Function to rename multiple files


def main():
    i = 0

    for folder in os.listdir("./"):

        truthy = '.' in folder

        if(truthy != True):

            if i < 10:
                updatedFolderName = '0{}-{}'.format(str(i), folder)
            else:
                updatedFolderName = '{}-{}'.format(str(i), folder)

            os.rename(folder, updatedFolderName)
            i += 1


main()
