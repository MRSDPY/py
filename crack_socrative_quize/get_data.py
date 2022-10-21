import json

final_dict = {}
count = 0

with open("Final_json.json", "r") as f:
    data = json.loads(f.read())

for q in data['questions']:
    count += 1
    final_dict[count] = {
        "Question is : ": q['question_text'],
    }

    for a in q['answers']:
        if a['is_correct'] is True:
            final_dict[count].update({"Answer : ": a['text']})

with open("final_ans.txt", "w") as f:
    for k, v in final_dict.items():
        f.write(f"{k} {v['Question is : ']} \n ==> {v['Answer : ']}\n\n")

