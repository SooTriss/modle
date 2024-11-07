import json

from models import Model

# TODO: update all result score;raw="max", scaled=1, duration=PT{float}S, success=true

def solve_activities(data: Model):
    has_children_in_children = False

    # head statement
    data.statement.result.score.raw = data.statement.result.score.max
    data.statement.result.score.scaled = 1

    # first level children
    for child in data.children:
        try:
            correct_ans = child.statement.object.definition.correctResponsesPattern[0]
            child.statement.result.response = correct_ans

            child.statement.result.score.raw = child.statement.result.score.max
            child.statement.result.score.scaled = 1
            child.statement.result.success = True

        except TypeError:
            has_children_in_children = True
        except AttributeError:
            has_children_in_children = True

    # nested children
    if has_children_in_children:
        for child in data.children:
            if child.children != None: # Model set children to None
                for child in child.children:
                    try:
                        correct_ans = child.statement.object.definition.correctResponsesPattern[0]
                        child.statement.result.response = correct_ans

                        child.statement.result.score.raw = child.statement.result.score.max
                        child.statement.result.score.scaled = 1
                        child.statement.result.success = True
                    except TypeError:
                        has_children_in_children = True
                    except AttributeError:
                        has_children_in_children = True

    # nested nested children
    if has_children_in_children:
        for child in data.children:
            if child.children != None: # Model set children to None
                for child in child.children:
                    if child.children != None: # Model set children to None
                        for child in child.children:
                            correct_ans = child.statement.object.definition.correctResponsesPattern[0]
                            child.statement.result.response = correct_ans

                            child.statement.result.score.raw = child.statement.result.score.max
                            child.statement.result.score.scaled = 1
                            child.statement.result.success = True
    
    return data.json(exclude_none=True) # Removes the children with None


if __name__ == '__main__':
    with open('test_json/video.json', 'r') as f:
        data = Model(**json.loads(f.read()))
    
    print(solve_activities(data))