from tempfile import NamedTemporaryFile
import shutil

src = "a.jpe"
right_jpe="right.jpe"
wrong_jpe="wrong.jpe"
wrong_jpe2="wrong2.jpe"
right2 = "right2.jpe"

def right():
    
    with open("a.jpe","r+") as f:
        for line in f:
            pass
    shutil.copy("a.jpe",right_jpe)

def wrong_temp():
    f=open("a.jpe","r+")
    with NamedTemporaryFile(suffix=".jpe",delete=True) as file:
        for line in f:
            file.write(line)
        shutil.copy(file.name,wrong_jpe2)

def wrong_temp_to_wright():
    f=open("a.jpe","r+")
    with NamedTemporaryFile(suffix=".jpe",delete=True) as file:
        for line in f:
            file.write(line)
        file.seek(0)
        shutil.copy(file.name,right2)
            


def wrong():
    
    f =  open("a.jpe","r+") 
        
    of = NamedTemporaryFile(suffix='.jpe',delete=False)
    for line in f:
	of.write(line)
    shutil.copy(of.name,wrong_jpe)


def main():
    right()
    wrong()
    wrong_temp_to_wright()
    wrong_temp()

if __name__ == "__main__":
    main()
