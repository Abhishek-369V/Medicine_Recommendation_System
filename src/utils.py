def symptoms_to_vector(symptoms,columns): # convert symptoms to vector
    # Convert user symptoms to vector

    vector=[0]*len(columns) # create vector of zeros with length of columns

    for s in symptoms: # loop through symptoms

        if s in columns: # if symptom is in columns

            index=columns.index(s) # get index of symptom

            vector[index]=1 # set value to 1 at index

    return vector # return vector