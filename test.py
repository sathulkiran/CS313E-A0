def func (a, b):

  if (a % b == 0):

    return b

  else:

    return func (b, a % b)


z = (88//4)*(88//4)
print(z)