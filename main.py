import urllib.request,json


ui = input("Please Enter Your UserID:- ")
pa = input("Please Enter Your API KEY:- ")

class Openload:
    def info():
        url = ("https://api.openload.co/1/account/info?login={}&key={}".format(ui, pa))
        data = urllib.request.urlopen(url).read()
        jsondata = json.loads(data.decode("UTF-8"))
        if (jsondata["status"] == 200):

            print("----------------------------------------")
            email = (jsondata["result"]["email"])
            print("Email -: {}".format(email))
            print("----------------------------------------")
            SignUpDate = (jsondata["result"]["signup_at"])
            print("Signup at -: {}".format(SignUpDate))
            print("----------------------------------------")
            StorageUsed = (jsondata["result"]["storage_used"])
            print("Storage Used -: {}".format(StorageUsed))
            print("----------------------------------------")
            balance = (jsondata["result"]["balance"])
            print("Total Balance -: {}".format(balance))
            print("----------------------------------------")
        else:
            print("Please Check Your login And Key")

    def Download():
        fi=input("Please Enter File ID-: ")
        url = ("https://api.openload.co/1/file/dlticket?file={}&login={}&key={}".format(fi,ui, pa))
        data = urllib.request.urlopen(url).read()
        jsondata = json.loads(data.decode("UTF-8"))
        if (jsondata["status"] == 200):
            #print("----------------------------------------")
            ticket = (jsondata["result"]["ticket"])
            #print("Ticket -: {}".format(ticket))
            #print("----------------------------------------")
            Captcha = (jsondata["result"]["captcha_url"])
            print("Captcha -: {}".format(Captcha))
            ValidTill = (jsondata["result"]["valid_until"])
            print("ValidTill -: {}".format(ValidTill))
            print("----------------------------------------")

        captcha = input("Please Enter Captcha Code-: ")
        url=("https://api.openload.co/1/file/dl?file={}&ticket={}&captcha_response={}".format(fi,ticket,captcha))
        data = urllib.request.urlopen(url).read()
        jsondata = json.loads(data.decode("UTF-8"))
        print(url)
        if(jsondata["status"] == 200):
            print("----------------------------------------")
            url = (jsondata["result"]["url"])
            print("Downloading Url -: {}".format(url))
            print("----------------------------------------")
            Fname = (jsondata["result"]["name"])
            print("File Name -: {}".format(Fname))
            print("----------------------------------------")
            size = (jsondata["result"]["size"])
            print("File Size -: {}".format(size))
            print("----------------------------------------")
            content_type = (jsondata["result"]["content_type"])
            print("Content Type -: {}".format(content_type))
            print("----------------------------------------")
            upload_at = (jsondata["result"]["upload_at"])
            print("Uploaded At -: {}".format(upload_at))

        else:
            print("Please Enter right Captch Code")

    def upload():
        fileurl = str(input("Please Enter File URL To Upload To Openload-: "))
        urltoupload = ("https://api.openload.co/1/remotedl/add?login={}&key={}&url={}".format(ui, pa,fileurl))
        data = urllib.request.urlopen(urltoupload).read()
        jsondata = json.loads(data.decode("UTF-8"))

        if (jsondata["status"] == 200):
            print("----------------------------------------")
            FI = (jsondata["result"]["folderid"])
            print("Uploading file to Folder ID -: {}".format(FI))
            print("Your File is Uploading Please Wait a Moment:) ")
        else:
            print("Plese check your file url:( ")
            
    def remainFile():
        fileId=input("Please Enter File Id-: ")
        NewName=input("Please Enter New File name-: ")
        urltoupload = ("https://api.openload.co/1/file/rename?login={}&key={}&file={}&name={}".format(ui, pa,fileId,NewName))
        data = urllib.request.urlopen(urltoupload).read()
        jsondata = json.loads(data.decode("UTF-8"))
        if (jsondata["status"] == 200):
            print("Your File is Remain sucessfully :)")
        else:
            print("An Error Occure")
            
    def remainFolder():
        folderId=input("Please Enter Folder Id-: ")
        NewFName=input("Please Enter New Folder name-: ")
        urltoupload = ("https://api.openload.co/1/file/renamefolder?login={}&key={}&folder={}&name={}".format(ui, pa,folderId,NewFName))
        data = urllib.request.urlopen(urltoupload).read()
        jsondata = json.loads(data.decode("UTF-8"))
        if (jsondata["status"] == 200):
            print("Your File is Remain sucessfully :)")
        else:
            print("Please Check Folder ID")
            
    def DeleteFile():
        fileIdD=input("Please Enter File Id-: ")

        urltoDelete = ("https://api.openload.co/1/file/delete?login={}&key={}&file={}".format(ui, pa,fileIdD))
        data = urllib.request.urlopen(urltoDelete).read()
        jsondata = json.loads(data.decode("UTF-8"))
        if (jsondata["status"] == 200):
            print("Your File is Deleted sucessfully :)")
        else:
            print("An Error Occure")
   

    def ConvertFile():
        File= input("Please enter File ID Which you went to Convert:- ")
        ConvertURL=("https://api.openload.co/1/file/convert?login={}&key={}&file={}").format(ui,pa,File)
        data = urllib.request.urlopen(ConvertURL).read()
        jsondata = json.loads(data.decode("UTF-8"))
        print(jsondata)
        if (jsondata["status"] == 200):
            print("Convertion Started Sucessfullly :)")
        else:
            print("Please Check file ID")
 ol=Openload
    print("What You Went to do?")
    what=int(input("Click 1 To Information of Your Account\n"
                   "Click 2 To Download File \n"
                   "Click 3 To Remote Upload File \n"
                   "Click 4 to Remain Files \n"
                   "Click 5 To Remain Folder \n"
                   "Click 6 To Delete File \n"
                   "Click 7 to Convert File-:"))
    if(what==1):
        return ol.info()
    elif(what==2):
        return ol.Download()
    elif(what==3):
        return ol.upload()
    elif(what==4):
        return ol.remainFile()
    elif (what==5):
        return ol.remainFolder()
    elif (what == 6):
        return ol.DeleteFile()
    elif (what==7):
        return ol.ConvertFile()

    if __name__ == '__main__':main()


