from csv import reader
import re

file = open("openfoodfacts_search.csv", "r")
data = file. read()
occurrences = data.count("sweeteners")
print ('Number occurrences: ', occurrences)
occurrences = data.count("artificially sweetened")
print ('Number of occurrences of "artificially sweetened":', occurrences)
occurrences = data.count ("artificial sweeteners")
print ('Number of occurrences of "artificial sweeteners":', occurrences)
occurences = data.count ("natural flavors")
print ('Number of occurences of "natural flavors":', occurences)
occurrences = data.count ("sweeteners,")
print ('Number of occurences of "sweeteners,":', occurences)

occurrences = data.count ("artificial flavour,")
print ('Number of occurences of "artificial flavour,":', occurences)





lineCounter = 0
#for line in reader(open("openfoodfacts_search.csv",newline="\n")):
#  print(line[29])
#  print("===)")
#  lineCounter += 1
  #if lineCounter == 5:
  #  break
  

count = 0
wordCount = {}

for line in reader(open("openfoodfacts_search.csv",newline="\n")): 
  word = line[29]
  result = re.search("\s+[a-zA-Z-]*\s?sweet[a-zA-Z-,)]*", word)
  if result != None:
    count += 1
    if result.group() in wordCount.keys():
      wordCount[result.group()] += 1
    else:
      wordCount[result.group()] = 1

print ("sweet count: ", count)

for key in wordCount.keys():
  print ('word: ', key)
  print ('occurrences: ', wordCount[key], '\n')


for line in reader(open("openfoodfacts_search.csv",newline="\n")): 
  word = line[29]
  result = re.search("\s+[a-zA-Z-]*\s?natural flavor[a-zA-Z-,)]*", word)
  if result != None:
    count += 1
    if result.group() in wordCount.keys():
      wordCount[result.group()] += 1
    else:
      wordCount[result.group()] = 1


for key in wordCount.keys():
  print ('word: ', key)
  print ('occurrences: ', wordCount[key], '\n')


counta= 0

for line in reader(open("openfoodfacts_search.csv",newline="\n")): 
  word = line[29]
  result = re.search("\s+[a-zA-Z-]*\s?artificial flavor[a-zA-Z-,)]*", word)
  if result != None:
    counta += 1
    if result.group() in wordCount.keys():
      wordCount[result.group()] += 1
    else:
      wordCount[result.group()] = 1

for key in wordCount.keys():
  print ('word: ', key)
  print ('occurrences: ', wordCount[key], '\n')

for line in reader(open("openfoodfacts_search.csv",newline="\n")): 
  word = line[29]
  result = re.search("\s+[a-zA-Z-]*\s?artificial flavour[a-zA-Z-,)]*", word)
  if result != None:
    counta += 1
    if result.group() in wordCount.keys():
      wordCount[result.group()] += 1
    else:
      wordCount[result.group()] = 1

for key in wordCount.keys():
  print ('word: ', key)
  print ('occurrences: ', wordCount[key], '\n')


print ("natural flavor: ", count)
print ("artificial flavor: ", counta)