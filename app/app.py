import controller
import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    chart_data = controller.completed_item_count_since()
    data = {
        'project': json.dumps(chart_data),
        'priority': json.dumps(controller.group_by_priority(chart_data)),
    }
    return render_template('main.html', name=controller.get_full_name(), data=data)

if __name__ == "__main__":
    app.run(debug=True)
