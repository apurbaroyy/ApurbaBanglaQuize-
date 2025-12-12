from flask import Flask, request, jsonify
import sqlite3, os
app = Flask(__name__)
DB = 'badges.db'

def init_db():
    if not os.path.exists(DB):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute('CREATE TABLE badges (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, score INTEGER, issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
        conn.commit()
        conn.close()

@app.route('/api/issue_badge', methods=['POST'])
def issue_badge():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    score = data.get('score')
    badge_awarded = score >= 3
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('INSERT INTO badges (name, email, score) VALUES (?, ?, ?)', (name, email, score))
    conn.commit()
    conn.close()
    return jsonify({'badge_issued': badge_awarded, 'score': score}), 201

if __name__ == '__main__':
    init_db()
    app.run(port=5000)
