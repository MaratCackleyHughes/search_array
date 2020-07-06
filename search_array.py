def main():
 size = 6
 names = ["Sally", "Tom","Sameer", "Rishika", "Fernando", "Camilio"]
 searchValue = ""
 index = 0
 found = False
 keepGoing = "y"
 while keepGoing == "y":
    print("Do you want to search the array?")
    keepGoing = input("(Enter y for yes.)").lower()
    if keepGoing == "y":
      index,found = searchFunction(index,searchValue,found,names,size)
      outputMod(index,found)
    else:
      print(" Thanks for searching")
 
 
def searchFunction(index,searchValue,found,names,size):
 searchValue = input("Enter a name to search for in the array: ").lower()
 while found == False and index <= size-1:
  if names[index].lower() == searchValue:
   found = True
  else:
   index = index + 1 
 return index,found  


def outputMod(index,found):
 if found:
  print("That name was found at subscript ", index)
 else:
  print("That name was not found in the array.")

main()