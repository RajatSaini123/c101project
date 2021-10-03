import os
import dropbox

from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token        

    def upload_file(self, file_from, file_to):  
        dbx = dropbox.Dropbox(self.access_token)
        # enumerate local files recursively
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                localpath= os.path.join(root,filename)
                relativepath=os,path.relpath(localpath,file_from)
                dropboxpath=ospath.join(file_to,relativepath)

        with open(localpath, 'rb') as f:        
            dbx.files_upload(f.read(), dropboxpath,mode=WriteMode('overwrite')) 

def main():
    access_token = 'aJJji2Q1k2cAAAAAAAAAAcDb91EH_PEG6d341AkgoulQ77aVySe8qKfqvGSDM07p'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer: ")
    file_to = input("enter the full path to upload to dropbox: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved")


main()