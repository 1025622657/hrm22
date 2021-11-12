import pytest
import warnings
warnings.filterwarnings("ignore")


if __name__ == "__main__":
    pytest.main(['-s', 'case'])
    #pytest.main(["-s test_case.py --alluredir", "./report/allure_raw3"])
