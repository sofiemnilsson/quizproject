from quiz.models import Quiz
from django.shortcuts import render

# quizzes = [
# 	{
# 		"quiz_number": 1,
# 		"name": "K-beauty basics",
# 		"description": "Grunderna inom K-beauty."
# 	},

# 	{
# 		"quiz_number": 2,
# 		"name": "Hudvård",
# 		"description": "Frågor om masker, märken och mists."
# 	},

# 	{
# 		"quiz_number": 3,
# 		"name": "Koreansk export",
# 		"description": "Vad vet du sydkoreanska influenser?"

# 	},
# ]

def startpage(request):
	context = {
		"quizzes": Quiz.objects.all(),
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
		"question": "Vad betyder 'gwang'?",
		"answer1": "Pormask",
		"answer2": "Yttorrhet",
		"answer3": "Strålande glow",
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


