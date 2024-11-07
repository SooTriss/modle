import json

from xapiresult import solve_activities
from models import Model

from mitmproxy import ctx
from mitmproxy import http


class EditMoodleH5P:
    def __init__(self):
        self.total_time = 0 # seconds

    def request(self, flow: http.HTTPFlow):
        if flow.request.pretty_url.endswith('action=set_finished'):
            ctx.log.info(f"H5P Submit: Trying to solve for {flow.request.urlencoded_form['contentId']}")

            flow.request.urlencoded_form['score'] = flow.request.urlencoded_form['maxScore']

            ctx.log.info(f"H5P Submit: Score set to {flow.request.urlencoded_form['maxScore']}.")
        
        if flow.request.pretty_url.endswith('action=xapiresult'):
            h5p_result = json.loads(flow.request.urlencoded_form['xAPIResult'])
            answered_result = solve_activities(Model(**h5p_result))
            flow.request.urlencoded_form['xAPIResult'] = answered_result

            ctx.log.info("H5P Submit: All answers set to correct.")

addons = [
    EditMoodleH5P()
]
