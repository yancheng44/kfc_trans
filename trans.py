
import os,sys,ftplib,socket
import datetime
from logger import logging
#from wechat import wechat

FILENAME = "T"+datetime.datetime.now().strftime('%Y%m%d')+"gz"
CONST_BUFFER_SIZE = 8192

def connect(host, username, pwd):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(username, pwd)
        return ftp
    except socket.error, socket.gaierror:
        logging.error("FTP is unavailable")
        sys.exit(0)

def disconnect(ftp):
    ftp.quit()
    logging.info("ftp disconnect")

def upload(ftp,filepath):
    f = open(filepath, "rb")
    file_name = os.path.split(filepath)[-1]
    try:
        ftp.storbinary('STOR %s' % file_name, f, CONST_BUFFER_SIZE)
    except ftplib.error_perm:
        logging.error("upload file error")
    logging.info("upload file success")

def download(ftp,filename):
    f = open(filename,"wb").write
    try:
        ftp.retrbinary("RETR %s" % filename, f, CONST_BUFFER_SIZE)
    except ftplib.error_proto:
        logging.error("download %s failed"+filename)
    logging.info("download %s success" +filename)

def checkfile(ftp,filename):
    ftp_f_list = ftp.nlst()
    if filename in ftp_f_list:
        logging.info("file exzit")
        return True
    else:
        logging.error("no files")
        return False

def main():
    ftplocal = connect("58.247.98.30", "ftpuser", "MeiyouMima123")
    logging.info("begin to download file to local path")
    if checkfile(ftplocal, FILENAME):
        pass
    else:
        disconnect(ftplocal)
        sys.exit(0)
    if download(ftplocal, FILENAME):
        pass
    else:
        sys.exit(0)
    disconnect(ftplocal)
    logging.info("Download local file  finished")

    ftpremote = connect("58.247.98.30", "ftpuser", "MeiyouMima123")
    logging.info("begin to upload file to remote path")
    if upload(ftpremote, FILENAME):
        pass
    else:
        sys.exit(0)
    disconnect(ftpremote)
    #wechat.sendwechat("johnnyjh")
    sys.exit(0)

if __name__ == '__main__':
    main()




