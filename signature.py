import os
import binascii
import shutil
import sys

def file_Load(path_dir):
    file_list = os.listdir(path_dir)
    print("\n[*] File Load ...")
    file = []
    for i in file_list:
        print("[+] File Name >>> "+i)
        file.append(i)
    return file

def search(file_li, path):
    print("\n[*] File Signature Searching ...")
    signature = []
    for j in file_li:
        file_r = open(path+"\\"+j, "rb")
        file_h = file_r.read(2)
        magic = binascii.b2a_hex(file_h).decode("utf-8")
        #magic = file_h.encode("hex")
        print("[+] File Name: "+j+"\tMagic Number: "+magic)
        signature.append(magic)
        if magic == "ffd8":
            print("\n=============== JPEG Signature Detection ===============")
            src = path+"\\"+j
            dst = path+"\\"+j+".jpeg"
            shutil.copy(src, dst)
            print("[*] File Copy ...")
            print("[+] File Path: "+dst)
            file_r.close()
            break
        file_r.close()
    return signature

def main():
    print("=============== JPEG Signature analysis ===============")
    print(r"[-] Sample >>> C:\Users\parj2\Downloads\Day3\Datasets\05.FileSignatureAnalysis\File Signature Examples")
    path = input("[-] File Path >>> ")
    file_li = file_Load(path)
    search(file_li, path)
    sys.exit()

if __name__ == '__main__':
    main()