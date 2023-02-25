from flask import Blueprint, render_template

views = Blueprint('views', __name__)

votes = 0


@views.route('/', methods=['GET', 'POST'])
def index_page():
    return render_template("index.html")


@views.route('/index_backup', methods=['GET', 'POST'])
def index_backup_page():
    # if request.method == 'POST':
    #     note = request.form.get('note')  # Gets the note from the HTML

    # if len(note) < 1:
    #     flash('Note is too short!', category='error')
    # else:
    #     new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note
    #     db.session.add(new_note) #adding the note to the database
    #     db.session.commit()
    #     flash('Note added!', category='success')

    return render_template("index_backup.html")


@views.route("/up", methods=["POST"])
def upvote():
    global votes
    votes = votes + 1
    return str(votes)


@views.route("/data", methods=["GET"])
def get_data():
    return {'id': 1, 'test': 'test'}
