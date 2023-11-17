What's the difference between the __div__ and the __truediv__ methods? 
<br><br>
 It appears that the __truediv__ just calls the __div__ method, so what gives?  
<br>Python 3 does away with the __div__ method in favor of the __truediv__ method and Python 2 uses the __div__ method.  That's really it.  I'm trying to make this work for both Python 2 and Python 3.
<br>
 These methods allow us to check for equality between two vectors.  This is also where we use the thresh variable. In computer-land two values can be nearly equal like 2 and 2.00000000001. If we were doing scientific computing, then that difference could be significant. However, we aren't doing science and we need to be able to say that those two values are the same. So we do that by subtracting the two values and then seeing if it's less than our theshold value, which is just a really small number. So in our game the two vectors <3,4> is equal to <3.000004, 4.000001>.
<br>
We have two types of magnitude methods here. The 'magnitude' method returns the actual length of the vector which requires a square root (which is why we had to import the math package). The 'magnitudeSquared' method, however, is the one we'll use more often in our game. The reason is because it does not require us to take a square root. It's good practice to avoid taking the square root in your games whenever you can avoid it. If all you need to do is compare the length of two vectors, then comparing their length squared is just as valid as comparing their length. For example, if m and n are the lengths of two vectors and if m > n, then it's also true that m2 > n2. 

