# Instructions

Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. 

IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Input to the function is guaranteed to be a single string.

**Examples**
```text
Valid inputs:

1.2.3.4
123.45.67.89

Invalid inputs:

1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
```
**Note that leading zeros (e.g. 01.02.03.04) are considered invalid.**


#### Code To Start
```python
def is_valid_IP(strng):
    return None
```

# Tests Given
```python
Test.assert_equals(is_valid_IP('12.255.56.1'),     True)
Test.assert_equals(is_valid_IP(''),                False)
Test.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
Test.assert_equals(is_valid_IP('123.456.789.0'),   False)
Test.assert_equals(is_valid_IP('12.34.56'),        False)
Test.assert_equals(is_valid_IP('12.34.56 .1'),     False)
Test.assert_equals(is_valid_IP('12.34.56.-1'),     False)
Test.assert_equals(is_valid_IP('123.045.067.089'), False)
Test.assert_equals(is_valid_IP('127.1.1.0'),        True)
Test.assert_equals(is_valid_IP('0.0.0.0'),          True)
Test.assert_equals(is_valid_IP('0.34.82.53'),       True)
Test.assert_equals(is_valid_IP('192.168.1.300'),   False)
```