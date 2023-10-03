import Pandas as pd

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv(url, header=None, names=column_names)

df.to_csv("iris_saved.csv", index=False)
df = pd.read_csv(" iris.csv")

print ("Shape-of-the-DataFrame:", df.shape)
print ("\n First-5-rows-of-the-DataFrame:")
print(df.head())

print ("\nSummary-statistics-of-the-DataFrame:")
print(df. describe())

mean_sepal_length = df['sepal_length'].mean() 
median_sepal_width = df['sepal_width'].median()
std_petal_length = df['petal_length'].std()

print("Loading MNIST dataset without normalization...")
import torchvision
trainset = torchvision.datasets.MNIST(root='.d/data',
                                      train = True
                                      download=T
                                      transform =transforms.Totensor())
trainloader = DataLoader(trainset, batch_size=1000, shuffle=False)