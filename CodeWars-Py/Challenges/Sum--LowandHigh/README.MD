# Instructions
Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)
```text
Example:

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
```

If array is empty, null or None, or if only 1 Element exists, return 0.
Note:In C++ instead null an empty vector is used. In C there is no null. ;-) 


-- There's no null in Haskell, therefore Maybe [Int] is used. Nothing represents null.
Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.


#### Code To Start
```python
def sum_array(arr):
    #your code here
```

# Tests Given
```python
Test.describe("Basic tests")
Test.it("None or Empty")
Test.assert_equals(sum_array(None), 0)
Test.assert_equals(sum_array([]), 0)

Test.it("Only one Element")
Test.assert_equals(sum_array([3]), 0)
Test.assert_equals(sum_array([-3]), 0)

Test.it("Only two Element")
Test.assert_equals(sum_array([ 3, 5]), 0)
Test.assert_equals(sum_array([-3, -5]), 0)

Test.it("Real Tests")
Test.assert_equals(sum_array([6, 2, 1, 8, 10]), 16)
Test.assert_equals(sum_array([6, 0, 1, 10, 10]), 17)
Test.assert_equals(sum_array([-6, -20, -1, -10, -12]), -28)
Test.assert_equals(sum_array([-6, 20, -1, 10, -12]), 3)
```