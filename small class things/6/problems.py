import re

def problem1(searchstring):
    """
    Match phone numbers.

    :param searchstring: string
    :return: True or False
    """
    valid = False

    p = re.compile('^\(\d{3}\)\s\d{3}\-\d{4}$') #for (XXX) XXX-XXXX
    if (p.search(searchstring)) :
        valid = True
    p = re.compile('^\d{3}\-\d{3}-\d{4}$') #for XXX-XXX-XXXX
    if (p.search(searchstring)) :
        valid = True
    p = re.compile('^\d{3}-\d{4}$') #for XXX-XXXX
    if (p.search(searchstring)) :
        valid = True
    
    return valid
    pass
        
def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """
    #p = re.compile("[0-9]+\s([A-Z][a-z]*\s)+(Ave|Dr|St|Rd)\.")
    #p = re.compile("[0-9]+\s([A-Z][a-z]*\s)+(Ave|Dr|St|Rd)\.")
    testing = re.search(r"[0-9]+\s([A-Z][a-z]*\s)+(Ave|Dr|St|Rd)\.", searchstring)
    if (testing) :
        valid = True
    else:
        valid = False
    #holder = re.match("[0-9]+\s([A-Z][a-z]*\s)+\b(Ave|Dr|St|Rd)\b\.", searchstring)
    #print(testing.span())
    #print(testing.group())
    street = testing.group()
    street = street.split(" ", 1) #filter out the numbers and space in the beginning
    street = street[1]
    end = street.rfind(' ') #filter out the road type at the end
    street = street[:end]
    #print(street)

    return street
    pass
    
def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """
    holder = re.search(r"[0-9]+\s([A-Z][a-z]*\s)+(Ave|Dr|St|Rd)\.", searchstring)
    street = holder.group() #get the street address
    index = holder.span()

    street = street.split(" ", 1) #filter out the numbers and space in the beginning
    offset = len(street[0])
    street = street[1]
    end = street.rfind(' ') #filter out the road type at the end
    street = street[:end]
    reverse = street[::-1] #reverse street name
    #print(reverse)

    #print(index)
    #print(index[0]+offset)
    #print(searchstring)
    new_string = searchstring[:index[0]+offset+1] + reverse + searchstring[index[0]+offset+len(street)+1:]
    #print(new_string)
    return new_string
    pass


if __name__ == '__main__' :
    print(problem1('765-494-4600')) #True
    print(problem1(' 765-494-4600 ')) #False
    print(problem1('(765) 494 4600')) #False
    print(problem1('(765) 494-4600')) #True    
    print(problem1('494-4600')) #True
    
    print(problem2('The EE building is at 465 Northwestern Ave.')) #Northwestern
    print(problem2('Meet me at 201 South First St. at noon')) #South First
    
    print(problem3('The EE building is at 465 Northwestern Ave.'))
    print(problem3('Meet me at 201 South First St. at noon'))
