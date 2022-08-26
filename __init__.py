from crypt import methods
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_books(request, questions):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    books = [question.format() for question in questions]
    current_books = books[start:end]

    return current_books

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers 
    # =1=====-----backend is set up --------------------------
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response


    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
     @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    #=================DONE==================

  


    @app.route('/v1/categories', methods=['GET'])
    def category():
        categories = Category.query.all()
        category = [category.format() for category in categories]
        
        print(category)
        

        return jsonify({
            'success': True,
            'category' : category,
            
                                  
        
        })


    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
#=================================DONE=================================


# controller function for handling getting questions from category.

    @app.route('/v1/categories/<int:category_id>/questions', methods=['GET'])
    def question(category_id):

        categories = Category.query.filter(Category.id==category_id)
        questions = Question.query.filter(Question.category==category_id).all()

        category = [category.format() for category in categories]
        current_books = paginate_books(request, questions)
        print(category_id)
        print(category)
       
                

        return jsonify({
            'success': True,
            'questions' : current_books,
            'category' : category,
            
            })



    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """

    #========================DONE=====================================================

    @app.route('/v1/questions/<int:question_id>', methods=['GET'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id== question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()
            questions = Question.query.order_by(Question.id).all()
            current_books = paginate_books(request, questions)

            print(question)
            print(len(Question.query.all()))
            print('deleted!')
            
            return jsonify({
                'success': True,
                'deleted' : question_id,   
                'questions' : current_books,
                'total_questions' : len(Question.query.all())
                })
        except:
            print('aborted')
            abort(422)

"""
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
            

#============================DONE==========================================


            


       

  

"""
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    return app

