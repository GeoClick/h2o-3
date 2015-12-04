from tests import pyunit_utils
import sys
sys.path.insert(1, "../../../")
import h2o

def iris_nfolds():
    # Connect to h2o
    h2o.init(ip,port)

    iris = h2o.import_frame(path=pyunit_utils.locate("smalldata/iris/iris.csv"))


    model = h2o.random_forest(y=iris[4], x=iris[0:4], ntrees=50, nfolds=5)
    model.show()
  
    # Can't specify both nfolds >= 2 and validation = H2OParsedData at once
    try:
        h2o.random_forest(y=iris[4], x=iris[0:4], validation_y=iris[4], validation_x=iris[0:4], ntrees=50, nfolds=5)
        assert False, "expected an error"
    except EnvironmentError:
        assert True

if __name__ == "__main__":
	pyunit_utils.standalone_test(iris_nfolds)
else:
	iris_nfolds()