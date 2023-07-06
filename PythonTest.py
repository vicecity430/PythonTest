import addDigits
import rotateString

#print("hello world")
#print("This line is change by branch-1")

AddTwoDigits = addDigits.Solution
RotateString = rotateString.Solution

#Test class 1
nA = 13
nResult = AddTwoDigits.addDigits(AddTwoDigits, nA)
print("addDigits = {}".format(nA))
print("Result = {}".format(nResult))
#Test class 1 End

#Test class 2
strA = "abcde"
strB = "abc"
strReverseA = "edcba"
print("strA = {}".format(strA))
print("strB = {}".format(strB))
print("strReverseA = {}".format(strReverseA))

bIsRotate = RotateString.rotateString(RotateString, strA, strB)
print("strA & strB, Result is {}".format(bIsRotate))
bIsRotate = RotateString.rotateString(RotateString, strA, strReverseA)
print("strA & strReverseA, Result is {}".format(bIsRotate))
#Test class 2 End
