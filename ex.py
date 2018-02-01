from tempfile import NamedTemporaryFile
import shutil

src = "a.jpe"
right_jpe="right.jpe"
wrong_jpe="wrong.jpe"


def right():
    
    with open("a.jpe","r+") as f:
        for line in f:
            pass
    shutil.copy("a.jpe",right_jpe)



def wrong():
    
    f =  open("a.jpe","r+") 
    
    of = NamedTemporaryFile(suffix='.jpe',delete=False)
    for line in f:
	of.write(line)
    shutil.copy(of.name,wrong_jpe)


def main():
    right()
    wrong()

if __name__ == "__main__":
    main()
