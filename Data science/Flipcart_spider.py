from dputils import scrape

# step1.get the data as soup obj.
# step2.create the setup dictionaries.
# step3.pass the dictionaries into the extract_many()function.
# step4.repeat the step1 to step3 until data keep coming.
# step5.check and save data into a file.

#understanding the url
url='https://www.flipkart.com/'

# step1
query = 'laptop'
pos = 1
url= f'https://www.flipkart.com/search?q={query}&page={pos}'
soup = scrape.get_webpage_data(url)


# Step2
# target dict,items dict,etc

t  = {'tag':'div', 'attrs':{'class':'_1YokD2 _3Mn1Gg'}}
rep_items =  {'tag':'div', 'attrs':{'class':'_1AtVbE col-12-12'}}
title = {'tag':'div', 'attrs':{'class':'_4rR01T'}}
price = {'tag':'div', 'attrs':{'class':'_30jeq3 _1_WHN1'}}
link = {'tag':'a', 'attrs':{'class':'_1fQZEK'}, 'output' : 'href'}

# Step3

data = scarpe.extract_many(soup,target)
