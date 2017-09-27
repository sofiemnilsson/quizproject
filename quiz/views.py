from django.shortcuts import render

def startpage(request):
	return render(request, "startpage.html")

def quiz(request, quiz_number):
	return render(request, "quiz.html")

def question(request, quiz_number, question_number):
	return render(request, "question.html")

def completed(request, quiz_number):
	return render(request, "completed.html")


quizzes = [
	{
		"quiz_number": 1,
		"name": "Klassiska böcker"
		"description": "Hur bra kan du dina klassiker?"
	},

	{
		"quiz_number": 2,
		"name": "Störst fotbollslagen",
		"description": "Kan du dina lag?"
	},

	{
		"quiz_number": 3,
		"name": "Världens mest kända hackare",
		"description": "Kan du din hackerhistoria?"

	},
]