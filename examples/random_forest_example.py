# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-08-21 16:39:58
@Last Modified by:   tushushu
@Last Modified time: 2018-08-21 16:39:58
"""
import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])

import sys
sys.path.append(os.path.abspath(".."))

from imylu.utils import load_breast_cancer, train_test_split, get_acc, run_time
from imylu.ensemble.random_forest import RandomForest


@run_time
def main():
    print("Tesing the accuracy of RandomForest...")
    # Load data
    X, y = load_breast_cancer()
    # Split data randomly, train set rate 70%
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=40)

    # Train model
    rf = RandomForest()
    rf.fit(X_train, y_train, n_samples=300, max_depth=3, n_estimators=20)
    # Model accuracy
    get_acc(rf, X_test, y_test)


if __name__ == "__main__":
    main()
