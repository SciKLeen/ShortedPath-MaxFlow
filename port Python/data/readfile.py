import json
def getData():
    points = "data\points.json"
    edges = "data\edges.json"    
    with open('points.json', encoding='utf-8') as fh:
        points = json.load(fh)
        
    with open('edges.json', encoding='utf-8') as fh1:
        edges = json.load(fh1)
        
        
    return points, edges