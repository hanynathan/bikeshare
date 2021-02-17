# bikeshare
solution for Udacity Data Analysis Professional Nanodegree Program (project #1)

## suggestions
Data structures and algorithms on python.  
1. [Think Python](http://greenteapress.com/thinkpython/html/index.html)  
2. [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/runestone/books/published/pythonds/index.html)  
3. [Data Structures and Algorithms in Python](https://docs.google.com/viewer?a=v&pid=sites&srcid=dnVrbWFsYmFzYS5jb218d3d3fGd4OjU3NWZjOWU1MTM4ZTI4OQ)  
4. this one is my favorite, it is about solving hard mathematical problems via programming languages. You really need to know how to play with data types : https://projecteuler.net


## visualization libraries:
1. [plotly](https://plotly.com/python/)
2. [streamlit](https://www.streamlit.io)
3. [tutorial about classes:](https://www.learnpython.org/en/Classes_and_Objects)


When I run the code, columns are collapsed, and only some of them are shown.
You can prevent this situation by adding this to your code:

1. `pd.set_option('display.max_columns',200)`
2. 
```
while True:
    display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
    if display_data.lower() != 'yes':
        break
    print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
    i+=5
 ```
    
I use a new library here, tabulate. So to use this, please also import the module:  
`from tabulate import tabulate`
