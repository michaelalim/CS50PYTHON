# QQQ: Does the input function work for any type of information or only for words (strings)?
# AAA: According to its documentation, input is expecting to what we call a string. 
# ----------------------------------------------------------------------------------------------------------------------
# QQQ: How to do many lines of comments?
# AAA: Continuous hash
# EXAMPLE
# 
# 
# 
# 
# AAA2: Another way is
"""
Everything in between is a comment
"""
# ----------------------------------------------------------------------------------------------------------------------
# QQQ: Can you use a function many times to solve a certain problem that we encounter many times in our code
# AAA: You can. But you can make your own function (which we will learn later) so that we're not repeating a lot
# ----------------------------------------------------------------------------------------------------------------------
# QQQ: What is the difference between using comma in perimeters than using concatenation? print("example " + variable) vs print("example", variable)
# AAA: In the context of strings, the plus operator is not just adding but it also concatenates, but it might get a little ugly having to use a lot of + signs.
# ----------------------------------------------------------------------------------------------------------------------
# QQQ: Quotation marks within quotation marks
# AAA: One way is escaping (but this is me speaking it's hard), another way is using single quotes outside then double quotes inside if you want to show your double quotes
# ----------------------------------------------------------------------------------------------------------------------
# QQQ: Is there anyway you could remove whitespaces in between of the value?
# AAA: No, it could only remove from the left and the right. In addition, there are also lstrip() and rstrip() functions which are straightforwardly says that it would remove whitespaces from left, and from right, respectively. Removing whitespaces in between will have to use another trick (probably on the next lessons) NOTE This is #6.var.title.py question
# ----------------------------------------------------------------------------------------------------------------------
# QQQ: How many functions could we combine? (referring to .strip().title combination)
# AAA: You could put as many as you want, but it might look bad if there's too many functions combined together on one line
# ----------------------------------------------------------------------------------------------------------------------
# NOTE: RHETORICAL QUESTION
# QQQ: is bring down .strip().title() better than combining them according to most programmers?
# AAA: There is no right answer BUT most people (as I have understood the instructor) loves breaking it down more to make it more readable especially if hte line gets a little bit too long.