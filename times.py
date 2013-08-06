import simplejson

class Times:
  def __init__(self, json="daft_punk.json"):
    with open(json) as f:
      self.data = simplejson.load(f)

  def bars(self):
    return [t["start"] for t in self.data["bars"]]

  def beats(self):
    return [t["start"] for t in self.data["beats"]]

  def sections(self):
    return [t["start"] for t in self.data["sections"]]
