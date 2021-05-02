# Welcome to my project!
Prediction apple and orange.
This is basic project about machine learning.
For easier understanding to everyone, I use Tkinter to build a small layout with sklearn for for predict.

# Let’s get started
With IDE, you can use VScode or Pycharm. **Don't forget install Python.exe**.

we are going to use a supervised machine learning algorithm, which utilizes a known dataset (referred to as the training dataset) to predict future events.

Here is a general flow of the supervised learning recipe:

-   Gather training data
-   Train the classifier
-   Make predictions

Let’s talk about each of the steps.

### 1. Gathering training data

We will use two variables:  **features**  (data in the first two columns) and  **labels**  (data in the last column). In other words, features are the input data and labels are the output values.

Here is the Python code:
> features = [[140,1], [130,1], [150,0], [170, 0]]
> labels = [0,0,1,1]

**features** is meaning [weight(g), skin], skin = 1 is smooth, 0 is bumpy
**lable**: 0 - Apple, 1 - Orange. 

### 2.  Training the classifier

In this example, to keep things simple, I' m going to use a **decision tree**, which can use decision rules deduced from the data features to learn and make appropriate predictions.
> from sklearn import tree

Here is a code that imports the decision tree classifier and adds it to our project.
> clf = tree.DecisionTreeClassifier()
#clf is meaning classifier

In Scikit-learn, the training algorithm is referred to as Fit (which can loosely be interpreted as “find patterns in data.”).
> clf = clf.fit(features, labels)

### 3.  Making predictions 

Let’s say that the new fruit is smooth and weighs 120 grams. Remember that we represented smooth as  **1**. And, because the weight is not very high, it is likely to be an apple (**0**). Furthermore, smoothness is a feature of apples.

Let’s see if our ML algorithm can make such a prediction:



It works!

I use condition show result text:



The output is what we expected:  **0**  (apple).

# References

https://blog.education-ecosystem.com/a-simple-machine-learning-algorithm-to-differentiate-between-an-apple-and-an-orange/