from mypythonlib import myfunctions

def test_haversine():
    # Amsterdam to Berlin
    assert myfunctions.haversine(
        4.895168, 52.370216, 13.404954, 52.520008
    ) == 576.6625818456291