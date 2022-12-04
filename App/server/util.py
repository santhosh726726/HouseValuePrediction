import json
import pickle

model = None
__data_columns = None



if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_price(59982,5,7,4))
