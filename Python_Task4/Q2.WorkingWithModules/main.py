
#importing modules of list string and logical operators
import functionsOfLogicalOperators
import functionOfList
import functionOfStrings

#calling all the functions of functionOfList module
print("------functions of list-------")
List = [12,58,64,13,11,24]
functionOfList.calculateSquare(6)
functionOfList.findMax(List)
functionOfList.findMin(List)
functionOfList.sumOfNumberList(List)
print()

#calling all the functions of functionOfStrings module
print("-------functions of string-------")
String="Hello Everyone"
functionOfStrings.calculateNoOfVowels(String)
functionOfStrings.lengthOfString(String)
functionOfStrings.middleCharacterOfString(String)
functionOfStrings.numberOfWords(String)
print()

#calling all the functions of functionOfLogicalOperators module
print("-------functions of logical operators-------")
x=10
y=20
functionsOfLogicalOperators.andOperator(x, y)
functionsOfLogicalOperators.orOperator(x, y)
functionsOfLogicalOperators.notOperator(x)
print()
