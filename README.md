# TechPig Website 🐷

**Project #001 | 100 Projects Challenge**

Build. Learn. Repeat.

Welcome to the official repository for the TechPig website, the first project in my **100 Projects Challenge**.

The goal of this challenge is to build 100 different technology projects, develop practical skills, experiment with new technologies, and document the learning process along the way.

For Project #001, I decided to build a website that would serve as the central hub for the entire challenge.

## About the Project

TechPig is a personal technology project platform designed to showcase and track my progress as I complete 100 projects.

The website will continue evolving throughout the challenge, with new features introduced in future versions.

## Version 1.0 — Features

Version 1 establishes the foundation of the TechPig website.

### Homepage
- Introduction to TechPig and the 100 Projects Challenge
- Project progress tracker
- Overview of completed, ongoing, and planned projects

### 100 Projects
- Project cards displaying names, descriptions, and categories
- Project status indicators
- Search functionality
- Status-based filtering

### Categories
- Projects organised by technology category
- Support for web development, hardware, AI, game development, cybersecurity, and more

### Suggest a Project
- Visitors can submit project ideas
- Optional name field
- Project category selection
- Suggestions stored in an SQLite database

### About
- Introduction to the TechPig initiative
- Explanation of the 100 Projects Challenge
- Overview of the project's goals

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| HTML | Website structure |
| CSS | Styling and responsive design |
| JavaScript | Search, filtering, and navigation |
| SQLite | Project suggestion storage |
| Jinja2 | Dynamic HTML templates |

## Project Structure

```text
TechPig-Website/
│
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── projects.html
│   ├── categories.html
│   ├── suggest.html
│   └── about.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

The SQLite database is created automatically when the application runs.

## Running the Website Locally

**1. Clone the repository**

```bash
git clone https://github.com/Jimmy-Oz007/TechPig-Website.git
```

**2. Navigate to the project folder**

```bash
cd TechPig-Website
```

**3. Install Flask**

```bash
python -m pip install flask
```

**4. Run the application**

```bash
python app.py
```

On Windows, `py app.py` can also be used.

**5. Open the website**

Visit:

http://127.0.0.1:5000

The website will run locally in your browser.

## Development Roadmap

### Version 1.0 — Foundation
- [x] Homepage
- [x] Project tracking
- [x] Project categories
- [x] Search and filtering
- [x] Suggestion form
- [x] SQLite integration
- [x] Responsive layout

### Version 2.0 — Project Showcase
- [ ] Individual project pages
- [ ] Project screenshots
- [ ] GitHub repository links
- [ ] Embedded YouTube videos
- [ ] Project build logs
- [ ] Improved suggestion management
- [ ] Interface improvements

### Version 3.0 — Expansion
- [ ] Production deployment
- [ ] Improved database infrastructure
- [ ] Project voting system
- [ ] Advanced project filtering
- [ ] Additional community features
- [ ] Performance and security improvements

These features are planned and may change during development.

## The 100 Projects Challenge

This website is Project #001 of a larger challenge to build 100 technology projects.

Projects will explore different areas, including:

- Software development
- Web development
- Artificial intelligence
- Cybersecurity
- Game development
- Hardware and electronics
- Automation
- Cloud computing

The objective is to learn through practical development rather than relying entirely on theory.

Each project will be an opportunity to experiment, solve problems, and improve.

## YouTube

The development journey is documented on the TechPig YouTube channel.

**YouTube:** https://www.youtube.com/@TheTechPig

Videos will cover project showcases, updates, challenges, and lessons learned.

## GitHub

Explore my other projects:

https://github.com/Jimmy-Oz007

## Current Status

**Version:** 1.0

**Project:** #001 / 100

**Development:** Ongoing

The website will continue receiving updates as the challenge progresses.

---

**TechPig — Build. Learn. Repeat.**

*1 down. 99 to go.*
