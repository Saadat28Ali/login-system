from django.http import HttpResponse
from django.shortcuts import render, redirect
import os

os.system("cls");

class LoginRegister:

	def login(request):
		return render(request, "loginpage.html", dict());

	def register(request):
		return render(request, "registrationpage.html", dict());

	def findUser(username: str):
		
		with open(r"D:\Saadat\coding\Django\Projects\LoginRegistration - 28-11-22\LoginRegistration\profiles.txt", "rt") as fh:
			for index, item in enumerate(fh.readlines()):
				if username==item.split(",")[0]:
					return True, index;
			
			return False, -1;

	def loginCredCheck(request):

		username=request.POST.get("username", "");
		password=request.POST.get("password", "");
		response=list();

		if username!="" and password!="":

			with open(r"D:\Saadat\coding\Django\Projects\LoginRegistration - 28-11-22\LoginRegistration\profiles.txt", "rt") as fh:
				'''
				for each in fh.readlines():
					
					if username in each:
						found_line=list(each)[len(username)+2:-2:1];
						found_line="".join(found_line);

						if password==found_line:
							response="Login Successful <br>"
							break;
						else:
							response=f"Password Incorrect <br>";
							break;
					else:
						pass;
				'''
				username_search_results=LoginRegister.findUser(username);

				if username_search_results[0]:

					check_against=(fh.readlines()[username_search_results[1]]).split(", ")[1][:-2:1];
					
					if password==check_against:
						response.append("Login successful");
					else:
						response.append("Password incorrect");

				else:
					response.append("User not found");

				if response==list():
					response.append("Login unsuccessful, check your username and password");
			

		response.append(f"You entered: Username={username} Password={password}");

		return LoginRegister.results(request, response);

	def registerCredCheck(request):

		username=request.POST.get("username", "");
		password=request.POST.get("password", "");
		response=list();

		username_search_results=LoginRegister.findUser(username);

		if not username_search_results[0]:
			with open(r"D:\Saadat\coding\Django\Projects\LoginRegistration - 28-11-22\LoginRegistration\profiles.txt", "at") as fh:
				fh.writelines([f"{username}, {password};\n"]);
				response.append("Registration successful");
		else:
			response.append("Registration unsuccessful, the user profile already exists");

		return LoginRegister.results(request, response);

	def results(request, results_page_content=dict()):

		return render(request, "resultspage.html", {"content_line_list": results_page_content});