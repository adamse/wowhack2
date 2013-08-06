import simplejson

class Times:
  def __init__(self, json="daft_punk.json"):
    with open(json):
      self.data = simplejson.load(f)

  def bars():
    return [t["start"] for t in self.data["bars"]]

  def beats():
    return [t["start"] for t in self.data["beats"]]

  def sections():
    return [t["start"] for t in self.data["sections"]]
