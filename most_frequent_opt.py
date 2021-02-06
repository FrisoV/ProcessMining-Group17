import pandas as pd

def extract_frequencies(input_dict):
    ##from a dictionary with lists returns the most frequent item in each list
    dct = {}
    for key in input_dict.keys():
        lst = input_dict[key]
        most_frequent = max(set(lst), key = lst.count)
        dct[key] = most_frequent

    return dct

def get_most_frequent(train_set):
    ###extract most frequent events from train set
    if type(train_set) != pd.core.frame.DataFrame:
        raise ValueError("Train set is not a DataFrame")
    else:
        train = train_set.copy()
    cases = train["case concept:name"].unique()
    events = train["event concept:name"].unique()

    frequent_events = {}
    for item in events:
        frequent_events[item] = []
        
    for case_nr in cases:
        trace = train[train["case concept:name"] == case_nr] #one case path
        events_values = trace["event concept:name"].values #every event in a case IN ORDER
        i=1
        for event in events_values:
            next_event = events_values[i] #gets next event
            if next_event == event:
                pass
            else:
                lst = frequent_events.get(event)
                lst.append(next_event)
                frequent_events[event] = lst

            if i < len(events_values)-1:
                i += 1
    final = extract_frequencies(frequent_events)

    return final

def test_inputer(test, most_frequent_dct):
    #inputs most frequent event into test set, based on passed dictionary
    
    def next_event(row):
        next_event = most_frequent_dct[row["event concept:name"]]
        return next_event
    test["NEXT EVENT"] = test.apply(next_event, axis = 1)

    return test

def baseline_next_event(path_to_train, path_to_test, output_csv):
    #MAIN function for the baseline implementation

    train = pd.read_csv(path_to_train) #train set from csv
    test = pd.read_csv(path_to_test) #test set from csv

    ### GET NEXT EVENT based on most frequent for baseline
    next_event_dct = get_most_frequent(train)
    test_next_event = test_inputer(test, next_event_dct)

    ### GET TIME UNTIL NEXT EVENT
    #############################
    #######  code here  #########
    #############################

    #create csv and return it

    test_next_event.to_csv(output_csv)
    print("CSV is saved to current dictionary with name {}".format(output_csv))

train_path = "data/BPI_Challenge_2012-training.csv"
test_path = "data/BPI_Challenge_2012-test.csv"

baseline_next_event(train_path, test_path, "test_next_event.csv")
