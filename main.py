from flask import Flask, request, render_template
import json
from utils import load_candidates, get_candidates_by_name, get_candidate_by_id, get_candidates_by_skill
from utils import get_candidates_by_first_name

file_json = "candidates.json"

app = Flask(__name__)

@app.route('/')
def get_name():
    names = load_candidates(file_json)
    return render_template("list.html", names=names)

@app.route('/candidate/<name>')
def get_candidate_by_name(name):
     candidate = get_candidates_by_name(name)
     return render_template("single.html", cand=candidate)

@app.route('/search/<first_name>')
def get_candidates_first_name(first_name):
     candidates = get_candidates_by_first_name(first_name)
     quantity = len(candidates)

     return render_template("search.html", names=candidates, quantity = quantity)

@app.route('/skill/<skill>')
def get_candidate_skill(skill):
     candidates = get_candidates_by_skill(skill)
     quantity = len(candidates)

     return render_template("skill.html", candidates=candidates, skill=skill, quantity=quantity)

app.run(debug=True)

