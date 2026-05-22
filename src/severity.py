from src.data_loader import load_severity # load_severity data

severity_dict=load_severity() # load severity data into dictionary


def calculate_severity(symptoms): # input list of user selected symptoms, output severity score

    score=0 # initialize severity score

    for s in symptoms: # iterate through user selected symptoms

        score+=severity_dict.get(s,0) # add severity score of each symptom to total score

    return score # return severity score