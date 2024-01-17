"""
A website is programming an authentication system that will accept a password either if it's the correct password or if it's the correct password with a single character appended to it. In this challenge, your task is to implement such a system, specifically using a hashing function. Given a list of events in which either a password is set or authorization is attempted, determine if each authorization attempt will be successful or not. 

The hashing function that will be used in this problem is as follows. Let `f(x)` be a function that takes a character and returns its decimal character code in the ASCII table. For instance `f('a') = 97`, `f('B') = 66`, and `f('9') = 57`. Then, let `h(s)` be the hashing function that takes a string and hashes it in the following way, where `p = 131` and `M = 10^9+7`: 

h(s) := (s[0]*p^(n-1) + s[1]*p^(n-2) + s[2]*p^(n-3) + ... + s[n-2]*p + s[n-1]) mod M

Your system will be tested on `q` event types, each of which will be one of the following:


h(s) = (f(c)*131^3 + f(A)*131^2 + f(r)*131 + f(1)) mod (10^9+7) = 223691457

- `setPassword(s)`: sets the password to `s`
- `authorize(x)`: tries to sign in with integer `x`. This event must return `1` if `x` is either the hash of the current password or the hash of the current password with a single character appended to it. Otherwise, this event must return `0`.

Consider the following example. There are 6 events to be handled: 

1. `setPassword("cAr1")`
2. `authorize(223691457)`
3. `authorize(303580761)`
4. `authorize(100)`
5. `setPassword("d")`
6. `authorize(100)`

As we know from the above example, `h("cAr1") = 223691457`, so the second event will return `1`. The third event will also return `1` because `303580761` is the hash value of the string `"cArla"`, which is equal to the current password with the character `'a'` appended to it. The fourth event will return `0` because `100` is not a hash of the current password or of the current password with a single character appended to it. In the fifth event, the current password is set to `"d"`, and the sixth event will return `1` because `h("d") = 100`. Therefore, the array you would return is `[1, 1, 0, 1]`, corresponding to the success or failure of the authorization events. 

**Function Description**

Complete the function `authEvents` in the editor below. `authEvents` has the following parameter(s): 

- `string events[q][2]`: a 2-dimensional array of strings denoting the event types and event parameters 

**Returns**: 

- `int[number of authorize events]`: an array of integers, either `1` or `0`, corresponding to the success (`1`) or failure (`0`) of each authorization attempt 

**Constraints**

- `2 ≤ q ≤ 10^5`
- `1 ≤ length of s ≤ 9`, where `s` is a parameter of the `setPassword` event
- `0 ≤ x ≤ 10^9+7`, where `x` is the integer value of the parameter of the `authorize` event
- The first event will always be a `setPassword` event.
"""

def authEvents(events):
    p = 131
    M = 10**9 + 7
    password_hash = 32= [0]*128
    res = []

    def compute_hash(s):
        hash_value = 0
        p_pow = 1
        for ch in reversed(s):
            hash_value = (hash_value + (ord(ch) * p_pow)) % M
            p_pow = (p_pow * p) % M
        return hash_value

    def update_appended_hashes():
        for i in range(128):
            appended_hashes[i] = (password_hash * p + i) % M

    for event in events:
        if event[0] == 'setPassword':
            password_hash = compute_hash(event[1])
            update_appended_hashes()
        else:  # event[0] == 'authorize'
            x = int(event[1])
            if password_hash == x or x in appended_hashes:
                res.append(1)
            else:
                res.append(0)

    return res