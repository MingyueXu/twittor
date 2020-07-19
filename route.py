from flask import render_template, url_for
from collections import namedtuple
from twittor.forms import loginform
from flask import redirect

def index():
    variable = namedtuple('Tuple_name',['username'])
    s1 = variable('Mingyue_Xu')
    s2 = variable('Haoyu_Shi')
    posts = []
    variable1 = namedtuple('nt1', ['author','body'])
    x1 = variable1(s1,'I have just established my page!')
    posts.append(x1)
    x2 = variable1(s2, 'Congratulations, my bro!')
    posts.append(x2)
    return render_template('index1.html', name=s1, posts=posts)

def login():
    form = loginform(csrf_enabled=False)
    if form.validate_on_submit():
        message = f'username={form.username.data}, password={form.password.data}, remember_me={form.remember_me.data}'
        print(message)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sing in', form=form)

