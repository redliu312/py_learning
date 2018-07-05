import sys
from multiprocessing import Process, Queue
from subprocess import check_output, CalledProcessError, Popen, PIPE
from memory_profiler import profile
# https://stackoverflow.com/questions/30847502/subprocess-check-output-without-high-memory-usage


@profile
def cmdloop(inQueue,outQueue):
    while True:
        command = inQueue.get()
        try:
            print(command)
            result = check_output(command,shell=True)
        except CalledProcessError as e:
            result = e

        outQueue.put(result)
        return

inQueue = Queue()
outQueue = Queue()
cmdHostProcess = Process(target=cmdloop, args=(inQueue,outQueue,))
cmdHostProcess.start()


def callCommand(command):
    inQueue.put(command)
    return outQueue.get()

def killCmdHostProcess():
    cmdHostProcess.terminate()

@profile
def execute(cmd, ignore_error=True):
    cmd = cmd.split()
    process = Popen(
        cmd, stdin=PIPE, stderr=PIPE
    )
    message = process.communicate()[1].decode('utf8')

    rc = process.returncode

    if not ignore_error:
        assert rc == 0, u'EXE: %s\n%s' % (cmd, message)

    return message


def main():
    if sys.argv[1]  == "proc":
        while True:
            command =input()
            ret = callCommand(command)
            print(ret)
    elif sys.argv[1] == "sub":
        while True:
            cmd = input()
            ret =execute(cmd)
            print(ret)
    else:
        print("u did not choose a test mod3")


if __name__=="__main__":

    main()
