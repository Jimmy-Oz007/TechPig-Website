from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "techpig-secret-key"


# ---------------------------------------------------
# PROJECT DATA
# ---------------------------------------------------

projects = [
    {
        "number": 1,
        "name": "Raspberry Pi Cyberdeck",
        "category": "Hardware",
        "status": "Completed",
        "description": "A portable Raspberry Pi 5 cyberdeck with touchscreen, keyboard and Linux tools."
    },
    {
        "number": 2,
        "name": "TechPig Website",
        "category": "Web Development",
        "status": "In Progress",
        "description": "The official website for the TechPig 100 Projects challenge."
    },
    {
        "number": 3,
        "name": "Save the House",
        "category": "Game Development",
        "status": "In Progress",
        "description": "A game about managing household electricity and saving money."
    },
    {
        "number": 4,
        "name": "Roblox Game",
        "category": "Game Development",
        "status": "Planned",
        "description": "A beginner Roblox game built using Roblox Studio and Lua."
    },
    {
        "number": 5,
        "name": "Basketball Manager",
        "category": "Game Development",
        "status": "Planned",
        "description": "A basketball management game inspired by football management games."
    },
    {
        "number": 6,
        "name": "LLM Work Logger",
        "category": "Artificial Intelligence",
        "status": "Completed",
        "description": "An LLM-powered application for recording work hours and project activity."
    },
    {
        "number": 7,
        "name": "Personal AI Assistant",
        "category": "Artificial Intelligence",
        "status": "Planned",
        "description": "A basic AI assistant capable of answering questions and helping with tasks."
    },
    {
        "number": 8,
        "name": "Home Network Scanner",
        "category": "Cybersecurity",
        "status": "Planned",
        "description": "A tool that identifies devices connected to a local network."
    },
    {
        "number": 9,
        "name": "Weather Dashboard",
        "category": "Web Development",
        "status": "Planned",
        "description": "A web dashboard that displays live weather information using an API."
    },
    {
        "number": 10,
        "name": "Cloud File Storage App",
        "category": "Cloud",
        "status": "Planned",
        "description": "A simple cloud-based application for storing and retrieving files."
    },
    {
        "number": 11,
        "name": "Password Generator",
        "category": "Cybersecurity",
        "status": "Planned",
        "description": "A tool for generating strong random passwords."
    },
    {
        "number": 12,
        "name": "Expense Tracker",
        "category": "Web Development",
        "status": "Planned",
        "description": "A simple application for recording expenses and tracking spending."
    },
    {
        "number": 13,
        "name": "Spotify E-Paper Display",
        "category": "Hardware",
        "status": "Planned",
        "description": "An e-paper display that shows the currently playing Spotify track."
    },
    {
        "number": 14,
        "name": "DIY MP3 Player",
        "category": "Hardware",
        "status": "Planned",
        "description": "A portable MP3 player built using small electronic components."
    },
    {
        "number": 15,
        "name": "Discord Bot",
        "category": "Automation",
        "status": "Planned",
        "description": "A Discord bot capable of responding to commands and automating tasks."
    }
]


# ---------------------------------------------------
# DATABASE
# ---------------------------------------------------

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            project_name TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ---------------------------------------------------
# HOME
# ---------------------------------------------------

@app.route("/")
def home():
    completed = len(
        [project for project in projects if project["status"] == "Completed"]
    )

    in_progress = len(
        [project for project in projects if project["status"] == "In Progress"]
    )

    planned = len(
        [project for project in projects if project["status"] == "Planned"]
    )

    return render_template(
        "index.html",
        projects=projects,
        completed=completed,
        in_progress=in_progress,
        planned=planned
    )


# ---------------------------------------------------
# PROJECTS
# ---------------------------------------------------

@app.route("/projects")
def project_list():
    return render_template(
        "projects.html",
        projects=projects
    )


# ---------------------------------------------------
# CATEGORIES
# ---------------------------------------------------

@app.route("/categories")
def categories():
    category_list = sorted(
        list(set(project["category"] for project in projects))
    )

    return render_template(
        "categories.html",
        projects=projects,
        categories=category_list
    )


# ---------------------------------------------------
# SUGGEST PROJECT
# ---------------------------------------------------

@app.route("/suggest", methods=["GET", "POST"])
def suggest():
    if request.method == "POST":

        name = request.form.get("name")
        project_name = request.form["project_name"]
        category = request.form["category"]
        description = request.form["description"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO suggestions
            (name, project_name, category, description)
            VALUES (?, ?, ?, ?)
        """, (
            name,
            project_name,
            category,
            description
        ))

        conn.commit()
        conn.close()

        flash("Thanks! Your project idea has been submitted.")

        return redirect("/suggest")

    return render_template("suggest.html")


# ---------------------------------------------------
# ABOUT
# ---------------------------------------------------

@app.route("/about")
def about():
    return render_template("about.html")


# ---------------------------------------------------
# RUN WEBSITE
# ---------------------------------------------------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)