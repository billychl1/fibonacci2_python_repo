from flask import Blueprint, render_template, flash
from flask import current_app, redirect, request, url_for



admin = Blueprint("admin", __name__, template_folder="templates")
