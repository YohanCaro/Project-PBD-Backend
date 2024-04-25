from app.controller import query_rh
from flask import Blueprint

main = Blueprint('rh_blueprint',__name__)

@main.route("/employees")
def get_employees():
    return query_rh.get_all_employees()

@main.route("/jobs")
def get_jobs():
    return query_rh.get_all_jobs()

@main.route("/jobshistories")
def get_jobs_histories():
    return query_rh.get_all_job_histories()

@main.route("/departments")
def get_departments():
    return query_rh.get_all_departments()