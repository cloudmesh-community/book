#! /bin/sh
rm -f *.txt

# Creating a file with data
echo "Big Data is the future." > file.txt

# Create the pem
openssl rsa -in ~/.ssh/id_rsa -pubout  > ~/.ssh/id_rsa.pub.pem

cat ~/.ssh/id_rsa.pub.pem

# encrypt the file into secret.txt
openssl rsautl -encrypt -pubin -inkey ~/.ssh/id_rsa.pub.pem -in file.txt -out secret.txt

# decrypt the file and print the contents to stdout
openssl rsautl -decrypt -inkey ~/.ssh/id_rsa -in secret.txt
