import os
import shutil
import subprocess

def compile(path, name):
    os.system("g++ -g -pipe -O2 -s -static -lm -DTHEMIS -Wl,--stack,66060288 " + path + " -o " + name + ".exe")

def run(name, fileIn, fileOut):
    fin = None
    fout = None
    if fileIn != "":
        fin = open(fileIn, "r")
    if fileOut != "":
        fout = open(fileOut, "w")
    
    subprocess.run([name + ".exe"], stdin = fin, stdout = fout)
    
    if fin != None:
        fin.close()
    if fout != None:
        fout.close()

def createRoot(prob):
    os.makedirs(prob, exist_ok = True)

def createTestSet(prob, test):
    os.makedirs(prob + "/Test" + str(test), exist_ok = True)
    
def moveToTestSet(prob, test, name):
    shutil.copyfile(name, prob + "/Test" + str(test) + "/" + name)

numTest = 2
problemName = "test"
solutionName = "solution"
solutionPath = "solution.cpp"
generatorName = "generator"
generatorPath = "generator.cpp"
defaultInput = "input.txt"
defaultOutput = "output.txt"

compile(generatorPath, generatorName)
compile(solutionPath, solutionName)
createRoot(problemName)

for i in range(numTest):
    createTestSet(problemName, i)
    run(generatorName, "", defaultInput)
    run(solutionName, defaultInput, defaultOutput)
    moveToTestSet(problemName, i, defaultOutput)
    moveToTestSet(problemName, i, defaultInput)
    