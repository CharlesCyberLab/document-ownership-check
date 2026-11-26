DOCS = {
 1:"userA",
 15:"userA",
 16:"userB",
}

def can_read(user, doc_id):
  owner = DOCS.get(doc_id)
  return owner is not None and owner == user

TITLES = {
  1: "A's budget",
  15: "A's private plan",
  16: "B's notes",
}

def open_document(user, doc_id):
  if can_read(user, doc_id):
     return TITLES[doc_id]
  return "Access denied" 

TESTS = [
  ("userA", 15, True),
  ("userB", 15, False),
  ("userB", 16, True),
  ("userA", 16, False),
  ("userA", 99, False),
  ("userB", 1, False),
  (None, 15, False),
  (None, 99, False),
] 

passed = 0
for user, doc_id, expected in TESTS:
  actual = can_read(user, doc_id)
  if actual == expected:
     passed += 1
  print(user, doc_id, "expected", expected, "got", actual)
print(passed, "of", len(TESTS), "passed")

while True:
  who = input("who is asking? (userA, userB, none, or q to quit):")
  if who == "q":
     break
  if who == "none":
     who = None
  number = input("which document number?")
  if not number.isdigit():
     print("Please type a number")
     continue
  print(open_document(who, int(number)))
