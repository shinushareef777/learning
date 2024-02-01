from flask import Flask
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
api = Api(app)

budget = {}

budget_args = RequestParser()
budget_args.add_argument("date", type=str, help="Date of spend")
budget_args.add_argument("spent_on", type=str, help="Money spend to")
budget_args.add_argument("amt", type=int, help="Amount spend on")

class BudgetTracker(Resource):
  def get(self, budget_id):
    return budget[budget_id]

  def put(self, budget_id):
    args = budget_args.parse_args()
    return budget[budget_id], 201


api.add_resource(BudgetTracker, '/budget/<int:budget_id>')

if __name__ == "__main__":
  app.run(debug=True)