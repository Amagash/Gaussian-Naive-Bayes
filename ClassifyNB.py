def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier

    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    pred = clf.fit(features_train, labels_train)
    # pred = clf.predict(features_train, labels_train)
    return pred
    ### your code goes here!

