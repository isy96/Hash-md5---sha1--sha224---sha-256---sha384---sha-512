#!/usr/bin/python

import sys, os , time
import getopt, hashlib

class hashCracking:
    def hashCrackFromWordlist(self, userHash, hashType, wordlist="wordlist.txt", bruteforce=True):
        start = time.time()
        solved = False
        self.lineCount = 0
        if "md5" in hashType:
            h = hashlib.md5
        elif "sha1" in hashType:
            h = hashlib.sha1
        elif "sha224" in hashType:
            h = hashlib.sha224
        elif "sha256" in hashType:
            h = hashlib.sha256
        elif "sha384" in hashType:
            h = hashlib.sha384
        elif "sha512" in hashType:
            h = hashlib.sha512
        else:
            print("[-] Is \'%s\' a supported hash type?" % hashType)   
            exit()

        if bruteforce ==True:
            with open(wordlist, "r") as infile:
                for line in infile:
                    line = line.strip()
                    encodeline=str.encode(line)
                    lineHash = h(encodeline).hexdigest()

                    if str(lineHash) == str(userHash.lower()):
                        end = time.time()
                        print("\n[+] Hash is: %s" % line) 
                        print("\n[+] Words tried: %s" % self.lineCount)
                        print("\n[+] Time: %s secounds" % round((end - start), 2))
                        savedHashFile = open('saveHashes.txt' , 'a+')
                        savedHashFile.write("{}  :  {}\n".format(line,lineHash) )
                        solved = True
                        exit()
                    else:
                        self.lineCount = self.lineCount +1

def info():
    print("Information: ")
    print("Options: ")    
    print("[*] (-h) Hash")
    print("[*] (-t) Type [Hash Function Type]")
    print("[*] (-w) wordlist file path")
    print("[*] (-n) Number bruteforce")
    print("[*] (-i) Help")
    print("\t Example:")
    print("\t\t python3 hash-Crack.py -h <Hash> -t md5 -w Wordlist.txt")
    print("[*] Supported Hashes:")
    print("[>] md5, sha1,sha224 ,sha256, sha384, sha512")

    
def main(argv):
    print(f"""  #########################################
#     MRajeh- Hash Cracker              #
#     Version 0.1"                      #
#########################################
         """
         )

    hashType = None
    userHash = None
    wordlist = None
    numberBruteForce = False

    try:
        opts, args = getopt.getopt(argv, "ih:t:w:n",["ifile=","ofile="])
        # -h -t
    except getopt.GetoptError:
        print("\t\t python3 hash-Crack.py -h <Hash> -t md5 -w wordlist.txt")
        print("[*] (-i) Help")
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-i':
            info()
            sys.exit() 
        elif opt in ("-h", "--hash"):
            userHash = arg.strip().lower()
        elif opt in ("-t", "--type"):
            hashType = arg.strip().lower()
        elif opt in ("-w","--wordlist"):
            wordlist = arg
        elif opt in ("-n" , "--number"):
            numberBruteForce = True
    
    if not(hashType and userHash):
        print("\t\t python3 hash-Crack.py -h <Hash> -t md5 -w Wordlist.txt")
        print("[*] (-i) Help")
        sys.exit(1)
    try:
        h = hashCracking()
        h.hashCrackFromWordlist(userHash , hashType)
    except:
        print("\n [-] Hashg not Cracked.")
        print("\n [*] Reached end of wordlist.")
        print("\n [-] Try another wordlist.")



if __name__ == "__main__":
    main(sys.argv[1:])