from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
import surveys

app = Flask(__name__)
# Ensure that debug mode is *on*
app.debug = True
app.config['SECRET_KEY'] = "password"
debug = DebugToolbarExtension(app)

responses = []
ind = 0 
# for i in range(len(surveys.satisfaction_survey.questions)):
    # print(surveys.satisfaction_survey.questions[i].question)

@app.route('/')
def home_page():
    survey_title = surveys.satisfaction_survey.title
    survey_instructions = surveys.satisfaction_survey.instructions
    ind = 0
    responses.clear()
    return render_template("home.html", survey_title=survey_title, survey_instructions=survey_instructions)


@app.route('/questions/<int:ind>', methods=["POST","GET"])
def question_page(ind):
    # print(surveys.satisfaction_survey.questions[ind].question)
    # print(len(surveys.satisfaction_survey.questions),"LENGTH OF SURVEY QUESTIONS")
    if ind != len(responses):
        flash('invalid question you have been redirected to your most up to date question' )
        return redirect(f"/questions/{len(responses)}")
    if ind < len(surveys.satisfaction_survey.questions):
        questions_question = surveys.satisfaction_survey.questions[ind].question 
        questions_choices = surveys.satisfaction_survey.questions[ind].choices
        return render_template("questions.html" , questions_question=questions_question, questions_choices=questions_choices, ind=ind)
    return "<h1>Thank you!</h1>"

@app.route('/answer', methods=["POST","GET"])
def answer_page():
    answer = request.form['yesorno']
    responses.append(answer)
    print(responses)
    return redirect(f"/questions/{len(responses)}")


# @app.route('/movies/new', methods=["POST"])
# def add_movie():
#     title = request.form["title"]
#     if title in MOVIES:
#         flash('Movie exists', 'error')
#     else:
#         MOVIES.add(title)
#         flash("Added!", 'success')
    
#     return redirect("/movies")

    
