mylist = list(range(10))
#returns a list [0,1,2,3,4,5,6,7,9]
alias = mylist
print(mylist)
print(alias)
# We want to change the the items in my list but continue to have alias pointing to the edited mylist and not the old mylist

mylist[:] = ['a'] * 6
print(mylist) #returns ['a','a','a','a','a','a']
print(alias)  #returns ['a','a','a','a','a','a']
