## 1. Setting Variables ##

/home/dq$ FOOD="Shrimp gumbo"

## 2. Accessing Variables ##

/home/dq$ echo $FOOD

## 3. Setting Environment Variables ##

/home/dq$ export FOOD="Chicken and waffles"

## 4. Accessing Environment Variables ##

/home/dq$ python
/home/dq$ import os
/home/dq$ print(os.environ["FOOD"])
/home/dq$ exit()
/home/dq$ echo $FOOD

## 5. Calling Programs ##

/home/dq$ /usr/bin/python
/home/dq$ exit()

## 6. The PATH Variable ##

/home/dq$ echo $PATH

## 7. Flags ##

/home/dq$ ls -l

## 8. Combining Flags ##

/home/dq$ ls -al

## 9. Long Flags ##

/home/dq$ ls -al --ignore=.ipython
