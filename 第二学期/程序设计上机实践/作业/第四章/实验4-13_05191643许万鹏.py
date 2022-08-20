one_hundred={'Q','W','E','R','T'}|{'1'}|{'2'}|{'4'}
two_hundred={'A','S','D','F','G'}|{'1'}|{'3'}|{'4'}
four_hundred={'Z','X','C','V','B'}|{'2'}|{'3'}|{'4'}
one_hundred_and_two_hundred=one_hundred&two_hundred-four_hundred#顺序运算
one_hundred_and_four_hundred=one_hundred&four_hundred-two_hundred
two_hundred_and_four_hundred=two_hundred&four_hundred-one_hundred
print("{}".format(one_hundred_and_two_hundred|one_hundred_and_four_hundred|two_hundred_and_four_hundred))
#集合名不能包含数字
