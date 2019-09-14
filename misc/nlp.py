# This is the file used to help create basic nlp responses
# It uses the cordial algorithm

# Very basic NLP using simple ifs and elses
import collections

def return_starred(text, count):
    if count > 1:
        starred = []
    words = text.split(" ")
    for i in range(len(words)):
        word = words[i]
        if word.count("*") > 0:
            word.replace("*", "")
            if count == 1:
                return word
            else:
                starred.append(word)
    return starred
            
def return_bold(text):
    # This will return an array of all bolded words
    words = text.split(" ")
    bolded = []
    count = []
    final = []
    for i in range(len(words)):
        word = words[i]
        if word.count("<b>") > 1:
            word.replace("<b>", "")
            word.replace("</b>", "")
            bolded.append(word)
    
    for item in bolded:
        count.append((bolded.count(item), item))
    
    for i in range(len(count)):
        min_val = min(count[i][0])
        final.append(min_val[1])
        count.remove(min_val)

    return final

def return_italics(text):
    words = text.split(" ")
    bolded = []
    count = []
    final = []
    for i in range(len(words)):
        word = words[i]
        if word.count("<i>") > 1:
            word.replace("<i>", "")
            word.replace("</i>", "")
            bolded.append(word)
    
    for item in bolded:
        count.append((bolded.count(item), item))
    
    for i in range(len(count)):
        min_val = min(count[i][0])
        final.append(min_val[1])
        count.remove(min_val)

    return final

def return_headers(text):
    words = text.split(" ")
    bolded = []
    count = []
    final = []
    for i in range(len(words)):
        word = words[i]
        if word.count("<h") > 1:
            word.replace("<h", "")
            word.replace("</h", "")
            word.replace("1>", "")
            word.replace("2>", "")
            word.replace("3>", "")
            word.replace("4>", "")
            word.replace("5>", "")
            word.replace("6>", "")
            bolded.append(word)
    
    for item in bolded:
        count.append((bolded.count(item), item))
    
    for i in range(len(count)):
        min_val = min(count[i][0])
        final.append(min_val[1])
        count.remove(min_val)

    return final

def return_headers(text):
    words = text.split(" ")
    bolded = []
    count = []
    final = []
    for i in range(len(words)):
        word = words[i]
        if word.count("<mark>") > 1:
            word.replace("<mark>", "")
            word.replace("</mark>", "")
            bolded.append(word)
    
    for item in bolded:
        count.append((bolded.count(item), item))
    
    for i in range(len(count)):
        min_val = min(count[i][0])
        final.append(min_val[1])
        count.remove(min_val)

    return final


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

def pattern_finder(text):
    big_dict = open("1-1000.txt", "r")
    big_list = big_dict.split("/n")
    big_dict.close()
    unformat(text)
    altered = []
    yes = []
    final = []
    ward = []
    count = []
    words = text.split(" ")
    for word in words:
        if word in big_list:
            del(word)
        else:
            altered.append(word)
    for word in altered:
        count.append((altered.count(word)))
        yes.append(word)
        for i in range(len(altered.count(word))):
            del(word)
    true_final = []
    for i in range(len(count)):
        final.append(max(count))
        ward.append(altered[count.index(max(count))])
        true_final.append((final[i], ward[i]))
        count.remove(max(count))

    return true_final

    def unformat(para):
        para.replace("<b>", "")
        para.replace("</b>", "")
        para.replace("<i>", "")
        para.replace("</i>", "")
        para.replace("<mark>", "")
        para.replace("</mark>", "")
        para.replace("<h", "")
        para.replace("</h", "")
        para.replace("1>", "")
        para.replace("2>", "")
        para.replace("3>", "")
        para.replace("4>", "")
        para.replace("5>", "")
        para.replace("6>", "")
        para.replace("<em>", "")
        para.replace("</em>", "")
