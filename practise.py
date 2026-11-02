def add_tag (tag , tags= None) :
    if tags is None : 
        tags = [tag]
    else : 
        tags.append(tag)
    return tags
print (add_tag ("a"))
print (add_tag ("b"))
print (add_tag ("c" , ["X"]))