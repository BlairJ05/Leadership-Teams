from django.http import HttpRequest
from django.shortcuts import render
from dataclasses import dataclass

@dataclass
class Team:
    name: str
    description: str
    members: list

def team_views(request: HttpRequest) -> render:
    return render(request, "home.html")

def leadership_views(request: HttpRequest, team: str) -> render:
    if team == "management":
        context = {
            "mark": Team(
                "Management Team",
                "Management Team assures that all other teams stay on task. They also make sure chores get done, and keep the building running properly.",
                ["Owen", "Jeremiah", "Nick", "Ab", "Abigail", "Matthew"]
            )
        }
    elif team == "community":
        context = {
            "mark": Team(
                "Community Team",
                "This team plans community events to help give base campers a break from coding. They make sure everyone's birthday is accounted for.",
                ["Jordan", "Joby", "Aj", "Micah", "Caleb"]
            )
        }
    elif team == "procurement":
        context = {
            "mark": Team(
                "Procurement Team",
                "They make sure every base camper is fed. ",
                ["Adrian", "Bryce", "Big John", "Blaine", "Wyatt"]
            )
        }
    elif team == "documentation":
        context = {
            "mark": Team(
                "Documentation Team",
                "Documentation keeps track of everything that happens throughout the year.",
                ["Kayleah", "Conner", "Kaleigh", "Blair", "Mina", "Josh", "Jay"]
            )
        }
    return render(request, "Teams.html", context)