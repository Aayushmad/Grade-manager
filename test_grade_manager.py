from grade_manager import GradeManager

def test_add_grade():
    gm = GradeManager()
    gm.add_grade(50)
    assert 50 in gm.grades

def test_average():
    gm = GradeManager()
    gm.add_grade(40)
    gm.add_grade(60)
    assert gm.get_average() == 50

def test_pass():
    gm = GradeManager()
    gm.add_grade(50)
    assert gm.is_pass() == True

def test_fail():
    gm = GradeManager()
    gm.add_grade(20)
    assert gm.is_pass() == False