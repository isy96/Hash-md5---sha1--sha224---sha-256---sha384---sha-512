This is a simple Python-based hash cracking tool that uses a wordlist to find the original value of a given hash

It works by:

Reading each word from a wordlist

Hashing it with the specified algorithm

Comparing the generated hash with the target hash

Stopping when a match is found

Supported Hash Types

  (md5) (sha1) (sha224) (sha256) (sha384) (sha512)

hash-Crack.py → The main Python script

wordlist.txt → A list of possible passwords (one per line)

saveHashes.txt → A file where cracked hashes are saved automatically

Option	  Description
  -h	    The hash value you want to crack.
  -t	    The hashing algorithm (md5, sha1, sha224, sha256, sha384, sha512).
  -w	    Path to your wordlist file.
  -n	    Enables brute force mode with numbers (not implemented yet in this version).
  -i	    Show help menu.
