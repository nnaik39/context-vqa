import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import json

sns.set_theme(style='whitegrid')

df = pd.read_csv('results/pilot_2_imgversion.csv')

with open('tags/question_types_all.json') as f:
   question_types_json = json.load(f)

with open('tags/ratings_txt.json') as f:
   ratings_txt = json.load(f)

with open('tags/stddev_txt.json') as f:
   std_dev_txt = json.load(f)

categories = ["shopping", "science_journals", "health", "news", "travel", "social_media"]

how = {}
what = {}
where = {}
was = {}
why = {}
who = {}

ratings = {}

std_dev = {}

questions_per_category = {}

for category in categories:
    row = df.loc[df['category'] == category]

    how[category] = 0
    what[category] = 0
    where[category] = 0
    why[category] = 0
    was[category] = 0
    who[category] = 0

    total_questions = 0

    for (cur_question, cur_img) in zip(row['question'], row['image']):
        question = cur_question
        image = cur_img 

        total_questions += 1
            
        question_type = question_types_json[question]

        if (question_type == 'How'):
            how[category] += 1
        elif (question_type == 'Why'):
            why[category] += 1
        elif (question_type == 'Where'):
            where[category] += 1
        elif (question_type == 'Who'):
            who[category] += 1
        elif (question_type == 'What'):
            what[category] += 1
        elif (question_type == 'Is'):
            was[category] += 1

    questions_per_category[category] = total_questions

    how[category] /= total_questions
    what[category] /= total_questions
    where[category] /= total_questions
    why[category] /= total_questions
    was[category] /= total_questions
    who[category] /= total_questions

question_types = ['what', 'is', 'where', 'how', 'why', 'who']

formatted_categories = ["Shopping", "Science Magazines", "Health", "News", "Travel", "Social Media"]
colors = ['#77AADD', '#99DDFF', '#44BB99', '#BBCC33', '#AAAA00', '#EEDD88']

question_type_list_map = {
    'how': how,
    'what': what,
    'where': where,
    'why': why,
    'is': was,
    'who': who
}

images = []

numCategories = {}

std_dev = {}

for question_type in question_types:
    ratings[question_type] = []
    std_dev[question_type] = [0, 0, 0, 0, 0, 0]

    for i in range(0, len(categories)):
        context = categories[i]

        ratings[question_type].append(question_type_list_map[question_type][context])

        numTypeQuestions = question_type_list_map[question_type][context] * questions_per_category[context]

        std_dev[question_type][i] = (1 - (ratings[question_type][i])) ** 2 * numTypeQuestions
        + (ratings[question_type][i])**2 * (questions_per_category[context] - numTypeQuestions)

        std_dev[question_type][i] /= questions_per_category[context]

fig, ax = plt.subplots(2, 6, sharex=True, sharey=True)
fontsize = 17

for i,row in enumerate(ax):
    for j,col in enumerate(row):
        question_type = question_types[j]
        formatted_question_type = question_type.capitalize()

        col.set_title('{}'.format(formatted_question_type), fontsize=fontsize)

        if (i == 1):
            col.bar(formatted_categories,
                 ratings[question_type],
                 color = colors,
                 edgecolor='black',
                 yerr=[yi/2 for yi in std_dev[question_type]],
                capsize=2
            )
        else:
            col.bar(formatted_categories,
                 ratings_txt[question_type],
                 color = colors,
                 edgecolor='black',
                 yerr=[yi/2 for yi in std_dev_txt[question_type]],
                capsize=2
            )
        
        col.tick_params(axis='x', labelsize=17)
        if (j == 0):
            col.set_ylim(bottom=0, top=0.65)

fig.autofmt_xdate(rotation=45)

plt.subplots_adjust(wspace=0.1)

plt.show()