import os,sys,ftplib,socket
import datetime
from logger import logging
#from wechat import wechat

FILENAME = "T"+datetime.datetime.now().strftime('%Y%m%d')+".gz"
CONST_BUFFER_SIZE = 8192

def connect(host, username, pwd,path):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(username, pwd)
        ftp.cwd(path)
        return ftp
    except socket.error, socket.gaierror:
        logging.error("FTP is unavailable")
        sys.exit(0)

def disconnect(ftp):
    ftp.quit()
    logging.info("ftp disconnect")

def upload(ftp,filename):
    path = os.path.abspath(".")
    print path
    f = open(path+"\\"+filename, "r")
    try:
        ftp.storbinary('STOR %s' % filename, f, CONST_BUFFER_SIZE)
        return True
    except ftplib.error_perm:
        logging.error("upload file error")
        return False

def download(ftp,filename):
    f = open(filename, "wb").write
    try:
        ftp.retrbinary("RETR %s" % filename, f, CONST_BUFFER_SIZE)
        return True
    except ftplib.error_proto:
        logging.error("download %s failed" %filename)
        return False

def checkfile(ftp,filename):
    ftp_f_list = ftp.nlst()
    if filename in ftp_f_list:
        logging.info("file exist")
        return True
    else:
        logging.error("no files")
        return False

def main():
    ftpsodex = connect("192.168.1.8", "ftpuser", "MeiyouMima123", "trans")
    logging.info("begin to download kfc_trans file")
    if checkfile(ftpsodex, FILENAME):
        pass
    else:
        disconnect(ftpsodex)
        sys.exit(0)
    if download(ftpsodex, FILENAME):
        pass
    else:
        logging.error("error")
        disconnect(ftpsodex)
        sys.exit(0)
    #disconnect(ftpsodex)
    logging.info("Download local file  finished")

    ftpremote = connect("192.168.1.8", "ftpuser", "MeiyouMima123", "blacklist")
    logging.info("begin to upload file to remote path")
    if upload(ftpremote, FILENAME):
        logging.info("upload trans file successful")
        pass
    else:
        logging.error("upload trans file failed")
        disconnect(ftpremote)
        sys.exit(0)
    disconnect(ftpremote)
    #wechat.sendwechat("johnnyjh")
    sys.exit(0)

if __name__ == '__main__':
    main()




