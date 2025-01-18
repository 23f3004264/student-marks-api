# api/index.py
import json
from http.server import BaseHTTPRequestHandler

# Marks data
marks_data = [{"name":"m","marks":96},{"name":"hEzKFJ001x","marks":24},{"name":"IA5sgd5A","marks":10},{"name":"4DrYXd06","marks":7},{"name":"wKfYTrUucb","marks":61},{"name":"eva","marks":85},{"name":"v","marks":99},{"name":"CTS1u","marks":80},{"name":"V6rjPi","marks":90},{"name":"5OJUWRg","marks":13},{"name":"LN","marks":14},{"name":"Tt8vrU","marks":82},{"name":"urITl","marks":24},{"name":"ZPhhnWKvia","marks":51},{"name":"luoSUznn","marks":44},{"name":"6RHp02A","marks":35},{"name":"cTblKApDlG","marks":28},{"name":"aO","marks":96},{"name":"oRU","marks":45},{"name":"imR","marks":50},{"name":"aiuQKxeer","marks":74},{"name":"cLMfhkrdM","marks":34},{"name":"feJhUzE","marks":33},{"name":"IY9zc","marks":38},{"name":"QwoOirL6","marks":24},{"name":"s","marks":10},{"name":"B7","marks":53},{"name":"m3Gmn1a","marks":31},{"name":"iJy5w","marks":4},{"name":"Rj","marks":94},{"name":"nUateC1Cy","marks":68},{"name":"pd6in","marks":10},{"name":"JbnerL","marks":86},{"name":"HSKsNObC4","marks":25},{"name":"RK4","marks":61},{"name":"M7","marks":23},{"name":"es6dEv3cq","marks":73},{"name":"nbJ0AzC","marks":39},{"name":"3EGbLGhfTu","marks":67},{"name":"otHIUvVB","marks":41},{"name":"3cS","marks":79},{"name":"qNdzt","marks":26},{"name":"P","marks":15},{"name":"XLI","marks":66},{"name":"Y1TXalna","marks":71},{"name":"Pd2oWii","marks":55},{"name":"q9RbjGhMij","marks":92},{"name":"i13s86CSje","marks":20},{"name":"i6ERBuSB","marks":46},{"name":"NE","marks":40},{"name":"LG","marks":65},{"name":"YHTCs","marks":89},{"name":"0j","marks":7},{"name":"T","marks":63},{"name":"M8KL","marks":5},{"name":"50V12g","marks":82},{"name":"qtT5SC","marks":18},{"name":"Hr4hmXJ","marks":36},{"name":"Ud","marks":12},{"name":"Wkn6XZqW","marks":12},{"name":"9tRru","marks":36},{"name":"AY","marks":1},{"name":"NX","marks":93},{"name":"nfE","marks":14},{"name":"Dnn95rJk00","marks":74},{"name":"dCg7oyo","marks":30},{"name":"q7wDu0q5o","marks":55},{"name":"w","marks":91},{"name":"H7","marks":25},{"name":"YAJl61","marks":61},{"name":"ZIVL","marks":96},{"name":"PS","marks":17},{"name":"OSGGM","marks":8},{"name":"Lw","marks":63},{"name":"ilQNEMDi","marks":92},{"name":"mzJ","marks":82},{"name":"9LlInbT","marks":26},{"name":"f","marks":91},{"name":"5ml4n2xA","marks":93},{"name":"nc","marks":54},{"name":"TTx","marks":98},{"name":"MWrG","marks":54},{"name":"X9","marks":33},{"name":"sBrI0bWa","marks":82},{"name":"4N7bCo95XG","marks":30},{"name":"Iup3od0T","marks":47},{"name":"BrCaxKUlQ","marks":58},{"name":"A5S07Vsv","marks":47},{"name":"k1cNrzjz","marks":45},{"name":"LY5x738OW","marks":4},{"name":"xmu42lSm","marks":82},{"name":"9HY5l2","marks":27},{"name":"lB41gF2","marks":44},{"name":"h7iyIicfmb","marks":85},{"name":"S0Xzu3X","marks":47},{"name":"EzT49zj","marks":79},{"name":"mee","marks":60},{"name":"tJUNVvJx","marks":94},{"name":"TjgkEyv","marks":7},{"name":"lydRJur","marks":24}]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query_string = self.path.split("?")[-1]
        params = [param.split("=")[1] for param in query_string.split("&") if param.startswith("name")]
        
        # Get marks for names
        marks = [marks_data.get(name, 0) for name in params]

        # Return JSON response
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"marks": marks}).encode("utf-8"))
        return
