from django.shortcuts import render

quizzes = [
	{
		"quiz_number": 1,
		"name": "Rengöring",
		"description": "Vad vet du om hudvårdens grundbult?"
	},

	{
		"quiz_number": 2,
		"name": "Exfoliering",
		"description": "Korn, kemisk eller inte alls?"
	},

	{
		"quiz_number": 3,
		"name": "Återfuktning",
		"description": "Varför serum när det finns crème? Och andra stora frågor."

	},
]

def startpage(request):
	context = {
		"quizzes":quizzes,
	}
	return render(request, "startpage.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[quiz_number - 1],
		"quiz_number":quiz_number,
	}
	return render(request, "quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
		"question_number": question_number,
		"question": "Hur ofta bör du gå på ansiktsbehandling?",
		"answer1": "1 gång om året",
		"answer2": "1 gång i månaden",
		"answer3": "1 gång i veckan",
		"quiz": quizzes[quiz_number -1],
		"quiz_number": quiz_number,

	}
	return render(request, "question.html", context)

def completed(request, quiz_number):
	context = {
		"correct": 12,
		"total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "completed.html", context)


