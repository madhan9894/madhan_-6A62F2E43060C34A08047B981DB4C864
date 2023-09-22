def isleapyear(year):
  if(year%==0 and year%100!=0):
    return True
  else:
    return False
    year=int(input("Enter a Year:"))
    if isleaoyear(year):
      print("{} is a leap year.".format(year))
    else:
      print("{} is not a leap
      year.".format(year))