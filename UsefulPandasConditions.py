
# Src: https://sparkbyexamples.com/pandas/pandas-create-conditional-column-in-dataframe/
# Below are some quick examples.
# Create conditional DataFrame column by np.where() function.
df['Discount'] = np.where(df['Courses']=='Spark', 1000, 2000)

# Another way to create column conditionally.
df['Discount'] = [1000 if x == 'Spark' else 2000 for x in df['Courses']]

# Create conditional DataFrame column by map() and lambda.
df['Discount'] = df.Courses.map( lambda x: 1000 if x == 'Spark' else 2000)

# Create conditional DataFrame column by np.select() function.
conditions = [
    (df['Courses'] == 'Spark') & (df['Duration'] == '30days'),
    (df['Courses'] == 'Spark') & (df['Duration'] == '35days'),
    (df['Duration'] == '50days')]
choices = [1000, 1050,200]
df['Discount'] = np.select(conditions,choices, default=0)

# Using Dictionary to map new values.
Discount_dictionary ={'Spark' : 1500, 'PySpark' : 800, 'Spark' : 1200}
df['Discount'] = df['Courses'].map(Discount_dictionary)

# Pandas create conditional DataFrame column by dictionary
df['Discount'] = [Discount_dictionary.get(v, None) for v in df['Courses']]

# Using DataFrame.assign() method.
def Courses_Discount(row):
    if row["Courses"] == "Spark":
        return 1000
    else:
        return 2000
df = df.assign(Discount=df.apply(Courses_Discount, axis=1))

# Conditions with multiple rand multiple columns.
def Courses_Discount(row):
    if row["Courses"] == "Spark":
        return 1000
    elif row["Fee"] == 25000:
        return 2000
    else:
        return 0
df = df.assign(Discount=df.apply(Courses_Discount, axis=1))

# Using .loc[] property for single condition.
df.loc[(df['Courses']=="Spark"), 'Discount'] = 1000

# Using loc[] method for Multiple conditions.
df.loc[(df['Courses']=="Spark")&(df['Fee']==23000)|(df['Fee']==25000), 'Discount'] = 1000

# Using DataFrame.apply() method with lambda function.
df['Discount'] = df['Courses'].apply(lambda x: '1000' if x=='Spark' else 1000)

# Pandas create conditional column using mask() method.
# Replace values where the condition is True
df['Discount'] = df['Discount'].mask(df['Courses']=='Spark', other=1000)

# Using where()
df['Discount'] = df['Discount'].where(df['Courses']=='Spark', other=1000)

# Using transform() with a lambda function.
df['Discount'] = df['Courses'].transform(lambda x: 1000 if x == 'Spark' else 2000)
