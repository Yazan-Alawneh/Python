# Write a function called reverse_string that takes a string as input and returns its reverse.
# example  "hello" => "olleh"
def reverse_string(word):
 return word[::-1]

x = 'hello'
print(reverse_string(x),'\n')


# Write a function called is_palindrome that takes a string as input and
# returns True if the string is a palindrome and False otherwise.
# examples "civic" => True
# example  "man" => "nam" => False
def is_palindrome(s):
 cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
 return cleaned_string == cleaned_string[::-1]


print(is_palindrome("Radar"))
print(is_palindrome("Level"))
print(is_palindrome("Happy"))


def v2(word):
  check = word[::-1]
  if check.lower() == word.lower():
   return True
  else:
   return False

print(v2("radar"))
print(v2("level"))
print(v2("happy"))

print('\n')
# Write a function called remove_duplicates that takes a list as input and
# returns a new list with duplicate elements removed.
# example [3,2,2,4,5] => [3,2,4,5]
def remove_duplicates(list):
 new_list = []
 for item in list:
  if item not in new_list:
   new_list.append(item)
 return new_list

l = [7,5,6,6,7,7]
print(remove_duplicates(l),'\n')


# Write a function called list_sum that takes a list of numbers as input and
# returns the sum of all elements.
# example [5,5,5] => 15
def list_sum(list):
 return sum(list)

b = [10, 10, 10]
print(list_sum(b),'\n')


# Write a function called remove_element that takes a list and an element
# as input and removes all occurrences of that element from the list.
# The function should return the modified list.
# example [1,2,6,5,3], 3 => [1,2,6,5]
def remove_element(list, element):
 return [x for x in list if x != element]

r = [4,3,2,5,3,3]
element =  3
print(remove_element(r,element))
