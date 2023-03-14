# This is a sample Python script.
import os
import shutil
from smb.SMBConnection import SMBConnection
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

userID = 'Taehoon'
userPW = '927200trtr'
client_machine_name = 'LIVA_EDGE'
server_ip = '192.168.0.4'
domain_name = '3DPTHNET'
remote_server_name = "DESKTOP-3DPSWTH"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def walk_path(path, sharedfiles, connection):
    print('Walking path'+path)
    for sharefile in sharedfiles:
        if sharefile.filename != '.' and sharefile.filename != '..':
            parentPath = path
            if not parentPath.endswith('/'):
                parentPath += '/'

            if sharefile.isDirectory:
                walk_path(parentPath + sharefile.filename)
                print("Deleting folder")
                connection.deleteDirectory('smbshare')


# def copyDir(conn, dirName):



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    os.chdir("/home/taehoon/HBNU_PBF3DP_Data")
    dir_path = os.getcwd()
    if not os.path.exists("20230314_1451_M160"):
        os.mkdir("20230314_1451_M160")
    print(dir_path)

    connection = SMBConnection(username=userID, password=userPW, my_name=client_machine_name, remote_name=remote_server_name, domain=domain_name)
    connection.connect(server_ip)
    shares = connection.listShares()

    for share in shares:
        print(share.name)


    dir = connection.listPath('smbShare','/')
    for e in dir:
        if not e.isDirectory:
            filepath = os.path.join(dir_path, e.filename)
            with open(filepath, 'wb') as f:
                connection.retrieveFile('smbShare', e.filename, f)
        # elif e.filename not in ['.','..']:
        #     copyDir(connection, os.path.join())



    sharedfiles = connection.listPath('smbShare', '/')
    # walk_path('/', sharedfiles)
    for sharefile in sharedfiles:
        print(sharefile.filename)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
