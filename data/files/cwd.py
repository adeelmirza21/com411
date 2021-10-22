import os
def cwd():
    path = os.getcwd()
    print (f"the current working directory is {path}")
    print (f"the directory contains the following files")
    for file in os.listdir(path):
        print(file)

def run():
    print("processing...")
    cwd()

if __name__ == "__main__":
  run()