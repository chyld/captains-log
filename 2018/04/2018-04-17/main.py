import pandas as pd

df = pd.read_csv('cars.csv')
df.corr()['mpg']

# Out[4]:
# mpg             1.000000
# cylinders      -0.777618
# displacement   -0.805127
# horsepower     -0.778427
# weight         -0.832244
# acceleration    0.423329
# model           0.580541
# origin          0.565209
