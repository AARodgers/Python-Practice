# note: list.sort() will change a list permanently
# note; sorted(list) changes the order temporarily

to_visit = ['Scotland', 'Fij', 'Mexico', 'Canada']
print(to_visit)
print("\nHere is the sorted list of locations:")
print(sorted(to_visit))
print("\nHere is the original order:")
print(to_visit)
print("\nHere is the reverse order using sorted that will not permanently change the order:")
print(sorted(to_visit, reverse=True))
print("\nHere is original order again:")
print(to_visit)
print("\nHere is the list in reverse order which will change the order permanently:")
to_visit.reverse()
print(to_visit)
print("\nHere is the list in the orginal order by using reverse again:")
to_visit.reverse()
print(to_visit)
print("\nHere is the list sorted in alphabetical order permanently using list.sort():")
print(sorted(to_visit))
print("\nHere is the list permanently sorted backwards using using list.sort(reverse=True)")
to_visit.sort(reverse=True)
print(to_visit)
print(f"\nThe number of places that I want to visit is {len(to_visit)}")
