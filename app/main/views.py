from flask_login import login_required
from flask import render_template,redirect,url_for,request,abort,flash
from ..models import User,Post,Comment