# This is the file used to help create basic nlp responses
# It uses the cordial algorithm

# Very basic NLP using simple ifs and elses


def return_quest_punct(text):
    words = text.split(" ")
    current_index = 0
    past_index = 0
    for i in range(len(words)):
        word = words[i]
        if word.count("?") > 0:
            current_index = i
            for j in range(0, current_index):
                if words[j].count(".") > 0:
                    past_index = j
                break
        break

    quest_sent = words[past_index:current_index]
    quest_str = ""
    for word in quest_sent:
        quest_str = quest_str + " " + word
    return quest_str

def return_quest(text: str):
    text.lower()
    words = text.split(" ")
    start_index = 0
    end_index = 0
    for i in range(len(words)):
        word = words[i]
        buzzWords = ['solve', 'compute', 'determine', 'explain', 'do']
        if word in buzzWords:
            for j in range(0, i):
                if words[j].count('.') > 0:
                    start_index = j
                break
            for j in range(i, len(words)):
                if words[j].count('.') > 0:
                    end_index = j
                break
        break
    quest_list = words[start_index:end_index]
    quest_str = ""
    for item in quest_list:
        quest_str = quest_str + " " + item
    return quest_str

def return_statement(text: str, question: str):
    question.replace('?', '')
    question.lower()
    quest_list = question.split(" ")
    words = text.split(" ")
    start_index = 0
    end_index = 0
    for i in range(len(words)):
        word = words[i]
        buzzWords = ["answer", "solution",
                            "key", "result", "justification"]
        # if word.lower() == "answer" or word.lower() == "solution" or word.lower:
        if word.lower() in buzzWords:
            for j in range(0, i):
                if words[j].count('.') > 0:
                    start_index = j
                break
            for j in range(i, len(words)):
                if words[j].count('.') > 0:
                    end_index = j
                break
        break
    statement_sentance = words[start_index:end_index]
    statement = ""
    for word in statement_sentance:
        statement = statement + " " + word
    return statement
