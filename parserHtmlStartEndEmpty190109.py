from html.parser import HTMLParser

def loop_through_attrs(attrs):
    for attr in attrs:
        print('-> {} > {}'.format(str(attr[0]), str(attr[1])))

class ExerciseParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : {}".format(str(tag)))
        loop_through_attrs(attrs)

    def handle_endtag(self, tag):
        print("End   : {}".format(str(tag)))

    def handle_startendtag(self, tag, attrs):
        print("Empty : {}".format(str(tag)))
        loop_through_attrs(attrs)

if __name__ == "__main__":
    N = int(input().rstrip())
    parser = ExerciseParser()
    parser.feed(''.join([input().rstrip() for _ in range(N)]))
