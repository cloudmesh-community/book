import os
from cloudmesh.common.util import path_expand

class EncryptFile (object):

    def __init__(self, file_in, file_out, debug=False):
        self.data = {
            'file': file_in,
            'secret': file_out,
            'pem': path_expand('~/.ssh/id_rsa.pub.pem'),
            'key': path_expand(' ~/.ssh/id_rsa')
        }
        self.debug = debug
        self.encrypt()

    def _execute(self, command):
        if self.debug:
            print(command)
        os.system(command)
            
        
    def pem_create(self):
        command = path_expand("openssl rsa -in {key} -pubout  > {pem}".format(**self.data))
        self._execute(command)

    def pem_cat(slef):
        command = path_expand("cat {pem}".format(**self.data))
        self._execute(command)

    def encrypt(self):
        # encrypt the file into secret.txt
        print (self.data)
        command = path_expand("openssl rsautl -encrypt -pubin -inkey {pem} -in {file} -out {secret}".format(**self.data))
        self._execute(command)

    def decrypt(self, filename=None):
        if filename is not None:
            self.data['secret'] = filename

        command = path_expand("openssl rsautl -decrypt -inkey {key} -in {secret}".format(**self.data))
        self._execute(command)

if __name__ == "__main__":        
        
  for filename in ['file.txt', 'secret.txt']:
      try:
          os.remove(filename)
      except Exception as e:
          pass

  # Creating a file with data

  with open("file.txt", "w") as f:
      f.write("Big Data is here.")

  e = EncryptFile('file.txt', 'secret.txt')
  e.decrypt()
    
