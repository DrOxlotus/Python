import re

string = """A very bad bedtime story.

Once upon a time, in a place far, far away called {a place}, there was a {an adjective} princess known as {female celebrity}. Her kingdom was tiny, but her {body part} was much, much bigger.

She was very beautiful from her {body part} to her {human organ}. One day she noticed a {an adjective} prince named {male celebrity}. He had a {an adjective} face. As soon as his {body part} touched her {body part}, they fell deeply in love. They were married at {a place} the following day. The End!
"""

res = re.split(r"\s+(?=[^()]*(?:\{|$))", """A very bad bedtime story.

Once upon a time, in a place far, far away called {a place}, there was a {an adjective} princess known as {female celebrity}. Her kingdom was tiny, but her {body part} was much, much bigger.

She was very beautiful from her {body part} to her {human organ}. One day she noticed a {an adjective} prince named {male celebrity}. He had a {an adjective} face. As soon as his {body part} touched her {body part}, they fell deeply in love. They were married at {a place} the following day. The End!
""")

test = string.split()

for word in test:
    print(word + " " + str(test.index(word)))
