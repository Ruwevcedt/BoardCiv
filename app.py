import random
from functools import wraps
from flask import Flask, render_template, session, redirect

from BoardGame import Room

app = Flask(__name__)
app.secret_key = str(random.random())

games = [
    Room.Room(host=random.random()),
    Room.Room(host=random.random()),
    Room.Room(host=random.random()),
    Room.Room(host=random.random()),
    Room.Room(host=random.random()),
    Room.Room(host=random.random()),
    Room.Room(host=random.random()),
    Room.Room(host=random.random()),
    Room.Room(host=random.random()),
    Room.Room(host=random.random()),
    Room.Room(host=random.random()),
]
[_game.add_player(player=random.random()) for _game in games]
[_game.add_player(player=random.random()) for _game in games]
[_game.add_player(player=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]
[_game.add_observer(observer=random.random()) for _game in games]

def session_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        return func(*args, **kwargs) if 'id' in session else redirect('/')
    return decorated_function


@app.route('/')
def facade():
    session['id'] = random.random() if 'id' not in session else session['id']
    return render_template('facade.html', session=session)


@app.route('/hall')
@session_required
def hall():
    return render_template('hall.html', session=session, room_list=reversed(games))


@app.route('/room/<host_session_id>')
@session_required
def room(host_session_id: float):
    room_by_host_session_id = [_game for _game in games if _game.host == host_session_id]
    if room_by_host_session_id:
        room_by_host_session_id = room_by_host_session_id[0]
    elif session['id'] == host_session_id:
        room_by_host_session_id = Room.Room(host_session_id)
        games.append(room_by_host_session_id)
    else:
        return redirect('/hall') # todo: 무조건 /로 가버리는디 왜이란지 몰루...
    return render_template('room.html', room=room_by_host_session_id)


if __name__ == '__main__':
    app.run()
