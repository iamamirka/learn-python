with open("./sample_data/novel-text.txt", "r") as file:
    data = file.readlines()
    print(len(data))
    for line in data:
        # lowercase words and split on whitespace to
        # to form a list of word tokens
        clean_line = line.lower().split()
        #print(clean_line)

        # check for sentences that contain 'wild' and 'places'
        if {'wild', 'places'}.issubset(set(clean_line)):
            print(line)