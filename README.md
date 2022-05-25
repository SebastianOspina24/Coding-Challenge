# Coding Challenge Slang

## Juan Sebastian Ospina Calderon    5/25/2022

Here is my solution to the problem given, where I sort the array given, 
then go through it and create the sessions for each user.

### Complexity analysis

For this algorithm, I was based on 2 step solution first to sort the list given,
in were using sort whit a complexity of O(n log(n)) plus the second part that is 
loop in where I order this activities order in the list so to get the complexity of this part
it is very easy, there is just one loop mean an O(n) an then is a constant value of lines this means that
my complexity is just of O(nLog(n)), using a sort list (key value was the first_seen_at) helps us just to need to add an check
with the last value of the array because is sort reduxin complexity.